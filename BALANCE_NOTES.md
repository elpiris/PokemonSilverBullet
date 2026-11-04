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

## Difficulty: Johto gym leaders

Goal: an even climb with no plateaus. Chuck, Jasmine, and the Rocket Hideout can come in any order, and
Pryce's gym only opens after the Hideout, so those three leaders stay close together.

| Leader | Vanilla ace | New ace | Main changes and reason |
|---|---|---|---|
| Falkner | 9 | 10 | Adds Spearow, a real attacker, as a third Pokémon |
| Bugsy | 16 | 17 | Metapod and Kakuna become Butterfree and Beedrill, since both evolve at Lv10. Scyther gains Pursuit |
| Whitney | 20 | 20 | Adds Snubbull so the fight is less centered on Miltank. Attract → Growl removes the luck that made Rollout unfair. Clefairy: Mimic → Sing |
| Morty | 25 | 26 | Misdreavus replaces Gastly. Lick replaces Mimic on Haunter. Gengar moves to the last slot |
| Chuck | 30 | 32 | Grows from 2 to 4 Pokémon with Machoke and Hitmontop. Primeape: Rage → Low Kick |
| Jasmine | 35 | 34 | Magnemites become Magneton and Skarmory, plus Forretress. Steelix: Sunny Day → Bind. Skarmory's Steel Wing is above its level on purpose |
| Pryce | 31 | 36 | Dewgong, Cloyster, Jynx, Piloswine, so he's clearly above Jasmine. Piloswine: Mist → Take Down. Cloyster's Spike Cannon is above its level on purpose |
| Clair | 40 | 41 | Adds Gyarados as a fifth Pokémon, since she's the last leader |

Leader aces may be evolved below the player's evolution level (Morty's Gengar, Jasmine's Steelix, Clair's Kingdra).

## Difficulty: Johto rival fights and Rocket executives

The Cherrygrove and Azalea rival fights are unchanged. The rest now climb with the story.

| Fight | Vanilla ace | New ace | Main changes and reason |
|---|---|---|---|
| Rival, Burned Tower | 22 | 23 | Zubat → Golbat. Haunter: Spite → Night Shade. Bayleef: Growl → Synthesis |
| Rocket Hideout, male executive | 24 | 30 | Levels only, and Zubat → Golbat. They were below leaders you may already have beaten |
| Rocket Hideout, female executive | 25 | 30 | Levels only |
| Radio Tower, Fake Director | 32 | 36 | Levels only, keeping the Koffing wall |
| Rival, Goldenrod | 32 | 37 | Magnemite → Magneton, Quilava → Typhlosion. Better moves on most of the team |
| Radio Tower, male executive | 36 | 38 | Levels only |
| Radio Tower, female executive | 32 | 38 | Levels only |
| Radio Tower, Rocket boss | 35 | 39 | Houndour → Houndoom and Koffing → Weezing, as both are past their evolution levels |
| Rival, Victory Road | 38 | 42 | Haunter → Gengar, Kadabra → Alakazam, following the new evolution levels. Starters get Giga Drain, Flamethrower, or Surf so they feel like aces |
