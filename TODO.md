# To do

The current plan, in order. Each topic is proposed and approved before any game file changes.

## 1. Catchable Pokémon and better Gen 2 availability

All 251 are now obtainable on one save, with as few code changes as possible. Done: Gold-only Pokémon, rare and late Pokémon, evolution stones, Johto starters, Kanto starters, fossils, the three legendary birds, Mewtwo, Mew, and Celebi.

Wild levels are done too. See `BALANCE_NOTES.md`.

## 2. Trainer evolutions and movesets

Done for regular trainers. The Kanto leaders, Blue, and Red still need theirs in the Kanto pass below.

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
- The starter gifts from Elm and Oak, and the New Bark Town rival fight.
- The fossil gifts in the Research Center.
- The static birds: Zapdos in Rock Tunnel, Moltres in Victory Road after the league, and Articuno in the Mt. Moon pocket, including whether it can be seen from the Route 4 exit room.
- The static Mewtwo in Silver Cave.
- The static Celebi at the Ilex Forest shrine.
- The new wild levels and evolved wild slots, mainly in Kanto.
- The evolved trainer teams, especially Crobat, Gyarados, and other early evolutions.
- The Mew reward: the scientist's news on catching the last Unown, and the encounter in the lower hall.
