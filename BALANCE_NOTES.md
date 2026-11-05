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

### Evolution stones

Fire, Water, Thunder, and Leaf Stones only came from Bill's grandfather in Kanto, one of each. Stones are now pickups in fitting places, replacing items players rarely use, so exploring gets you evolutions early. Anyone who misses one can buy it late.

| Stone | Where | Replaces | Type |
|---|---|---|---|
| Leaf | Ilex Forest | Ether | Hidden |
| Leaf | Route 2 | Dire Hit | Item ball |
| Fire | Burned Tower 1F | X Speed | Item ball |
| Fire | Victory Road | X Special | Item ball |
| Water | Route 41 | Max Ether | Hidden |
| Water | Whirl Islands SW | Guard Spec | Item ball |
| Thunder | Rocket Hideout B1F | X Accuracy | Item ball |
| Thunder | Rock Tunnel 1F | X Defend | Hidden |
| Sun | Route 46 | Dire Hit | Item ball |
| Sun | Route 45 | X Special | Item ball |
| Moon | Mt. Mortar, outside | Guard Spec | Item ball |

Celadon Dept. Store 4F now sells all six stones for ¥2100 each. The Moon Stone's price changed from ¥0 to ¥2100 so it isn't free there, which also means it can now be sold. Existing sources, such as Bill's grandfather and Tohjo Falls, are unchanged. Event names in the map scripts still mention the old items, which doesn't show in-game.

### Johto starters

Only one starter was available, and breeding can't produce the others. Both now come from a short post-league story in New Bark Town. The script is in `maps/ElmsLab.asm` and `maps/NewBarkTown.asm`, using two new event flags.

| You chose | Rival stole | Elm gives (Lv5, holding a Berry) | Rival gives (Egg) |
|---|---|---|---|
| Cyndaquil | Totodile | Chikorita | Totodile |
| Totodile | Chikorita | Cyndaquil | Chikorita |
| Chikorita | Cyndaquil | Totodile | Cyndaquil |

- **Elm:** after you've collected the S.S. Ticket, talking to him gives you the starter left on his table. It's Lv5, the same as your first one. A full party means you come back later.
- **Rival:** Elm's gift brings the rival back to the lab window where you first met. They battle you with their Mt. Moon team, then hand over an Egg of the stolen starter. They keep their own Pokémon, so later fights still make sense. Losing lets you try again, and a full party means you come back for the Egg.

### Kanto starters

Prof. Oak gives them at Lv5, holding a Berry, one per conversation. The script is in `maps/OaksLab.asm`, using three new event flags.

| When | Pokémon |
|---|---|
| First time you talk to him | Bulbasaur |
| 12 badges | Charmander |
| 16 badges | Squirtle, alongside opening Mt. Silver |

After each gift, he tells you to come back when you have the next badge count, so the player knows to return. If you already have enough badges, he tells you to talk to him again. A full party means the gift waits, and it doesn't hold up Mt. Silver.

### Fossils

Solving a Ruins of Alph wall puzzle now also earns a revived fossil Pokémon. A scientist in the Research Center gives it with no held item, one per conversation. The script is in `maps/RuinsOfAlphResearchCenter.asm`, using two new event flags, and the chambers themselves didn't change.

| Puzzle solved | Pokémon |
|---|---|
| Kabuto chamber | Kabuto, Lv10 |
| Omanyte chamber | Omanyte, Lv25, higher because it comes later |

The Kabuto chamber can be reached without Surf, so Kabuto can come very early. The Omanyte chamber is reached through Union Cave and needs Surf, so Omanyte comes later. That's fine because both evolve only at Lv40, so they stay modest until the mid-game. It also gives players a reason to solve the puzzles on their first visit. After a gift, the scientist points you to the other puzzle, or tells you to talk again if you've already solved it. A full party means the gift waits.

### Legendary birds

Each bird is a one-time static encounter at the end of a Kanto dungeon that had no prize, so the player can save first. They work like Lugia: talk to the bird and the fight starts. If it faints or you run, it's gone. The game has no overworld sprite for these birds, so they reuse `SPRITE_MOLTRES` with a different color.

| Pokémon | Level | Where | Why |
|---|---|---|---|
| Zapdos | 50 | Rock Tunnel 1F, a narrow passage in the northwest section | It's next to the Power Plant, and this is the farthest walkable spot from both entrances. You can only reach that section through B1F, and the bird blocks nothing because a second passage runs alongside it |
| Moltres | 50 | Victory Road, the dead-end side room near the Route 23 exit | It's its Gen 1 home. It only appears after you beat the Elite Four, so it stays a post-league prize even though you walk through Victory Road before the league |
| Articuno | 50 | Mt. Moon, the small pocket above the Route 4 exit room | Its Gen 1 home, Seafoam Islands, is only Blaine's gym here. You reach the pocket by going out to Mt. Moon Square and back in through a second cave, so it's off the normal route. A ledge leads out, and the bird stands clear of it |

