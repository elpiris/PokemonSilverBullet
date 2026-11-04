#!/usr/bin/env python3
"""Generate AVAILABILITY_AUDIT.md: how and when each Pokémon can be obtained in Silver.

Run from the repository root: python tools/audit_availability.py

Sources read from the repo: wild, swarm, fishing, headbutt, Rock Smash and contest data,
evolutions, breeding data, gifts, static encounters and NPC trades. The story stage of each
map and item is set by hand in the tables below, so those stages are approximate.
"""
import re

STAGES = ["Before Falkner", "Before Bugsy", "Before Whitney", "Before Morty", "Before Pryce",
          "Before Clair", "Before Elite Four", "Kanto", "After Kanto"]
FALKNER, BUGSY, WHITNEY, MORTY, PRYCE, CLAIR, LEAGUE, KANTO, LATE = range(9)

MAP_STAGE = {
    **dict.fromkeys(["NEW_BARK_TOWN", "CHERRYGROVE_CITY", "VIOLET_CITY", "ROUTE_29", "ROUTE_30", "ROUTE_31",
                     "ROUTE_46", "DARK_CAVE_VIOLET_ENTRANCE", "SPROUT_TOWER_2F", "SPROUT_TOWER_3F"], FALKNER),
    **dict.fromkeys(["ROUTE_32", "ROUTE_33", "RUINS_OF_ALPH_OUTSIDE", "RUINS_OF_ALPH_INNER_CHAMBER",
                     "UNION_CAVE_1F", "SLOWPOKE_WELL_B1F"], BUGSY),
    **dict.fromkeys(["ILEX_FOREST", "ROUTE_34", "ROUTE_35", "NATIONAL_PARK"], WHITNEY),
    **dict.fromkeys(["ROUTE_36", "ROUTE_37", "ECRUTEAK_CITY", "BURNED_TOWER_1F", "BURNED_TOWER_B1F"], MORTY),
    **dict.fromkeys(["ROUTE_38", "ROUTE_39", "OLIVINE_CITY", "OLIVINE_PORT", "ROUTE_40", "ROUTE_41", "CIANWOOD_CITY",
                     "ROUTE_42", "ROUTE_43", "ROUTE_44", "LAKE_OF_RAGE", "MOUNT_MORTAR_1F_OUTSIDE",
                     "MOUNT_MORTAR_1F_INSIDE", "MOUNT_MORTAR_2F_INSIDE", "MOUNT_MORTAR_B1F",
                     "UNION_CAVE_B1F", "UNION_CAVE_B2F", "SLOWPOKE_WELL_B2F"], PRYCE),
    **dict.fromkeys(["ICE_PATH_1F", "ICE_PATH_B1F", "ICE_PATH_B2F_BLACKTHORN_SIDE", "ICE_PATH_B2F_MAHOGANY_SIDE",
                     "ICE_PATH_B3F", "BLACKTHORN_CITY", "DRAGONS_DEN_B1F", "DARK_CAVE_BLACKTHORN_ENTRANCE",
                     "ROUTE_45", "WHIRL_ISLAND_NW", "WHIRL_ISLAND_NE", "WHIRL_ISLAND_SW", "WHIRL_ISLAND_SE",
                     "WHIRL_ISLAND_CAVE", "WHIRL_ISLAND_B1F", "WHIRL_ISLAND_B2F", "WHIRL_ISLAND_LUGIA_CHAMBER"], CLAIR),
    **dict.fromkeys(["ROUTE_26", "ROUTE_27", "TOHJO_FALLS", "VICTORY_ROAD"], LEAGUE),
    **dict.fromkeys(["ROUTE_28", "SILVER_CAVE_OUTSIDE", "SILVER_CAVE_ROOM_1", "SILVER_CAVE_ROOM_2", "SILVER_CAVE_ROOM_3",
                     "SILVER_CAVE_ITEM_ROOMS", "TIN_TOWER_2F", "TIN_TOWER_3F", "TIN_TOWER_4F", "TIN_TOWER_5F",
                     "TIN_TOWER_6F", "TIN_TOWER_7F", "TIN_TOWER_8F", "TIN_TOWER_9F"], LATE),
}
SURF_STAGE = PRYCE
OLD_ROD, GOOD_ROD, SUPER_ROD = BUGSY, PRYCE, KANTO
HEADBUTT_STAGE = WHITNEY
ROCK_SMASH_STAGE = MORTY
CONTEST_STAGE = WHITNEY
DAYCARE_STAGE = WHITNEY
ITEM_STAGE = {"MOON_STONE": PRYCE, "FIRE_STONE": MORTY, "WATER_STONE": PRYCE, "THUNDERSTONE": PRYCE,
              "LEAF_STONE": WHITNEY, "SUN_STONE": WHITNEY}
