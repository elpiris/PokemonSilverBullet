#!/usr/bin/env python3
"""Check trainer levels in story order against the next boss and write TRAINER_LEVELS_AUDIT.md.

Run from the repo root: python tools/audit_trainers.py
Exits with status 1 if a check fails.
"""
import glob
import os
import re
import sys

BOSSES = {"FALKNER", "WHITNEY", "BUGSY", "MORTY", "PRYCE", "JASMINE", "CHUCK", "CLAIR", "RIVAL1", "RIVAL2", "WILL", "BRUNO",
          "KAREN", "KOGA", "CHAMPION", "BROCK", "MISTY", "LT_SURGE", "ERIKA", "JANINE", "SABRINA", "BLAINE", "RED", "BLUE",
          "EXECUTIVEM", "EXECUTIVEF", "CAL"}

# Story order: (next boss, its ace's level, maps)
AREAS = [
    ("Falkner", 10, ["Route30", "Route31", "SproutTower1F", "SproutTower2F", "SproutTower3F", "VioletGym"]),
    ("Bugsy", 17, ["Route32", "UnionCave1F", "Route33", "SlowpokeWellB1F", "AzaleaGym"]),
    ("Whitney", 20, ["Route34", "GoldenrodUnderground", "Route35", "NationalPark", "GoldenrodGym"]),
    ("Morty", 26, ["Route36", "Route37", "Route46", "RuinsOfAlphOutside", "DanceTheater", "BurnedTower1F", "EcruteakGym"]),
    ("Chuck", 32, ["Route38", "Route39", "Route40", "Route41", "OlivineLighthouse2F", "OlivineLighthouse3F", "OlivineLighthouse4F",
                   "OlivineLighthouse5F", "CianwoodGym"]),
    ("Pryce", 36, ["Route42", "Route43", "LakeOfRage", "UnionCaveB1F", "UnionCaveB2F", "TeamRocketBaseB1F", "TeamRocketBaseB2F",
                   "TeamRocketBaseB3F", "MahoganyGym", "MountMortarB1F"]),
    ("Radio Tower boss", 39, ["RadioTower1F", "RadioTower2F", "RadioTower3F", "RadioTower4F", "RadioTower5F",
                              "GoldenrodUndergroundSwitchRoomEntrances", "GoldenrodUndergroundWarehouse"]),
    ("Clair", 41, ["Route44", "Route45", "BlackthornGym1F", "BlackthornGym2F"]),
    ("Will", 44, ["Route26", "Route27"]),
    ("Kanto leaders", 54, ["FastShipB1F", "FastShipCabins_NNW_NNE_NE", "FastShipCabins_SE_SSE_CaptainsCabin", "FastShipCabins_SW_SSW_NW",
                           "Route1", "Route2", "Route3", "Route4", "Route8", "Route9", "Route10South", "Route11", "Route12", "Route13",
                           "Route14", "Route15", "Route17", "Route18", "Route19", "Route20", "Route21", "Route24", "Route25",
                           "PewterGym", "CeruleanGym", "VermilionGym", "CeladonGym", "FuchsiaGym", "SaffronGym"]),
]

# These three stand on Route 34's pond, which needs Surf, so they answer to a later boss.
CAP_OVERRIDE = {"IRENE": ("Chuck", 32), "JENN": ("Chuck", 32), "KATE": ("Chuck", 32)}

# Fuchsia Gym's trainers are loaded by its disguise scripts instead of `trainer` lines.
LOADTRAINER_FIRST_FIGHTS = {"FuchsiaGym"}

# Boss ace levels, in story order.
BOSS_CURVE = [("Falkner", "FALKNER"), ("Bugsy", "BUGSY"), ("Whitney", "WHITNEY"), ("Morty", "MORTY"), ("Chuck", "CHUCK"),
              ("Jasmine", "JASMINE"), ("Pryce", "PRYCE"), ("Clair", "CLAIR"), ("Will", "WILL"), ("Koga", "KOGA"), ("Bruno", "BRUNO"),
              ("Karen", "KAREN"), ("Lance", "CHAMPION"), ("Janine", "JANINE"), ("Brock", "BROCK"), ("Lt. Surge", "LT_SURGE"),
              ("Erika", "ERIKA"), ("Misty", "MISTY"), ("Sabrina", "SABRINA"), ("Blaine", "BLAINE"), ("Blue", "BLUE"), ("Red", "RED")]

