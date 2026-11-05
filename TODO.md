# To do

The current plan, in order. Each topic is proposed and approved before any game file changes.

## 1. Catchable Pokémon and better Gen 2 availability

All 251 are now obtainable on one save, with as few code changes as possible. Done: Gold-only Pokémon, rare and late Pokémon, evolution stones, Johto starters, Kanto starters, fossils, the three legendary birds, Mewtwo, Mew, and Celebi.

Wild levels are done too. See `BALANCE_NOTES.md`.

## 2. Trainer evolutions and movesets

Done.

## 3. Finish Kanto

Done: the Kanto leaders and gym trainers, the later rival fights, Blue, Red, and a full pass on trainer levels. `python tools/audit_trainers.py` repeats the check.

## 4. Clearly unusable Pokémon

Improve the stats of extreme cases only, such as Ledian. Everyone else stays as they are.

Sneasel is on the list: its Dark and Ice moves are special, and it has only 35 Sp. Atk.

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
- The Kanto leaders and gym trainers, the later rival fights, Blue, and Red.
- The evolved trainer teams, especially Crobat, Gyarados, and other early evolutions.
- The Mew reward: the scientist's news on catching the last Unown, and the encounter in the lower hall.
