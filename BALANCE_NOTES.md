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

## Difficulty: Elite Four and Lance

| Fight | Vanilla ace | New ace | Main changes and reason |
|---|---|---|---|
| Will | 42 | 44 | Girafarig replaces the first of two Xatu |
| Koga | 44 | 46 | Levels only, as his fight already works |
| Bruno | 46 | 48 | Onix → Steelix, past its new evolution level and a cover for Fighting's weaknesses |
| Karen | 47 | 50 | Gengar: Lick and Spite → Shadow Ball and Night Shade |
| Lance | 50 | 52 | Two Dragonite: Twister → DragonBreath |

## Difficulty: regular trainers

A quick pass, levels only: species and fixed movesets are unchanged, so some trainers now have Pokémon past their usual evolution level. Trainers are still below the next boss, but the gap is smaller. Each area gets a level bonus, and a cap keeps it under that boss. A level already above the cap stays as it is.

| Area | Bonus | Cap | Next boss ace |
|---|---|---|---|
| Routes 30 and 31 | +1 | | Falkner 10 |
| Sprout Tower | 1F and 2F +2, 3F +1 | 3F 9 | Falkner 10 |
| Violet Gym | none | | Falkner 10 |
| Route 32, Union Cave 1F, Route 33, Slowpoke Well | +2 | 12 to 16 | Bugsy 17 |
| Azalea Gym | +1 | 14 | Bugsy 17 |
| Route 34, Goldenrod Underground, Route 35, National Park | +3 | 15 to 19 | Whitney 20 |
| Goldenrod Gym | +1 | 19 | Whitney 20 |
| Routes 36 and 37, Dance Theater, Burned Tower | +5 | 22 | Morty 26 |
| Ecruteak Gym | +3 | 25 | Morty 26 |
| Routes 38 to 41, Olivine Lighthouse | +7 to +8 | 28 to 30 | Chuck 32, Jasmine 34 |
| Cianwood Gym | +3 | 30 | Chuck 32 |
| Routes 42 and 43 | +11 | 30 | Pryce 36 |
| Rocket Hideout | +5 | 29 | Executives 30 |
| Lake of Rage, Union Cave lower floors | +3 | 30 to 31 | Pryce 36 |
| Mahogany Gym | +6 | 34 | Pryce 36 |
| Radio Tower, Goldenrod Underground rooms | +10 | 35 to 36 | Executives 38, boss 39 |
| Routes 44 and 45 | +10 to +11 | 38 to 39 | Clair 41 |
| Blackthorn Gym | +1 | 38 | Clair 41 |
| Routes 26 and 27 | +6 | 42 | Will 44 |
| Kanto routes, Fast Ship | +10 | 45 to 48 | Kanto leaders |

Other cases:

- Phone rematches go up with their level: +2 up to Lv12, +4 up to Lv20, +6 up to Lv30, and +8 above that.
- The Route 34 Cooltrainers and Ruins of Alph trainers get +2, and Kiyo in Mt. Mortar gets +2.
- Unchanged: Route 46, the Kanto gyms (these stay with their leaders until the Kanto to-do), Trainer House, and unused parties.
- Until the Kanto leaders are done, some Kanto route trainers (up to Lv48) are above vanilla leaders such as Janine (39).

## Difficulty: battle AI

Bosses and Cooltrainers now also use `AI_TYPES`, the existing rule that favors super effective moves and avoids resisted ones when another attack type is available. They already avoided their weaker attacks, but their best attack only tied with their status moves, so they could pick a status move over a super effective hit.

This applies to all Johto and Kanto leaders, the Elite Four, Lance, Cal, the rival, Red, Blue, and both Cooltrainer classes. It's set in `data/trainers/attributes.asm`. Other classes are unchanged, so early trainers like Youngsters and Bug Catchers stay simple.

## Availability: all 251 on one save

Goal: every Pokémon can be obtained on one Silver save, using data changes wherever possible. Rare Pokémon can stay rarer than others. `tools/audit_availability.py` generates `AVAILABILITY_AUDIT.md`.

### Gold-only Pokémon

These use Gold's locations and levels, replacing common filler in Silver's tables. Ariados, Primeape, and Ursaring evolve by level from these. Arcanine needs a Fire Stone.

| Pokémon | Where | Replaces | Level | Chance |
|---|---|---|---|---|
| Spinarak | Route 30, night | Hoothoot | 3 | 30% |
| Spinarak | Route 31, night | Hoothoot | 4 | 30% |
| Spinarak | Route 37, night | Hoothoot | 13 | 30% |
| Growlithe | Route 37, all day | Vulpix | 14 | 10% |
| Growlithe | Route 37, daytime | Vulpix | 16 | 5% |
| Mankey | Route 42, all day | Mareep | 15 | 20% |
| Gligar | Route 45, all day | Graveler | 24 | 20% |
| Teddiursa | Route 45, night | Phanpy | 20 | 10% |
| Mantine | Route 41, surfing | Tentacool | 20 | 10% |

### Rare and late Pokémon

Chances that were too low go up, and Pokémon that arrived too late move into Johto. Swarms and the original locations still work.

| Pokémon | Where | Replaces | Level | Chance | Reason |
|---|---|---|---|---|---|
| Yanma | Route 35 | Pidgey, Hoothoot | 12 | 6% (was 1%) | Uncommon, without needing a swarm |
| Dunsparce | Dark Cave, Violet side | Zubat | 4 | 5% (was 1%) | Stays a rare find |
| Snubbull | Route 38 | Raticate | 16 | 31% (was 1%) | A normal catch for this route |
| Marill | Mt. Mortar, outside | Rattata | 14 | 11% (was 1%) | An option before Pryce |
| Miltank | Route 39 | Raticate | 15 | 35% (was 5%) | That route has few encounters, so it still takes some finding |
| Chansey | Routes 13, 14, 15 | Hoppip, Quagsire, Skiploom | 25 | 5% (was 1%) | Blissey depends on it |
| Skarmory | Route 42 | Flaaffy | 20 | 5% | Around gyms 5 and 6, where its typing isn't as oppressive. Route 45 keeps it |
| Murkrow | Route 38, night | Meowth | 16 | 10% | Was Kanto only |
| Slugma | Burned Tower 1F | Rattata | 15 | 20% | Fits the setting, and weak enough to be safe early |
| Misdreavus | Burned Tower B1F, night | Rattata | 15 | 10% | Was Mt. Silver only |
| Houndour | Route 44, night | Weepinbell | 22 | 5% | Evolves at 24, so late and rare keeps it in check |
| Sneasel | Ice Path, all floors, morning and night | Zubat | 22-24 | 5% | Was Mt. Silver only |
| Larvitar | Victory Road | Onix | 28 | 5% | Evolves at 30. Mt. Silver keeps it |
| Qwilfish | Good Rod on Route 32 and maps sharing its table | Tentacool | 20 | 10% of bites | Was Super Rod only |
| Remoraid | Good Rod on Route 44 and maps sharing its table | Poliwag | 20 | 10% of bites | Was Super Rod only |

## To do

Remaining work is tracked in [TODO.md](TODO.md).