KINGS_ROCK_STAGE = PRYCE

# (species, stage, kind, where). A starter is one choice out of three.
SINGLE_SOURCES = [
    ("CYNDAQUIL", FALKNER, "Starter", "Elm's Lab"), ("TOTODILE", FALKNER, "Starter", "Elm's Lab"),
    ("CHIKORITA", FALKNER, "Starter", "Elm's Lab"), ("SPEAROW", WHITNEY, "Gift", "Route 35 gate"),
    ("TOGEPI", BUGSY, "Gift", "Mystery Egg"), ("EEVEE", WHITNEY, "Gift", "Bill's family"),
    ("TYROGUE", CLAIR, "Gift", "Kiyo, Mt. Mortar"), ("SUDOWOODO", MORTY, "Static", "Route 36"),
    ("GYARADOS", PRYCE, "Static", "Lake of Rage"), ("LAPRAS", PRYCE, "Static", "Union Cave, Fridays"),
    ("ELECTRODE", PRYCE, "Static", "Rocket Hideout"), ("VOLTORB", PRYCE, "Static", "Rocket Hideout"),
    ("GEODUDE", PRYCE, "Static", "Rocket Hideout"), ("KOFFING", PRYCE, "Static", "Rocket Hideout"),
    ("LUGIA", CLAIR, "Static", "Whirl Islands"), ("HO_OH", LATE, "Static", "Tin Tower"),
    ("SNORLAX", KANTO, "Static", "Vermilion"), ("RAIKOU", MORTY, "Roamer", "Johto"),
    ("ENTEI", MORTY, "Roamer", "Johto"), ("SUICUNE", MORTY, "Roamer", "Johto"),
]
# Prizes can be bought repeatedly, so they aren't one-time.
PRIZES = [("ABRA", WHITNEY, "Goldenrod Game Corner"), ("SANDSHREW", WHITNEY, "Goldenrod Game Corner"),
          ("DRATINI", WHITNEY, "Goldenrod Game Corner"), ("MR__MIME", KANTO, "Celadon Game Corner"),
          ("EEVEE", KANTO, "Celadon Game Corner"), ("PORYGON", KANTO, "Celadon Game Corner")]
NPC_TRADE_STAGE = {"DROWZEE": WHITNEY, "BELLSPROUT": FALKNER, "KRABBY": PRYCE,
                   "DRAGONAIR": CLAIR, "GLOOM": KANTO, "CHANSEY": KANTO}
GRASS_SLOTS = [30, 30, 20, 10, 5, 4, 1]
WATER_SLOTS = [60, 30, 10]


def read_lines(path):
    with open(path, encoding="utf8") as f:
        return f.read().split("\n")


def silver_lines(path):
    """Yield the lines Silver assembles, skipping IF DEF(_GOLD) blocks."""
    skipping = False
    for line in read_lines(path):
        stripped = line.strip()
        if stripped.startswith("IF DEF(_GOLD)"):
            skipping = True
        elif stripped.startswith(("ELIF DEF(_SILVER)", "ENDC")):
            skipping = False
        elif not skipping:
            yield stripped


def load_species():
    species = []
    for line in read_lines("constants/pokemon_constants.asm"):
        match = re.match(r"\s*const (\w+)", line)
        if match:
            species.append(match.group(1))
            if match.group(1) == "CELEBI":
                break
    assert len(species) == 251, len(species)
    return species


def load_evolutions(species):
    """Return [(from, to, method, argument)]."""
    evos = []
    index = -1
    in_evos = False
    for line in read_lines("data/pokemon/evos_attacks.asm"):
        if re.match(r"\w+EvosAttacks:", line):
            index += 1
            in_evos = True
        elif in_evos:
            stripped = line.split(";")[0].strip()
            if stripped == "db 0":
                in_evos = False
            elif stripped.startswith("db EVOLVE_"):
                parts = [p.strip() for p in stripped[3:].split(",")]
                evos.append((species[index], parts[-1], parts[0], parts[1]))
    assert index == 250, index
    return evos


