# Pokémon Silver balance hack (pret/pokegold)

## Goal
Build a modified Pokémon Silver ROM from the pret/pokegold disassembly and fix its balance flaws.
The challenge should climb steadily from the first leader to Red, with no plateaus, and every
Pokémon should be obtainable on one cartridge.

## Current state
- Done: level-based trade evolutions, Johto boss teams, regular trainer levels, type awareness
  for the boss AI, all 251 Pokémon obtainable on one save, wild levels, and evolved regular trainers. `BALANCE_NOTES.md` has every change and its reason.
- Next: see `TODO.md`, and work through it in order.
- Most of this hasn't been played, so don't describe a change as tested unless I've reported it.

## Hard constraints
- Start from the vanilla base game. Do NOT add the physical/special split: Gen 2 keeps the
  type-based split (Fire, Water, Grass, Electric, Psychic, Ice, Dragon, Dark = special; the rest physical). Leave that logic alone.
- Scope grows only when I ask. So far I've asked for evolutions, trainer teams and levels, the
  battle AI, encounters (availability), and stat buffs for extreme cases. Anything else is out of
  scope until I ask for it.
- Special is already split into Sp. Atk and Sp. Def in Gen 2, so both can be tuned independently.

## Setup
- Repo: https://github.com/pret/pokegold (use pokegold, NOT pokegold-spaceworld, which is the 1997 prototype).
- Read INSTALL.md for the exact RGBDS version and platform steps. On Windows, use WSL (Ubuntu).
- Build: `make silver` produces `pokesilver.gbc`. `roms.sha1` only matches the unmodified game.
- Git: work on `balance`. `origin` is my public fork (elpiris/PokemonSilverBullet) and `upstream`
  is pret/pokegold. `master` stays identical to upstream. Never commit ROMs or saves.
- Test emulator: mGBA (mgba.io). Prefer fast-forward and quick saves when testing.

## Where things live
- Base stats: `data/pokemon/base_stats/<name>.asm`
  - Stat line order: HP, Attack, Defense, Speed, Sp. Atk, Sp. Def (e.g. `db 35, 55, 30, 90, 50, 40`).
  - The same file also holds types, catch rate, base exp, items, growth rate, TM/HM compatibility.
    Open a file and read it before assuming the layout.
- Level-up moves and evolutions: `data/pokemon/evos_attacks.asm`.
- Trainer teams: `data/trainers/parties.asm`. Parties are grouped by class, not location, so use
  the `trainer` and `loadtrainer` lines in `maps/*.asm` to find where each one appears.
- Trainer AI flags: `data/trainers/attributes.asm`. Move scoring: `engine/battle/ai/scoring.asm`.
- Stat audit: `python tools/audit_stats.py` regenerates `BASE_STATS_AUDIT.md`.

## Workflow
1. Take one topic at a time. Propose changes in a short list (current -> proposed, with a one-line
   reason) and wait for my approval before editing game files. Confirm key fights one by one.
2. If I ask for a quick pass, apply it directly and summarize the result instead of asking per item.
3. Apply approved changes in small batches: one commit per batch with a clear message.
4. Rebuild with `make silver` after each batch and make sure the build succeeds.
5. Keep `BALANCE_NOTES.md` updated with every change and its reasoning, and `TODO.md` with the plan.

## Balance guidelines
- Bosses: team size grows from 3 to 6 over the game, level-up moves come first with TMs only where
  they define a fight, and aces may be evolved below the player's evolution level. Rival aces carry
  a strong same-type move.
- Regular trainers stay easier than the next boss, but shouldn't be a pushover. Keep their levels
  capped below that boss.
- Stat buffs are for clearly unusable Pokémon only, such as Ledian. Don't propose a wider rebalance.
- Buff sparingly and keep each Pokémon in its intended role (e.g. don't turn a fast glass cannon into a tank).
- Compare against Pokémon of similar evolution stage and availability, and watch for early-game
  Pokémon becoming too strong for Johto's level curve.
- Keep fully evolved weak Pokémon near the BST range of comparable fully evolved ones.

## Candidates to audit for stat buffs (from general knowledge, verify against the actual data)
Butterfree, Beedrill, Fearow, Raticate, Arbok, Parasect, Farfetch'd, Dewgong, Ledian, Ariados,
Furret, Noctowl, Delibird, Corsola, Sunflora. This is only a starting list, and only extreme cases
should change; let the stat audit decide.

## How I work
- I prefer English for all code, comments, commit messages, and docs.
- Ask before any destructive action (force-push, deleting branches, rewriting history).