# Rematch unlocks, in story order, with the next boss's ace.
GATES = [("ENGINE_FLYPOINT_GOLDENROD", "Whitney", 20), ("ENGINE_FLYPOINT_ECRUTEAK", "Morty", 26), ("ENGINE_FLYPOINT_OLIVINE", "Chuck", 32),
         ("ENGINE_FLYPOINT_CIANWOOD", "Jasmine", 34), ("ENGINE_FLYPOINT_LAKE_OF_RAGE", "Pryce", 36), ("ENGINE_FLYPOINT_MAHOGANY", "Pryce", 36),
         ("EVENT_CLEARED_ROCKET_HIDEOUT", "Radio Tower boss", 39), ("EVENT_CLEARED_RADIO_TOWER", "Clair", 41),
         ("ENGINE_FLYPOINT_BLACKTHORN", "Clair", 41), ("EVENT_BEAT_ELITE_FOUR", "Kanto leaders", 54),
         ("EVENT_RESTORED_POWER_TO_KANTO", "Kanto leaders", 54)]
GATE_ORDER = {g[0]: i for i, g in enumerate(GATES)}

MAX_TEAM_GAP = 8  # A Pokemon this far below its teammates is left over from an uneven bump.


def load_parties():
    """Return {(class, trainer constant): [(level, species)]}."""
    groups = []
    for line in open("data/trainers/parties.asm", encoding="utf8"):
        if re.match(r"\w+Group:", line):
            groups.append([])
        elif re.match(r'\s*db ".*@", TRAINERTYPE_', line) and groups:
            groups[-1].append([])
        else:
            m = re.match(r"\s*db\s+(\d+),\s*(\w+)", line)
            if m and groups and groups[-1]:
                groups[-1][-1].append((int(m.group(1)), m.group(2)))
    classes = []
    for line in open("constants/trainer_constants.asm", encoding="utf8"):
        m = re.match(r"\s*trainerclass (\w+)", line)
        if m:
            classes.append((m.group(1), []))
            continue
        m = re.match(r"\s*const (\w+)", line)
        if m and classes:
            classes[-1][1].append(m.group(1))
    classes = [c for c in classes if c[0] != "TRAINER_NONE"]
    assert len(classes) == len(groups)
    parties = {}
    for (cls, names), teams in zip(classes, groups):
        for name, team in zip(names, teams):
            parties[(cls, name)] = team
    return parties


def rematches(parties):
    """Return [(map, class, trainer, gate)] for phone rematch fights, reading each script top to bottom."""
    out = []
    for path in sorted(glob.glob("maps/*.asm")):
        name = os.path.basename(path)[:-4]
        last_check = None
        branch = {}
        label = None
        for line in open(path, encoding="utf8"):
            t = line.strip()
            m = re.match(r"(?:checkflag|checkevent)\s+(\w+)", t)
            if m:
                last_check = m.group(1)
            m = re.match(r"iftrue\s+\.(\w+)", t)
            if m and last_check:
                branch[m.group(1)] = last_check
            m = re.match(r"\.(\w+):", t)
            if m:
                label = m.group(1)
            m = re.match(r"loadtrainer\s+(\w+),\s*(\w+)", t)
            if m and label and "Fight" in label and m.group(1) not in BOSSES and (m.group(1), m.group(2)) in parties:
                out.append((name, m.group(1), m.group(2), branch.get(label)))
    return out