def load_breeding(species):
    """Return {species: (gender ratio, has an egg group)}."""
    data = {}
    for mon in species:
        name = mon.lower()
        if mon == "MR__MIME":
            name = "mr__mime"
        path = f"data/pokemon/base_stats/{name}.asm"
        text = "\n".join(read_lines(path))
        gender = re.search(r"db (GENDER_\w+) ; gender", text).group(1)
        groups = re.search(r"dn (EGG_\w+), (EGG_\w+)", text).groups()
        data[mon] = (gender, "EGG_NONE" not in groups)
    return data


def wild_tables(path, sources, kind, slots, base_stage, swarm=False):
    current = None
    rates = None
    slot = 0

    def flush():
        if current:
            for mon, rate in rates.items():
                sources.setdefault(mon, []).append(
                    (max(MAP_STAGE[current], base_stage), kind + (" swarm" if swarm else ""), current, rate, True))

    per_time = len(slots)
    tally = {}
    for line in silver_lines(path):
        match = re.match(r"def_(?:grass|water)_wildmons (\w+)", line)
        if match:
            flush()
            current, rates, slot, tally = match.group(1), {}, 0, {}
            continue
        match = re.match(r"db\s+(\d+), (\w+)$", line)
        if match and current:
            time = slot // per_time
            key = (time, match.group(2))
            tally[key] = tally.get(key, 0) + slots[slot % per_time]
            rates[match.group(2)] = max(rates.get(match.group(2), 0), tally[key])
            slot += 1
    flush()


def tree_tables(sources):
    set_maps = {}
    for line in read_lines("data/wild/treemon_maps.asm"):
        match = re.match(r"\s*treemon_map (\w+),\s*(TREEMON_SET_\w+)", line)
        if match and match.group(1) in MAP_STAGE:
            set_maps.setdefault(match.group(2), []).append(match.group(1))
    labels = {"TreeMonSet_Forest": "TREEMON_SET_FOREST", "TreeMonSet_Canyon": "TREEMON_SET_CANYON",
              "TreeMonSet_Rock": None}
    active = None
    tally = {}
    for line in silver_lines("data/wild/treemons.asm"):
        match = re.match(r"(TreeMonSet_\w+):", line)
        if match:
            active = match.group(1) if match.group(1) in labels else None
            tally = {}
            continue
        match = re.match(r"db\s+(\d+), (\w+),\s*\d+", line)
        if match and active:
            tally[match.group(2)] = tally.get(match.group(2), 0) + int(match.group(1))
            if labels[active] is None:
                sources.setdefault(match.group(2), []).append(
                    (ROCK_SMASH_STAGE, "Rock Smash", "breakable rocks", tally[match.group(2)], True))
            else:
                maps = set_maps.get(labels[active], [])
                if maps:
                    best = min(maps, key=MAP_STAGE.get)
                    sources.setdefault(match.group(2), []).append(
                        (max(MAP_STAGE[best], HEADBUTT_STAGE), "Headbutt", best, tally[match.group(2)], True))
        elif line == "db -1":
            tally = {}


