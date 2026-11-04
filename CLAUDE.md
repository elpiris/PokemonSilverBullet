# Pokémon Silver balance hack (pret/pokegold)

## Goal
Build a modified Pokémon Silver ROM from the pret/pokegold disassembly and fix balance flaws
by improving the base stats of Pokémon that need it.

## Hard constraints
- Start from the vanilla base game. Do NOT add the physical/special split: Gen 2 keeps the
  type-based split (Fire, Water, Grass, Electric, Psychic, Ice, Dragon, Dark = special; the rest physical). Leave that logic alone.
- Scope is stat rebalancing. Changes to movesets, evolutions, encounters, or difficulty are
  out of scope unless I ask for them explicitly.
- Special is already split into Sp. Atk and Sp. Def in Gen 2, so both can be tuned independently.

## Setup
- Repo: https://github.com/pret/pokegold (use pokegold, NOT pokegold-spaceworld, which is the 1997 prototype).
- Read INSTALL.md for the exact RGBDS version and platform steps. On Windows, use WSL (Ubuntu).
- Build: `make silver` produces `pokesilver.gbc`. Verify the vanilla build boots before changing anything.
- Test emulator: mGBA (mgba.io). Prefer fast-forward and quick saves when testing.

## Where things live
- Base stats: `data/pokemon/base_stats/<name>.asm`
  - Stat line order: HP, Attack, Defense, Speed, Sp. Atk, Sp. Def (e.g. `db 35, 55, 30, 90, 50, 40`).
  - The same file also holds types, catch rate, base exp, items, growth rate, TM/HM compatibility.
    Open a file and read it before assuming the layout.
- Level-up moves and evolutions: `data/pokemon/evos_attacks.asm` (read-only reference for now).

## Workflow
1. Build vanilla, confirm it boots in mGBA, and commit that as the baseline.
2. Audit all base stats and produce a table (name, BST, per-stat values) so weak Pokémon can be
   identified objectively rather than by gut feeling.
3. Propose buffs in a short list (current -> proposed, with a one-line reason) and wait for my
   approval before editing files.
4. Apply approved changes in small batches: one commit per batch with a clear message
   (e.g. `buff bug-type stats: Butterfree, Beedrill`).
5. Rebuild with `make silver` after each batch and make sure the build succeeds.
6. Keep a `BALANCE_NOTES.md` with every change and its reasoning.

## Balance guidelines
- Buff sparingly and keep each Pokémon in its intended role (e.g. don't turn a fast glass cannon into a tank).
- Compare against Pokémon of similar evolution stage and availability, and watch for early-game
  Pokémon becoming too strong for Johto's level curve.
- Keep fully evolved weak Pokémon near the BST range of comparable fully evolved ones.

## Starting candidates to audit (from general knowledge, verify against the actual data)
Butterfree, Beedrill, Fearow, Raticate, Arbok, Parasect, Farfetch'd, Dewgong, Ledian, Ariados,
Furret, Noctowl, Delibird, Corsola, Sunflora. This is only a starting list; let the stat audit decide.

## How I work
- I prefer English for all code, comments, commit messages, and docs.
- Ask before any destructive action (force-push, deleting branches, rewriting history).