def main():
    sys.stdout.reconfigure(encoding="utf8")
    parties = load_parties()
    report = ["# Trainer levels audit", "", "Generated by `tools/audit_trainers.py`. This checks the data only, not how the fights play.", ""]
    problems = []

    report += ["## Boss curve", "", "| Boss | Levels | Team |", "|---|---|---|"]
    for label, cls in BOSS_CURVE:
        team = next(t for (c, n), t in parties.items() if c == cls)
        levels = [m[0] for m in team]
        report.append(f"| {label} | {min(levels)}-{max(levels)} | {len(team)} |")
    report.append("")

    report += ["## First fights", "", "A trainer's strongest Pokémon must be below the next boss's ace.", "",
               "| Next boss | Ace | Lowest trainer top | Highest trainer top | Trainers |", "|---|---|---|---|---|"]
    seen = set()
    for boss, cap, maps in AREAS:
        tops = []
        for name in maps:
            text = open(f"maps/{name}.asm", encoding="utf8").read()
            fights = re.findall(r"^\s*trainer\s+(\w+),\s*(\w+)", text, re.M)
            if name in LOADTRAINER_FIRST_FIGHTS:
                fights += re.findall(r"^\s*loadtrainer\s+(\w+),\s*(\w+)", text, re.M)
            for cls, trainer in fights:
                team = parties.get((cls, trainer))
                if cls in BOSSES or not team or (name, cls, trainer) in seen:
                    continue
                seen.add((name, cls, trainer))
                top = max(m[0] for m in team)
                tops.append(top)
                who, limit = CAP_OVERRIDE.get(trainer, (boss, cap))
                if top >= limit:
                    problems.append(f"{name}: {trainer} has Lv{top}, not below {who} ({limit})")
                low = min(m[0] for m in team)
                if top - low > MAX_TEAM_GAP:
                    problems.append(f"{name}: {trainer} has a Lv{low} Pokémon next to a Lv{top} one")
        report.append(f"| {boss} | {cap} | {min(tops)} | {max(tops)} | {len(tops)} |")
    report.append("")

    fights = rematches(parties)
    report += ["## Phone rematches", "", "A rematch must be below the next boss's ace at the point it unlocks.", "",
               "| Unlocked by | Next boss | Ace | Highest | Fights |", "|---|---|---|---|---|"]
    for gate, boss, cap in GATES:
        rows = [(n, max(m[0] for m in parties[(c, n)])) for _, c, n, g in fights if g == gate]
        if not rows:
            continue
        top = max(r[1] for r in rows)
        report.append(f"| `{gate}` | {boss} | {cap} | {top} | {len(rows)} |")
        for trainer, level in rows:
            if level >= cap:
                problems.append(f"Rematch {trainer} has Lv{level} at {gate}, not below {boss} ({cap})")
    for _, cls, trainer, _ in fights:
        levels = [m[0] for m in parties[(cls, trainer)]]
        message = f"Rematch {trainer} has a Lv{min(levels)} Pokémon next to a Lv{max(levels)} one"
        if max(levels) - min(levels) > MAX_TEAM_GAP and message not in problems:
            problems.append(message)
    report.append("")

    # Each trainer's fights must not get weaker as the story goes on.
    by_trainer = {}
    for name, cls, trainer, gate in fights:
        by_trainer.setdefault((name, cls, re.sub(r"\d+$", "", trainer)), []).append((GATE_ORDER.get(gate, -1), trainer))
    for (name, cls, base), rows in sorted(by_trainer.items()):
        levels = [(order, trainer, max(m[0] for m in parties[(cls, trainer)])) for order, trainer in sorted(set(rows))]
        for a, b in zip(levels, levels[1:]):
            if b[2] < a[2]:
                problems.append(f"{name}: {base} drops from Lv{a[2]} ({a[1]}) to Lv{b[2]} ({b[1]})")

    # Every trainer on a map must belong to an area.
    assigned = {m for _, _, maps in AREAS for m in maps}
    for path in sorted(glob.glob("maps/*.asm")):
        name = os.path.basename(path)[:-4]
        if name in assigned or name == "TrainerHouseB1F":
            continue
        fights_here = re.findall(r"^\s*(?:trainer|loadtrainer)\s+(\w+),\s*(\w+)", open(path, encoding="utf8").read(), re.M)
        if any(c not in BOSSES and (c, n) in parties for c, n in fights_here):
            problems.append(f"{name} has regular trainers but no story area in this audit")

    report += ["## Result", ""]
    report += [f"- {p}" for p in problems] if problems else ["All checks pass."]
    report.append("")
    with open("TRAINER_LEVELS_AUDIT.md", "w", encoding="utf8", newline="\n") as f:
        f.write("\n".join(report))
    print("\n".join(problems) if problems else "All checks pass.")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