def fish_tables(sources):
    constants = [m.group(1) for line in read_lines("constants/map_data_constants.asm")
                 for m in [re.match(r"\s*const (FISHGROUP_\w+)", line)] if m]
    constants = [c for c in constants if c != "FISHGROUP_NONE"]
    group_maps = {}
    for line in read_lines("data/maps/maps.asm"):
        match = re.match(r"\s*map (\w+),.*(FISHGROUP_\w+)", line)
        if match:
            name = re.sub(r"(?<=[a-z0-9])(?=[A-Z])|(?<=[a-z])(?=[0-9])", "_", match.group(1)).upper()
            if name in MAP_STAGE:
                group_maps.setdefault(match.group(2), []).append(name)
    lines = list(silver_lines("data/wild/fish.asm"))
    labels = [m.group(1) for line in lines for m in [re.match(r"fishgroup .*?\.(\w+)_Old,", line)] if m]
    assert len(labels) == len(constants), (labels, constants)
    time_groups = []
    for line in lines[lines.index("TimeFishGroups:") + 1:]:
        match = re.match(r"db (\w+),\s*\d+,\s*(\w+),\s*\d+", line)
        if match:
            time_groups.append((match.group(1), match.group(2)))
    rods = {"Old": OLD_ROD, "Good": GOOD_ROD, "Super": SUPER_ROD}
    group = rod = None
    previous = 0
    for line in lines:
        match = re.match(r"\.(\w+)_(Old|Good|Super):", line)
        if match:
            group, rod = match.groups()
            previous = 0
            continue
        match = re.match(r"db\s+(\d+) percent(?: \+ 1)?,\s*(.+)", line)
        if match and group:
            chance = int(match.group(1))
            rate = chance - previous
            previous = chance
            body = match.group(2)
            timed = re.match(r"time_group (\d+)", body)
            mons = set(time_groups[int(timed.group(1))]) if timed else {body.split(",")[0].strip()}
            maps = group_maps.get(constants[labels.index(group)], [])
            if not maps:
                continue
            best = min(maps, key=MAP_STAGE.get)
            kind = "Fish swarm" if "_Swarm" in group else "Fish"
            for mon in mons:
                sources.setdefault(mon, []).append(
                    (max(MAP_STAGE[best], rods[rod]), f"{kind} ({rod} Rod)", best, rate, True))


def contest_table(sources):
    for line in silver_lines("data/wild/bug_contest_mons.asm"):
        match = re.match(r"db\s+(\d+), (\w+),", line)
        if match:
            sources.setdefault(match.group(2), []).append(
                (CONTEST_STAGE, "Bug Contest", "National Park", int(match.group(1)), True))


def kanto_stage(name):
    return MAP_STAGE.setdefault(name, KANTO)


