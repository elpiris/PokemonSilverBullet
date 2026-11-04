#!/usr/bin/env python3
"""Generate BASE_STATS_AUDIT.md from the base stats, evolution, and wild data.

Usage: python tools/audit_stats.py  (run from the repository root)

Wild levels describe Silver: IF DEF(_GOLD) blocks are skipped. Gift and static
encounters (starters, Eevee, legendaries, etc.) are not wild data, so they show "-".
"""

import glob
import re
from statistics import median

STATS = ["hp", "atk", "def", "spd", "sat", "sdf"]
SPECIAL_TYPES = {"FIRE", "WATER", "GRASS", "ELECTRIC", "PSYCHIC_TYPE", "ICE", "DRAGON", "DARK"}
LEGENDARIES = {
    "ARTICUNO", "ZAPDOS", "MOLTRES", "MEWTWO", "MEW",
    "RAIKOU", "ENTEI", "SUICUNE", "LUGIA", "HO_OH", "CELEBI",
}
NAME_OVERRIDES = {
    "NIDORAN_F": "Nidoran F", "NIDORAN_M": "Nidoran M", "FARFETCH_D": "Farfetch'd",
    "MR__MIME": "Mr. Mime", "HO_OH": "Ho-Oh",
}
# A STAB-mismatch flag needs the unused offensive stat to lead by at least this much
MISMATCH_MARGIN = 20
JOHTO_WILD_FILES = ["johto_grass", "johto_water", "swarm_grass", "swarm_water",
                    "bug_contest_mons", "treemons", "fish"]
KANTO_WILD_FILES = ["kanto_grass", "kanto_water"]


def read_lines(path):
    with open(path, encoding="utf-8") as f:
        return [line.split(";")[0].rstrip() for line in f]


def load_mons():
    mons = []
    for path in glob.glob("data/pokemon/base_stats/*.asm"):
        with open(path, encoding="utf-8") as f:
            text = f.read()
        const, dex = re.search(r"db (\w+) ; (\d+)", text).groups()
        values = re.search(r"db\s+(\d+),\s*(\d+),\s*(\d+),\s*(\d+),\s*(\d+),\s*(\d+)\n", text).groups()
        types = re.search(r"db (\w+), (\w+) ; type", text).groups()
        mon = {"const": const, "dex": int(dex), "types": sorted(set(types), key=types.index)}
        mon.update(zip(STATS, map(int, values)))
        mon["bst"] = sum(mon[s] for s in STATS)
        mons.append(mon)
    return sorted(mons, key=lambda m: m["dex"])


def load_evolutions():
    """Return {species: [evolved species]} keyed by dex order of the labels."""
    evos, order, current, in_evos = {}, [], None, False
    for line in read_lines("data/pokemon/evos_attacks.asm"):
        label = re.match(r"(\w+)EvosAttacks:", line)
        if label:
            current = label.group(1)
            order.append(current)
            evos[current] = []
            in_evos = True
        elif in_evos:
            if re.match(r"\s*db 0$", line):
                in_evos = False
            else:
                evo = re.match(r"\s*db EVOLVE_\w+,.*,\s*(\w+)$", line)
                if evo:
                    evos[current].append(evo.group(1))
    return [evos[name] for name in order]


def wild_levels(files, species):
    """Return {species: lowest wild level} for Silver across the given data files."""
    lowest = {}
    # "db level, MON", "db chance, MON, level[, max]", "db chance percent, MON, level", or "db MON, level, ..."
    pattern = re.compile(r"(?:db\s+(\d+),\s*(\w+)(?:,\s*(\d+))?)|(?:\b(\w+),\s*(\d+))")
    for name in files:
        skipping = False
        for line in read_lines(f"data/wild/{name}.asm"):
            stripped = line.strip()
            if stripped.startswith("IF DEF(_GOLD)"):
                skipping = True
            elif stripped.startswith(("ELIF DEF(_SILVER)", "ENDC")):
                skipping = False
            elif not skipping and stripped:
                for first, second, third, other, other_level in pattern.findall(stripped):
                    mon, level = (second, third or first) if second in species else (other, other_level)
                    if mon in species:
                        lowest[mon] = min(lowest.get(mon, 255), int(level))
    return lowest


