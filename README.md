# 🎮 Zombie Survival — DSA Prelim Group Project

A console-based Python survival game where the player fights through a series of zombie encounters using weapons, supplies, and strategy. Originally a repetitive, variable-heavy starter script, redesigned to use **Python lists and nested lists** as its core data structure for Data Structures and Algorithms (DSA) — Prelim Group Project, Group 4.

## 🎮 Game Description

Survive as many zombie encounters as you can. Manage your health, ammo, and supplies while fighting a variety of zombies, each with different health, damage, and difficulty. Defeat zombies to earn loot, use supply items to heal, and make it through at least 3 encounters with health remaining to win.

## 🎮 Members and Roles

| Name | Role |
|---|---|
| Joniel Amoguis | Game Producer / Team Leader |
| Milan Mojello | Lead Game Programmer |
| Dairjeen Abasolo | Gameplay and Logic Programmer |
| Jasper Emano | Game/UI Designer and Writer |
| Karioca Ceniza | QA Tester and Documentation Lead |

## 🎮 Installation / How to Run

1. Make sure [Python 3](https://www.python.org/downloads/) is installed on your machine.
2. Clone this repository or download `game.py`.
   ```
   git clone https://github.com/Enzo-Devx/dsa-zombie-survival.git
   ```
3. Navigate into the project folder.
   ```
   cd dsa-zombie-survival
   ```
4. Run the game.
   ```
   python game.py
   ```

## 🎮 Controls / How to Play

- Enter your survivor name at the start.
- During each encounter, choose an action by typing its menu number:
  - Select a weapon (each costs ammo, except melee options)
  - Use a supply item (type the item name when prompted)
  - Run away from the current zombie
- Answer `y`/`n` prompts to continue between encounters or play again.
- Survive at least 3 encounters with health remaining to win.

## ❗ List Operations Used

This project fulfills the 10 mandatory list requirements from the DSA Prelim rubric:

| # | Requirement | Where it's used |
|---|---|---|
| 1 | 4+ meaningful lists | `zombies`, `weapons_list`, `inventory`, `battle_log` |
| 2 | Nested list | `zombies` (`[name, health, damage, difficulty]`), `weapons_list` (`[name, min_dmg, max_dmg, cost, resource]`) |
| 3 | `append()` in gameplay | Adding loot to `inventory`, logging results to `battle_log` |
| 4 | `pop()` / `remove()` in gameplay | `zombies.pop(0)` per encounter, `inventory.remove(item)` after use |
| 5 | Traverse with a loop | `for`/`while` loops through zombies, weapons, and battle turns |
| 6 | List indexing | Accessing `zombie[0]`, `weapon[1]`, etc. |
| 7 | Search through a list | `find_weapon()` and `search_inventory()` — linear search functions |
| 8 | `sort()` / `sorted()` | Battle log sorted by damage dealt for the final summary |
| 9 | `len()` / `count()` | Tracking zombies remaining, inventory size |
| 10 | Display list-based summary | Final inventory and battle history shown at game end |

## 🎮 Gameplay Features

- Title screen and player-name input
- Clear in-game instructions
- 5 zombie types across 3+ encounters per playthrough
- Health, ammo, and inventory management
- Meaningful choices (weapon selection, item use, retreat option)
- Win and lose conditions
- Play-again option
- Input validation to prevent crashes from invalid input
- Final summary with sorted battle history and inventory display

## ✨ Creativity / Changes from Starter Code

- Added 2 new zombie types (Crawler, Screamer) beyond the original 3
- Added 2 new weapons (Bat, Shotgun) beyond basic shoot/punch
- Added a random loot-drop system after defeating zombies
- Added a "continue or retreat" choice between encounters

## 🎮 Screenshots

_(Add screenshots of the title screen, a battle in progress, and the final summary here)_

## 🎮 Testing

See [`test-cases.md`](./test-cases.md) for the full test case table and bug log.

## 📐 Flowchart

See `flowchart.png` for the program's overall flow.