def main():
    species = load_species()
    evos = load_evolutions(species)
    breeding = load_breeding(species)
    for path in ("data/wild/kanto_grass.asm", "data/wild/kanto_water.asm"):
        for line in read_lines(path):
            match = re.match(r"\s*def_(?:grass|water)_wildmons (\w+)", line)
            if match:
                kanto_stage(match.group(1))

    sources = {}
    wild_tables("data/wild/johto_grass.asm", sources, "Grass", GRASS_SLOTS, 0)
    wild_tables("data/wild/kanto_grass.asm", sources, "Grass", GRASS_SLOTS, 0)
    wild_tables("data/wild/johto_water.asm", sources, "Surf", WATER_SLOTS, SURF_STAGE)
    wild_tables("data/wild/kanto_water.asm", sources, "Surf", WATER_SLOTS, SURF_STAGE)
    wild_tables("data/wild/swarm_grass.asm", sources, "Grass", GRASS_SLOTS, 0, swarm=True)
    wild_tables("data/wild/swarm_water.asm", sources, "Surf", WATER_SLOTS, SURF_STAGE, swarm=True)
    tree_tables(sources)
    fish_tables(sources)
    contest_table(sources)
    for mon, stage, where in PRIZES:
        sources.setdefault(mon, []).append((stage, "Prize", where, None, True))
    for mon, stage, kind, where in SINGLE_SOURCES:
        sources.setdefault(mon, []).append((stage, kind, where, None, False))

    # Unused species names in data files (time groups can repeat) are filtered here.
    direct = {mon: sources[mon] for mon in species if mon in sources}

    stage = {mon: min(s[0] for s in srcs) for mon, srcs in direct.items()}
    how = {mon: min(srcs, key=lambda s: (s[0], not s[4], -(s[3] or 0)))[1] for mon, srcs in direct.items()}
    repeatable = {mon: any(s[4] and "Starter" not in s[1] for s in srcs) for mon, srcs in direct.items()}
    # Starters: only one of three can be taken, so they get no credit for being repeatable.

    prevo = {b: a for a, b, _, _ in evos}

    def root(mon):
        while mon in prevo:
            mon = prevo[mon]
        return mon

    def improve(mon, new_stage, text, new_repeat):
        changed = False
        if mon not in stage or new_stage < stage[mon]:
            stage[mon], how[mon] = new_stage, text
            changed = True
        if new_repeat and not repeatable.get(mon):
            repeatable[mon] = True
            changed = True
        return changed

    trades = [("DROWZEE", "MACHOP"), ("BELLSPROUT", "ONIX"), ("KRABBY", "VOLTORB"),
              ("DRAGONAIR", "RHYDON"), ("GLOOM", "RAPIDASH"), ("CHANSEY", "AERODACTYL")]
    changed = True
    while changed:
        changed = False
        for a, b, method, arg in evos:
            if a not in stage:
                continue
            need = stage[a]
            if method == "EVOLVE_ITEM":
                need = max(need, ITEM_STAGE[arg])
            elif method == "EVOLVE_KINGS_ROCK":
                need = max(need, KINGS_ROCK_STAGE)
            changed |= improve(b, need, f"Evolve {a}", repeatable.get(a, False))
        for give, get in trades:
            if give in stage:
                changed |= improve(get, max(stage[give], NPC_TRADE_STAGE[give]), f"Trade {give}", False)
        for mon in species:
            gender, can = breeding[mon]
            if mon not in stage or not can or mon == "DITTO":
                continue
            need = max(stage[mon], DAYCARE_STAGE)
            has_both = gender not in ("GENDER_UNKNOWN", "GENDER_F0", "GENDER_F100")
            if not has_both or not repeatable.get(mon):
                # Needs Ditto, except that a one-time Pokémon can still pair with Ditto.
                if "DITTO" not in stage:
                    continue
                need = max(need, stage["DITTO"])
            changed |= improve(root(mon), need, f"Breed {mon}", True)

    # The best rate at the first stage it can be found in the wild, ignoring swarms.
    best_rate = {}
    for mon, srcs in direct.items():
        rates = [s for s in srcs if s[3] is not None and "swarm" not in s[1]]
        if rates:
            first = min(s[0] for s in rates)
            top = max((s for s in rates if s[0] == first), key=lambda s: s[3])
            best_rate[mon] = (top[3], top[1], top[2], STAGES[first])

    rows = []
    for number, mon in enumerate(species, 1):
        if mon not in stage:
            rows.append((number, mon, None, "Not obtainable", None, False))
        else:
            rows.append((number, mon, stage[mon], how[mon], best_rate.get(mon), repeatable.get(mon, False)))

    missing = [r for r in rows if r[2] is None]
    one_time = [r for r in rows if r[2] is not None and not r[5]]
    swarm_only = [mon for mon, srcs in direct.items()
                  if all("swarm" in s[1] for s in srcs) and not how[mon].startswith(("Evolve", "Breed"))]

    out = ["# Availability audit", "",
           "How each Pokémon can be obtained on one Silver cartridge. Generated by `tools/audit_availability.py`.", "",
           "- **Earliest:** the first story stage it can be obtained, ignoring the level needed to evolve. Stages are set by hand and approximate.",
           "- **How:** the source for that earliest stage.",
           "- **First regular wild source:** the first stage it appears outside swarms, with its best rate there for one time of day.",
           "- **Repeatable:** yes if more than one can be obtained, by catching, buying, or breeding.",
           "- **Starters:** one is chosen at the start. After the league, Elm gives the one nobody took, and the rival gives an Egg of the stolen one.", "",
           f"Obtainable: {251 - len(missing)} of 251. One-time only: {len(one_time)}.", "",
           "## Not obtainable", "", ", ".join(r[1] for r in missing) or "None", "",
           "## One-time only", "", ", ".join(f"{r[1]} ({r[3]})" for r in one_time) or "None", "",
           "## Swarm only (as a direct wild source)", "", ", ".join(swarm_only) or "None", ""]
    for title, low, high in (("Gen 2", 151, 251), ("Gen 1", 0, 151)):
        out += [f"## {title}", "", "| Dex | Pokémon | Earliest | How | First regular wild source | Repeatable |",
                "|---|---|---|---|---|---|"]
        for number, mon, st, text, rate, rep in rows[low:high]:
            label = STAGES[st] if st is not None else "-"
            rate_text = f"{rate[3]}: {rate[0]}%, {rate[1]}, {rate[2]}" if rate else "-"
            out.append(f"| {number} | {mon} | {label} | {text} | {rate_text} | {'Yes' if rep else 'No'} |")
        out.append("")
    with open("AVAILABILITY_AUDIT.md", "w", encoding="utf8", newline="\n") as f:
        f.write("\n".join(out))
    print(f"Obtainable {251 - len(missing)}; missing {len(missing)}; one-time {len(one_time)}")


if __name__ == "__main__":
    main()
