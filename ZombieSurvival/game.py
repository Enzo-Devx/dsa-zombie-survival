"""
ZOMBIE SURVIVAL — DSA Prelim Group Project (Group 4)
Redesigned to use Python lists as the core data structure.

Mandatory list requirements covered:
1. At least four meaningful lists      -> zombies, weapons, inventory, battle_log
2. Nested list for related records     -> zombies (each: [name, health, damage, difficulty])
                                        -> weapons (each: [name, min_dmg, max_dmg, ammo_cost])
3. append() during gameplay            -> battle_log.append(...), inventory.append(...)
4. pop()/remove() during gameplay      -> zombies.pop(0), inventory.remove(item)
5. Traverse with a loop                -> for zombie in zombies / while loops
6. List indexing                       -> zombie[0], zombie[1], weapon[2], etc.
7. Search through a list                -> find_weapon(), item search in inventory
8. sort()/sorted()                     -> battle_log sorted by damage dealt
9. len()/count()                       -> len(zombies), inventory.count(item)
10. Display list-based summary         -> show_inventory(), show_battle_log()
"""

import random

# ---------------------------------------------------------------------------
# GAME DATA (lists)
# ---------------------------------------------------------------------------

# Nested list: each zombie = [name, health, damage, difficulty_label]
ZOMBIE_TEMPLATE = [
    ["Walker", 16, 5, "Easy"],
    ["Runner", 24, 7, "Medium"],
    ["Crawler", 20, 6, "Medium"],
    ["Zombie Brute", 35, 10, "Hard"],
    ["Screamer", 22, 8, "Medium"],
]

# Nested list: each weapon = [name, min_damage, max_damage, resource_cost, resource_type]
WEAPONS = [
    ["Pistol", 8, 14, 1, "ammo"],
    ["Bat", 3, 6, 0, "ammo"],       # melee, costs no ammo
    ["Shotgun", 14, 22, 2, "ammo"],
]

SUPPLY_ITEMS = ["Bandage", "Food Ration", "Energy Drink"]


# ---------------------------------------------------------------------------
# HELPER / VALIDATION FUNCTIONS
# ---------------------------------------------------------------------------

def get_valid_choice(prompt, valid_options):
    """Keeps asking until the player enters one of the valid_options."""
    while True:
        choice = input(prompt).strip().lower()
        if choice in valid_options:
            return choice
        print(f"Invalid input. Please enter one of: {', '.join(valid_options)}")


def find_weapon(weapon_name, weapons_list):
    """Linear search through the weapons list. Returns the weapon record or None."""
    for weapon in weapons_list:
        if weapon[0].lower() == weapon_name.lower():
            return weapon
    return None


def search_inventory(item_name, inventory):
    """Linear search through the inventory list. Returns index if found, -1 if not."""
    for index in range(len(inventory)):
        if inventory[index].lower() == item_name.lower():
            return index
    return -1


def show_inventory(inventory):
    print("\n--- INVENTORY ---")
    if not inventory:
        print("(empty)")
    else:
        for index, item in enumerate(inventory, start=1):
            print(f"{index}. {item}")
    print(f"Total items: {len(inventory)}")


def show_weapons(weapons_list):
    print("\n--- AVAILABLE WEAPONS ---")
    for index, weapon in enumerate(weapons_list, start=1):
        name, min_dmg, max_dmg, cost, resource = weapon
        print(f"{index}. {name}  | Damage: {min_dmg}-{max_dmg}  | Cost: {cost} {resource}")


def show_battle_log(battle_log):
    print("\n--- BATTLE HISTORY (sorted by damage dealt, highest first) ---")
    if not battle_log:
        print("No battles fought yet.")
        return
    sorted_log = sorted(battle_log, key=lambda entry: entry[1], reverse=True)
    for entry in sorted_log:
        zombie_name, damage_dealt, outcome = entry
        print(f"{zombie_name:<15} | Damage dealt: {damage_dealt:<4} | Result: {outcome}")


def print_status(health, ammo, inventory):
    print(f"\nHealth: {health}  |  Ammo: {ammo}  |  Items carried: {len(inventory)}")


# ---------------------------------------------------------------------------
# CORE GAMEPLAY FUNCTIONS
# ---------------------------------------------------------------------------