Lv50 matches the birds in Gen 1 and sits just under the Kanto leaders' target levels.

### Late legendaries

These are one-time static encounters too, available only in the late game.

| Pokémon | Level | Where | Why |
|---|---|---|---|
| Mewtwo | 70 | Silver Cave, the east end of the far item room | Silver Cave only opens at 16 badges, and this is its deepest point, past Surf and Waterfall and off the path to Red. Lv70 matches Gen 1 and sits under Red's target level. The room's Full Restore is right beside it, and you don't have to beat Red first |
| Celebi | 60 | Ilex Forest shrine, by reading it with all 16 badges | The shrine honors the forest's protector. Before 16 badges, its text adds a hint that it's waiting for a trainer with every badge. It sits between the birds and Mewtwo in level |

### Mew

Mew is the reward for catching all 26 Unown, which used to earn little more than a printer. It's a one-time Lv30 static encounter at the bottom of the Inner Chamber's lower hall, around (9, 25), reached by dropping through a solved chamber's floor.

All 26 forms need all four puzzles solved. Only the Kabuto chamber can be reached without Surf, so Mew can come as soon as the player has Surf and the patience. There's no badge gate, which is why it's Lv30, unlike the other legendaries.

When you leave the Inner Chamber after catching the last Unown, a scientist stops you outside and says where to look. The Research Center scientist repeats the hint until you've fought Mew. The Unown count only changes when you catch one, so seeing them isn't enough.

## Wild levels

Wild levels went up only where there was room below the trainers. For each map, the cap is the median ace of its first-time trainers, minus 10, or minus 5 on early routes. Maps without trainers borrow a neighbor's value, and Kanto maps without trainers use 32. A table below its cap rises halfway to it, and every slot in the table shifts by the same amount, so the spread between slots stays the same. No level went down.

| Area | Change |
|---|---|
| Most Johto routes | None. Their wild Pokémon were already within 10 levels of the trainers, closer than the cap allows |
| Union Cave B1F, Ilex Forest, Route 46 | Up 3 to 4 |
| Route 43, Route 45, Mt. Mortar, Ice Path, Whirl Islands, Dark Cave (Blackthorn side) | Up 1 to 2 |
| Tin Tower | Up 4, to 24-28 |
| Tohjo Falls | Up 3 |
| Kanto early routes, Routes 1-4, 22, 24, 25 | Up 9 to 14, to around 16-24 |
| Kanto middle routes, Routes 5-11, Mt. Moon, Rock Tunnel | Up 6 to 10, to around 16-26 |
| Kanto late routes, Routes 13-18, Diglett's Cave | Up 1 to 5 |
| Kanto and late Johto water | Up by the same rule |

Unchanged on purpose:

- **Swarms, fishing, Headbutt, Rock Smash, and the Bug-Catching Contest:** these keep their levels. Fishing levels depend on the rod, not the map.
- **Silver Cave, Route 28, Victory Road, and Mt. Mortar 2F:** these are already high.

Wild slots now evolve by level, using the same evolution levels as the player. This includes slots that were already past their evolution level, such as Rattata at Lv20 and up. Stone and friendship evolutions stay as they are in the wild.

The one exception is Magikarp, which stays Magikarp at any level, because evolving it would fill ordinary water with Gyarados.

Wild moves update on their own: the game builds a wild Pokémon's moves from its level-up list at the moment of the encounter.

## Trainer evolutions and moves

Regular trainers' Pokémon now evolve to fit their levels. Bosses keep their hand-picked teams, and the Kanto leaders, Blue, and Red wait for the Kanto pass.

| Evolution type | Rule |
|---|---|
| By level | At the player's evolution level |
| By stone | From Lv30 |
| By friendship | From Lv32 |
| Tyrogue | From Lv20 |

Where a Pokémon has more than one option, it takes the first one in its data. A trainer's Slowpoke becomes Slowbro, not Slowking. 

Most regular trainers use automatic moves, which already follow level and species. For the ones with hand-written moves, TMs and signature moves stay. Gaps are filled, and up to two older level-up moves are swapped for newer ones, but never a stronger attack for a weaker move.

## Kanto leaders

Kanto leaders can be fought in any order, so they share a narrow range. Each has six Pokémon.

| Leader | Was | Now | Notes |
|---|---|---|---|
| Brock | 41-44, 5 Pokémon | 51-54 | Onix becomes Steelix as the ace, and Aerodactyl joins. Rock Slide isn't learnable in this game, but his original team used it, and he needs Rock attacks |
| Janine | 33-39, 5 Pokémon | 50-54 | Biggest jump. Muk and Tentacruel replace her second Weezing, and Crobat is her ace |
| Lt. Surge | 40-46, 5 Pokémon | 51-54 | Ampharos and Jolteon replace his second Electrode. Raichu has Surf, a nod to Pokémon Yellow, and Ampharos has Ice Punch, so Ground types can't wall him |

## To do

Remaining work is tracked in [TODO.md](TODO.md).
