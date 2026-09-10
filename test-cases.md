# Test Cases — Zombie Survival

This document records manual test cases run against `game.py` to verify the game's core mechanics, list operations, and input handling work as intended.

**Tested by:** Karioca Ceniza (QA Tester and Documentation Lead)
**Environment:** Python 3, VS Code terminal

| # | Test Case | Steps | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| 1 | Exact match inventory search | Take damage, choose "Use a supply item," type an exact item name (e.g. `Bandage`) | Health increases, item is removed from inventory | Health increased, item removed correctly | ✅ Pass |
| 2 | Case-insensitive inventory search | Same as above, but type `bandage` or `BANDAGE` | Item is still found and used despite case difference | Item found and used correctly regardless of case | ✅ Pass |
| 3 | Item not found | Choose "Use a supply item," type an item not in inventory (e.g. `Sword`) | Game prints "You don't have that item." and does not crash | Message displayed correctly, no crash | ✅ Pass |
| 4 | Empty inventory | Choose "Use a supply item" before picking up any loot | Game prints "You have no supply items!" and returns to action menu | Message displayed correctly, returned to menu | ✅ Pass |
| 5 | Invalid menu input | At any action prompt, type letters, symbols, or an out-of-range number | Game prints an invalid input message and re-prompts without crashing | Re-prompted correctly, no crash | ✅ Pass |
| 6 | Win and lose conditions | Play one run losing on purpose (never heal), play one run winning (defeat 3+ zombies) | GAME OVER shown on loss; YOU WIN shown after 3+ defeats with health remaining | Both outcomes displayed correctly with accurate summary | ✅ Pass |
| 7 | Ammo depletion | Use a weapon that costs ammo until ammo reaches 0, then try to use it again | Game blocks the action ("Not enough ammo!") and lets the player pick another action instead | Blocked correctly, no crash | ✅ Pass |
| 8 | Zombie list traversal | Play through a full run and confirm all zombies in the `zombies` list are encountered in order, none skipped or repeated | Each encounter pulls the next zombie via `pop(0)` until the list is empty | Zombies encountered in correct order, list emptied properly | ✅ Pass |
| 9 | Battle log sorting | Finish a run with multiple battles logged, check the final summary | Battle history displays sorted by damage dealt, highest first | Battle log displayed in correct sorted order | ✅ Pass |
| 10 | Play-again loop | At the end of a run, choose `y` to play again | Game resets health, ammo, inventory, and zombie list, and starts a fresh playthrough | Game state reset correctly, new playthrough started | ✅ Pass |

## Bugs Found and Fixed

| Bug | Description | Fix |
|---|---|---|
| Unused search requirement | `find_weapon()` was written but never called during gameplay, leaving requirement #7 (search through a list) unsatisfied | Added `search_inventory()` function and wired it into the supply-item-use flow in `battle()`, replacing the implicit `in` operator check |

## Summary

All 10 test cases passed after the search fix was applied. No crashes were observed across normal gameplay, edge cases (empty inventory, no ammo), or invalid input handling.
