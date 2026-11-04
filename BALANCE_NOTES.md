# Balance notes

Every change from vanilla Pokémon Silver and the reason for it.

## Evolutions: no trade evolutions

Every trade evolution now happens by level, so the full Pokédex is reachable on one cartridge.

| Evolution | Vanilla | Now | Reason |
|---|---|---|---|
| Kadabra → Alakazam | Trade | Lv36 | Matches Charizard, Typhlosion, and Pidgeot |
| Machoke → Machamp | Trade | Lv40 | 12 levels after Machoke (Lv28), before Cross Chop at 43 |
| Graveler → Golem | Trade | Lv38 | 13 levels after Graveler (Lv25) |
| Haunter → Gengar | Trade | Lv38 | Same timing as Golem, since both lines first evolve at 25 |
| Seadra → Kingdra | Trade with Dragon Scale | Lv45 | 13 levels after Seadra (Lv32), late for 540 BST but before Dragonite (Lv55) |
| Onix → Steelix | Trade with Metal Coat | Lv40 | Onix is catchable at Lv6, so the jump from 385 to 510 BST comes late |
| Scyther → Scizor | Trade with Metal Coat | Lv30 | Scizor learns Metal Claw at 30, and both have 500 BST |
| Porygon → Porygon2 | Trade with Up-Grade | Lv30 | Porygon is only a Lv20 Celadon prize, so the wait is short |
| Poliwhirl → Politoed | Trade with King's Rock | Lv35 | Politoed learns Perish Song at 35. Water Stone → Poliwrath is unchanged |
| Slowpoke → Slowking | Trade with King's Rock | Lv37 holding King's Rock | Slowbro keeps Lv37 without the item, so the player chooses |

### Engine change for Slowking

Level and held item together had no existing evolution method, so this adds `EVOLVE_KINGS_ROCK`
(`db EVOLVE_KINGS_ROCK, level, species`), handled in `engine/pokemon/evolve.asm`. The entry must come
before Slowpoke's `EVOLVE_LEVEL` entry, because the first matching entry wins. It keeps the usual 3-byte
layout, so other code that reads evolution data needs no changes. The King's Rock is used up on
evolving, as in the vanilla trade, and is kept if the player cancels.

### Known side effects

- Up-Grade is expected to have no remaining use. The item and where it's found are unchanged.
- `EVOLVE_TRADE` is no longer used by any Pokémon, but the engine still supports it.