def classify(mons, evo_lists):
    by_const = {m["const"]: m for m in mons}
    for mon, evos in zip(mons, evo_lists):
        mon["evos"] = evos
    has_prevo = {target for evos in evo_lists for target in evos}
    for mon in mons:
        if mon["const"] in LEGENDARIES:
            mon["stage"] = "Legendary"
        elif mon["evos"]:
            mon["stage"] = "Middle" if mon["const"] in has_prevo else "Basic"
        else:
            mon["stage"] = "Final" if mon["const"] in has_prevo else "Single"
    return by_const


def line_levels(mons, johto):
    """Return {species: lowest Johto wild level of it or any pre-evolution}."""
    prevo = {target: m["const"] for m in mons for target in m["evos"]}
    levels = {}
    for mon in mons:
        current, found = mon["const"], []
        while current:
            if current in johto:
                found.append(johto[current])
            current = prevo.get(current)
        if found:
            levels[mon["const"]] = min(found)
    return levels


def stab_mismatch(mon):
    """Name the unused offensive stat if every STAB type uses the weaker one."""
    categories = {"sat" if t in SPECIAL_TYPES else "atk" for t in mon["types"]}
    if len(categories) == 2:
        return ""
    used = categories.pop()
    unused = "atk" if used == "sat" else "sat"
    return unused if mon[unused] - mon[used] >= MISMATCH_MARGIN else ""


def name(mon):
    return NAME_OVERRIDES.get(mon["const"], mon["const"].title())


def row(mon, johto, kanto, line):
    stats = " | ".join(str(mon[s]) for s in STATS)
    types = "/".join(t.replace("_TYPE", "").title() for t in mon["types"])
    wild_j = johto.get(mon["const"], "-")
    wild_k = kanto.get(mon["const"], "-")
    wild_line = line.get(mon["const"], "-")
    flag = stab_mismatch(mon)
    return (f"| {mon['dex']:03} | {name(mon)} | {types} | {mon['stage']} | **{mon['bst']}** | {stats} "
            f"| {wild_j} | {wild_line} | {wild_k} | {flag} |")


HEADER = ("| # | Name | Type | Stage | BST | HP | Atk | Def | Spd | SpA | SpD "
          "| Johto Lv | Line Johto Lv | Kanto Lv | Off-type stat |\n"
          "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")


def main():
    mons = load_mons()
    assert len(mons) == 251
    classify(mons, load_evolutions())
    species = {m["const"] for m in mons}
    johto = wild_levels(JOHTO_WILD_FILES, species)
    kanto = wild_levels(KANTO_WILD_FILES, species)
    line = line_levels(mons, johto)

    out = ["# Base stats audit", "",
           "Generated by `tools/audit_stats.py`. Regenerate it after applying stat changes.", "",
           "- **Stage:** Basic and Middle evolve further, Final has a pre-evolution, "
           "Single never evolves, Legendary is listed by hand.",
           "- **Johto / Kanto Lv:** lowest wild level in Silver, including fishing, headbutt, "
           "swarms, and the Bug-Catching Contest under Johto. Gifts and static encounters are not counted.",
           "- **Line Johto Lv:** lowest Johto wild level of the Pokémon or any pre-evolution.",
           f"- **Off-type stat:** this offensive stat leads by {MISMATCH_MARGIN}+ but no STAB type uses it. "
           "Coverage moves may still use it, so read it as a prompt to check, not as a defect.",
           "", "## BST by stage", "",
           "| Stage | Count | Min | Median | Max |", "|---|---|---|---|---|"]
    stages = ["Basic", "Middle", "Final", "Single", "Legendary"]
    for stage in stages:
        bsts = [m["bst"] for m in mons if m["stage"] == stage]
        out.append(f"| {stage} | {len(bsts)} | {min(bsts)} | {median(bsts):g} | {max(bsts)} |")

    finished = [m for m in mons if m["stage"] in ("Final", "Single")]
    out += ["", "## Finished Pokémon, weakest first", "",
            "Final and Single stages together, since these are what a team ends up using.", "", HEADER]
    out += [row(m, johto, kanto, line) for m in sorted(finished, key=lambda m: (m["bst"], m["dex"]))]
    out += ["", "## All Pokémon in dex order", "", HEADER]
    out += [row(m, johto, kanto, line) for m in mons]

    with open("BASE_STATS_AUDIT.md", "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
