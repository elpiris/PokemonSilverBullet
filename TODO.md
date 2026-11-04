# To do

The current plan, in order. Each topic is proposed and approved before any game file changes.

## 1. Catchable Pokémon and better Gen 2 availability

- Make sure every Pokémon can be caught on one Silver cartridge.
- Make Gen 2 Pokémon more available in general.
- Wild Pokémon levels haven't been adapted to the new curve yet, so decide whether to handle them here.

## 2. Trainer evolutions and movesets

The regular trainer pass only changed levels. Evolve trainers' Pokémon and update their movesets to fit those new levels.

## 3. Finish Kanto

- Leaders, with these target top levels:
  - Janine, Brock, and Lt. Surge: 54
  - Erika: 55
  - Misty and Sabrina: 56
  - Blaine: 58
- Another pass on Kanto trainers, including the gym trainers, which haven't changed. Route trainers are now up to Lv48, above some vanilla leaders until this is done.
- Later fights, with these target top levels:
  - Rival at Mt. Moon: 53 (now 45)
  - Rival at Indigo Plateau: 60 (now 50)
  - Blue: 64 (now 58)
  - Red: 75 (now 81), though this level is still open
- Consider fixing the `RIVAL2` DV bug in `data/trainers/dvs.asm`.

## 4. Clearly unusable Pokémon

Improve the stats of extreme cases only, such as Ledian. Everyone else stays as they are.

## Testing

Only booting has been confirmed so far. These still need testing in-game:

- The level-based evolutions, including Slowking with a King's Rock.
- The Johto boss fights.
- The new trainer levels.
- The boss AI change.
