# Pokémon Silver Bullet

A balance hack of Pokémon Silver that keeps the original game's feel and fixes its best-known flaws: trade-only evolutions, an uneven level curve, and Pokémon you can't catch on one cartridge. The goal is a challenge that climbs steadily from the first gym to the final battle against Red, with every Pokémon obtainable on one cartridge.

It's built on [pret/pokegold](https://github.com/pret/pokegold), a disassembly of Pokémon Gold and Silver. Gen 2's type-based physical/special split stays as it was.

No ROMs are included. You build one yourself from this source.

## What's changed

These are the main changes. [BALANCE_NOTES.md](BALANCE_NOTES.md) has every change and the reason for it.

### Balance

- **No trade evolutions:** every trade evolution now happens by level, such as Alakazam at Lv36, Gengar at Lv38, and Steelix at Lv40. Slowpoke becomes Slowking at Lv37 if it holds a King's Rock, and Slowbro otherwise, so the choice stays with the player.
- **Boss teams:** every boss has a rebuilt team. Teams grow from 3 Pokémon at the first gym to 6 at the end, with better moves and coverage for the types that counter them. A few moves are ones the species can't normally learn, used on purpose. Lt. Surge's Raichu has Surf, for example.
- **Regular trainers:** their Pokémon now evolve to fit their levels, and hand-written movesets were refreshed. Kanto gym trainers have at least 3 Pokémon each.
- **Weak Pokémon:** a small group of outrageously weak Pokémon get better stats and level-up moves, and a clearer identity. They stay weak, but usable.
  - **Stats and moves:** Sneasel, Dunsparce, Ledian, Delibird, Yanma, Aipom, Ariados, Togetic, Farfetch'd, Lickitung, and Beedrill.
  - **Stats only:** Corsola.
  - **Moves only:** Murkrow, Politoed, Ninetales, Wigglytuff, and Arbok.

Gen 2's type-based physical/special split is unchanged.

### Level curve

The challenge climbs steadily from the first gym to Red. Kanto leaders can be fought in any order, so they share a narrow range.

| Boss | Levels | Pokémon |
|---|---|---|
| Falkner | 8-10 | 3 |
| Bugsy | 14-17 | 3 |
| Whitney | 17-20 | 3 |
| Morty | 23-26 | 4 |
| Chuck | 30-32 | 4 |
| Jasmine | 32-34 | 4 |
| Pryce | 33-36 | 4 |
| Clair | 38-41 | 5 |
| Will | 42-44 | 5 |
| Koga | 42-46 | 5 |
| Bruno | 44-48 | 5 |
| Karen | 45-50 | 5 |
| Lance | 47-52 | 6 |
| Janine | 50-54 | 6 |
| Brock, Lt. Surge | 51-54 | 6 |
| Erika | 52-55 | 6 |
| Misty, Sabrina | 53-56 | 6 |
| Blaine | 55-58 | 6 |
| Blue | 61-64 | 6 |
| Red | 73-81 | 6 |

The rival's strongest Pokémon goes 5, 16, 23, 37, 42, then 53 at Mt. Moon and 60 at Indigo Plateau. Rocket executives top out at 30 in the Hideout and 39 in the Radio Tower.

- **Regular trainers:** raised by area, and always below the next boss's ace. Phone rematches follow the same rule. `python tools/audit_trainers.py` checks this.
- **Kanto gym trainers:** 3 to 5 levels below their leader's lowest Pokémon.
- **Wild Pokémon:** raised where they sat far below the local trainers, mostly in Kanto, while staying well under those trainers. Wild slots evolve by level, except Magikarp.
- **Red:** keeps his original levels as the ultimate boss.

### Pokémon availability

All 251 Pokémon can be obtained on one save, with no trading. `python tools/audit_availability.py` checks this.

- **Gold-only Pokémon:** they now appear in Silver, in the places Gold has them.
- **Rare and late Pokémon:** they're easier to find, and many arrive earlier in Johto. Examples are Yanma, Skarmory, Sneasel, Larvitar, and Chansey.
- **Evolution stones:** they're pickups around the world, and Celadon Dept. Store sells all six late on.
- **Johto starters:** after the league, Elm gives you the one left on his table, and the rival gives you an Egg of the one they stole, after a battle.
- **Kanto starters:** Prof. Oak gives Bulbasaur on your first visit, Charmander at 12 badges, and Squirtle at 16.
- **Fossils:** solving the Kabuto and Omanyte puzzles in the Ruins of Alph earns the matching Pokémon.
- **Legendary birds:** Lv50 one-time encounters. Zapdos is in Rock Tunnel, Articuno is in Mt. Moon, and Moltres is in Victory Road after the league.
- **Mewtwo:** a Lv70 one-time encounter deep in Silver Cave.
- **Celebi:** a Lv60 encounter at the Ilex Forest shrine, for a trainer with all 16 badges.
- **Mew:** a Lv30 encounter in the Ruins of Alph, as the reward for catching all 26 Unown. A scientist tells you where to go.

### Battle AI

Bosses and Cooltrainers now favor super effective moves and avoid resisted ones when they have another attack type. Before, they could pick a status move over a super effective hit. Other trainer classes are unchanged, so early trainers stay simple.

## Status

The planned changes are finished, and playtesting has just started. Most of this hasn't been played yet, so expect rough edges. Smaller adjustments from playtesting are collected in [TODO.md](TODO.md) and made in batches.

## Building

Follow [INSTALL.md](INSTALL.md) to set up RGBDS, then run:

```bash
make silver
```

This produces `pokesilver.gbc`. Only the Silver build has been checked. The hashes in `roms.sha1` are for the unmodified games, so they won't match this hack.

## Credits

The disassembly is the work of the [pret](https://pret.github.io/) team and contributors.

This is an unofficial fan project, not affiliated with or endorsed by Nintendo, Game Freak, or The Pokémon Company.
