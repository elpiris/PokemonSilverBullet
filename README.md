# Pokémon Silver Bullet

A balance hack of Pokémon Silver that keeps the original game's feel and fixes its best-known flaws: trade-only evolutions and an uneven level curve. The goal is a challenge that climbs steadily from the first gym to the final battle against Red, with every Pokémon obtainable on one cartridge.

It's built on [pret/pokegold](https://github.com/pret/pokegold), a disassembly of Pokémon Gold and Silver. Gen 2's type-based physical/special split stays as it was.

No ROMs are included. You build one yourself from this source.

## What's changed so far

- **No trade evolutions:** every trade evolution now happens by level. Slowking needs a held King's Rock at Lv37, so Slowpoke's choice between Slowbro and Slowking stays with the player.
- **Johto bosses:** gym leaders, rival fights, Rocket executives, the Elite Four, and Lance have new levels, teams, and moves, so the challenge climbs with the story.
- **Regular trainers:** levels are raised by area to sit closer to the next boss. Species and movesets aren't updated yet, so some Pokémon are past their usual evolution level.
- **Battle AI:** bosses and Cooltrainers now favor super effective moves.
- **Availability (in progress):** Gold-only Pokémon are now in Silver, rare and late Pokémon are easier to find, and evolution stones are pickups around the world and sold late in Celadon.

Kanto is unfinished: its leaders still have their original teams.

Most of this hasn't been playtested yet. See [BALANCE_NOTES.md](BALANCE_NOTES.md) for every change and the reason for it, and [TODO.md](TODO.md) for what's next.

## Building

Follow [INSTALL.md](INSTALL.md) to set up RGBDS, then run:

```bash
make silver
```

This produces `pokesilver.gbc`. Only the Silver build has been checked. The hashes in `roms.sha1` are for the unmodified games, so they won't match this hack.

## Credits

The disassembly is the work of the [pret](https://pret.github.io/) team and contributors.

This is an unofficial fan project, not affiliated with or endorsed by Nintendo, Game Freak, or The Pokémon Company.