def battle(zombie, player_health, ammo, inventory, weapons_list, battle_log):
    """
    Handles one encounter against a single zombie.
    zombie = [name, health, damage, difficulty]
    Returns updated (player_health, ammo).
    """
    zombie_name, zombie_health, zombie_damage, difficulty = zombie
    total_damage_dealt = 0

    print(f"\nA {zombie_name} ({difficulty}) appeared!")

    while zombie_health > 0 and player_health > 0:
        print_status(player_health, ammo, inventory)
        print(f"{zombie_name} health: {zombie_health}")
        show_weapons(weapons_list)
        print(f"{len(weapons_list) + 1}. Use a supply item")
        print(f"{len(weapons_list) + 2}. Run away")

        valid_options = [str(i) for i in range(1, len(weapons_list) + 3)]
        choice = get_valid_choice("Choose an action: ", valid_options)
        choice_num = int(choice)

        if choice_num <= len(weapons_list):
            weapon = weapons_list[choice_num - 1]
            name, min_dmg, max_dmg, cost, resource = weapon

            if resource == "ammo" and ammo < cost:
                print("Not enough ammo! Try another action.")
                continue

            ammo -= cost
            damage = random.randint(min_dmg, max_dmg)
            zombie_health -= damage
            total_damage_dealt += damage
            print(f"You used {name} and dealt {damage} damage!")

            if zombie_health > 0:
                player_health -= zombie_damage
                print(f"{zombie_name} hit you for {zombie_damage} damage.")

        elif choice_num == len(weapons_list) + 1:
            if not inventory:
                print("You have no supply items!")
                continue
            show_inventory(inventory)
            item_choice = input("Type the exact item name to use (or 'cancel'): ").strip()
            if item_choice.lower() == "cancel":
                continue
            found_index = search_inventory(item_choice, inventory)
            if found_index != -1:
                item_choice = inventory[found_index]  # normalize capitalization
                if item_choice == "Bandage":
                    player_health += 12
                    print("You used a Bandage and recovered 12 health!")
                elif item_choice == "Energy Drink":
                    player_health += 6
                    print("You used an Energy Drink and recovered 6 health!")
                elif item_choice == "Food Ration":
                    player_health += 8
                    print("You ate a Food Ration and recovered 8 health!")
                inventory.remove(item_choice)  # pop from inventory after use
                if zombie_health > 0:
                    player_health -= zombie_damage
                    print(f"{zombie_name} hit you for {zombie_damage} damage.")
            else:
                print("You don't have that item.")

        else:
            print(f"You fled from the {zombie_name}.")
            battle_log.append([zombie_name, total_damage_dealt, "Escaped"])
            return player_health, ammo

    if player_health > 0:
        print(f"You defeated the {zombie_name}!")
        battle_log.append([zombie_name, total_damage_dealt, "Defeated"])
        # random loot drop
        if random.randint(1, 2) == 1:
            loot = random.choice(SUPPLY_ITEMS)
            inventory.append(loot)
            print(f"You found a {loot} and added it to your inventory!")
    else:
        battle_log.append([zombie_name, total_damage_dealt, "Player Down"])

    return player_health, ammo


def show_title_and_instructions():
    print("=" * 50)
    print("           ZOMBIE SURVIVAL")
    print("=" * 50)
    print("""
Survive as many zombie encounters as you can!
- Fight using weapons (each costs ammo, except melee)
- Use supply items to heal
- Manage your ammo and health carefully
- Defeat zombies to earn loot
- Survive at least 3 encounters with health remaining to WIN
""")


def play_round(player_health, ammo, inventory, zombies, weapons_list, battle_log):
    """Plays through all remaining encounters. Returns final health."""
    encounter_number = 1
    while zombies and player_health > 0:
        print(f"\n=== ENCOUNTER {encounter_number} ===")
        current_zombie = zombies.pop(0)  # remove next zombie from the list
        player_health, ammo = battle(
            current_zombie, player_health, ammo, inventory, weapons_list, battle_log
        )
        encounter_number += 1

        if player_health <= 0:
            break

        if zombies:
            cont = get_valid_choice("\nContinue to next encounter? y/n: ", ["y", "n"])
            if cont == "n":
                print("You decide to retreat and end your run here.")
                break

    return player_health, ammo


def final_summary(player_name, player_health, inventory, battle_log):
    print("\n" + "=" * 50)
    print("               FINAL SUMMARY")
    print("=" * 50)
    print(f"Survivor: {player_name}")
    print(f"Final health: {max(player_health, 0)}")

    zombies_defeated = 0
    for entry in battle_log:
        if entry[2] == "Defeated":
            zombies_defeated += 1

    print(f"Zombies defeated: {zombies_defeated}")
    print(f"Total encounters faced: {len(battle_log)}")
    show_battle_log(battle_log)
    show_inventory(inventory)

    if player_health > 0 and zombies_defeated >= 3:
        print("\nYOU SURVIVED THE NIGHT! YOU WIN!")
    elif player_health > 0:
        print("\nYou survived, but needed to defeat more zombies for a full victory.")
    else:
        print("\nYou were overwhelmed by the horde. GAME OVER.")


def main():
    while True:
        show_title_and_instructions()
        player_name = input("Enter your survivor name: ").strip() or "Survivor"

        # Fresh game state each playthrough
        player_health = 50
        ammo = 8
        inventory = ["Bandage"]                      # starting item
        zombies = [row[:] for row in ZOMBIE_TEMPLATE]  # copy so original template stays intact
        weapons_list = WEAPONS
        battle_log = []

        print(f"\nGood luck, {player_name}. {len(zombies)} zombies stand between you and safety.")

        player_health, ammo = play_round(
            player_health, ammo, inventory, zombies, weapons_list, battle_log
        )

        final_summary(player_name, player_health, inventory, battle_log)

        again = get_valid_choice("\nPlay again? y/n: ", ["y", "n"])
        if again == "n":
            print("Thanks for playing ZOMBIE SURVIVAL!")
            break


if __name__ == "__main__":
    main()