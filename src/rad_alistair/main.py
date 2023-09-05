import sys
import random
import time

from rad_alistair.character import Character, spawn_bat, spawn_demon, spawn_skeleton
from rad_alistair.item import Item, Helmet, BaseArmor, HeadArmor, ChestArmor, WaistArmor, LegArmor, FeetArmor, Accessory, Weapon

player_character = Character("Marshmellow", 100, 20, 10)
Alistair = Character("Alistair", 200, 20, 10)


introduction = '''You awake but don't open your eyes.
Your head throbs and an
excruciating pain shoots down your spine.
'What happened? Where am I?'
You feel the warmth from a
nearby fire and hear it crackling.
You peel an eye open. '''

total_victories = 0
total_deaths = 0
inventory = {
    "gold": 0,
    "silver": 0,
    'weapon': False,
    "helmet": False,
    "accessory": False,
    "item": False,
    "backpack": [],
}


def check_backpack(search_name):
    backpack = inventory["backpack"]
    for item in backpack:
        if getattr(item, "name", None) == search_name:
            return True
    return False


def action_1():
    print("\nYou're in a small room.")
    time.sleep(1)
    print("The walls are made of cobblestone.")
    time.sleep(1)
    print("A single torch provides light.")
    time.sleep(1)
    print("\nFear spikes as your memory returns.")
    time.sleep(1)
    print("\n")
    print("A simple quest of finding a missing child\nended with you captured by the Cult of Alistair.\nNow you're in a dungeon and your sword is gone.\nYou take the torch and walk down the hallway.")
    item_1 = Item(name="Torch", weight=1, defense=0)
    player_character.inventory.append(item_1)
    print("\n")
    player_character.print_inventory()
    time.sleep(3)
    return action_2


def action_2():
    print("\n")
    print("You enter room 2")
    print("The first room is empty but has 3 doors.")
    print("One to the West, North, and East.")
    print("You can hear people talking in the distance.")
    print("Which do you choose?")
    while True:
        response = get_input("W, N, E")
        if response == "w":
            time.sleep(1)
            return action_3
        elif response == "n":
            time.sleep(1)
            return action_4
        elif response == "e":
            time.sleep(1)
            return action_5


def action_3():
    global total_deaths
    global total_victories
    time.sleep(1)
    print("\n")
    print("You enter the west room(3).")
    print("Bats flutter overheard.")
    print("The room is otherwise empty")
    print("Would you like to search the room?")
    while True:
        response = get_input("Y, N")
        if response == "y":
            time.sleep(1)
            print("You find a Key!")
            item_2 = Item(name="Key", weight=1, defense=0)
            player_character.inventory.append(item_2)
            print("\n")
            player_character.print_inventory()
            print("\n")
            time.sleep(1)
            print("The room is now empty.")
            print("You return to the previous room.")
            return action_2
        elif response =="n":
            time.sleep(1)
            print("You return to main room")
            return action_2


def action_4():
    global total_deaths
    global total_victories
    time.sleep(1)
    print("\n")
    print("You enter the north room(4).")
    print("Skeleton's are fighting over what to eat.")
    print("They haven't seen you.")
    print("What would you like to do?")
    while True:
        choice = get_input("1. Fight\n2. Sneak passed skeletons")
        spawned_skeleton = spawn_skeleton()
        if choice == "1":
            time.sleep(1)
            result = run_battle(player_character, spawned_skeleton)
            if result == "victory":
                reward = random.randint(2, 10)  # Generate a random number between 2 and 10
                print(
                    f"You kill {spawned_skeleton.name}!\n"
                    f"You find {reward} gold pieces!"
                )
                inventory["gold"] += reward  # Add the reward to the inventory
                total_victories += 1  # Update the victory counter by adding 1 to whatever it currently is at
                time.sleep(1)
                print("The room is now empty.")
                print("There is a door to the north.")
                return action_6
            elif result == "defeat":
                total_deaths += 1
                print(f"You are a disappointment to your father. Inigo Montoya is also disappointed!")
                return action_exit
            else:
                return action_2
        if choice == "2":
            print("You enter the door to the north.")
            return action_6



def action_5():
    global total_deaths
    global total_victories
    global character
    time.sleep(1)
    print("\n")
    print("You enter the east room(5)")
    print("A skeleton sees you enter the room.")
    print("What would you like to do?")
    while True:
        choice = get_input("1. Fight\n2. Retreat")
        spawned_skeleton = spawn_skeleton()
        if choice == "1":
            time.sleep(1)
            result = run_battle(player_character, spawned_skeleton)
            if result == "victory":
                reward = random.randint(2, 10)  # Generate a random number between 2 and 10
                print(
                    f"You kill {spawned_skeleton.name}!\n"
                    f"You find {reward} gold pieces!"
                )
                inventory["gold"] += reward  # Add the reward to the inventory
                total_victories += 1  # Update the victory counter by adding 1 to whatever it currently is at
                time.sleep(1)
                print("You rummage through whats left of his bony body.")
                print("One bone is a perfect club.")
                print("You find Bone Club!")
                weapon_1 = Weapon(name="Bone Club", weight=2, attack=8)
                print("\n")
                player_character.print_inventory()
                print("\n")
                print("Equip the Bone Club?")
                response = get_input("Y, N")
                if response == "y":
                    print("You have equipped the Bone club!")
                    player_character.lhand = weapon_1
                    time.sleep(1)
                    print("The room is now empty.")
                    print("You return to the previous room.")
                    time.sleep(1)
                    return action_2
                else:
                    time.sleep(1)
                    player_character.inventory.append(weapon_1)
                    print("The room is now empty.")
                    print("You return to the previous room.")
                    time.sleep(1)
                    return action_2
            elif result == "defeat":
                total_deaths += 1
                print(f"You are a disappointment to your father. Inigo Montoya is also disappointed!")
                return action_exit
        elif choice == "2":
            time.sleep(1)
            return action_2


def action_6():
    global total_deaths
    global total_victories
    global inventory
    time.sleep(1)
    print("\n")
    print("You enter the north room(6).")
    print("A Skeleton attacks you!")
    spawned_skeleton = spawn_skeleton()
    result = run_battle(player_character, spawned_skeleton)
    if result == "victory":
        reward = random.randint(2, 10)  # Generate a random number between 2 and 10
        print(
            f"You kill {spawned_skeleton.name}!\n"
            f"You find {reward} gold pieces!"
        )
        inventory["gold"] += reward  # Add the reward to the inventory
        total_victories += 1  # Update the victory counter by adding 1 to whatever it currently is at
        time.sleep(1)
        print("\n")
        player_character.print_inventory()
        print("\n")
        time.sleep(1)
        print("There are doors to the west and east.")
        print("Which do you choose?")
        while True:
            response = get_input("W, E")
            if response == "w":
                time.sleep(1)
                return action_7
            elif response == "e":
                time.sleep(1)
                return action_8
            elif result == "defeat":
                return action_exit


def action_7():
    global inventory
    time.sleep(1)
    print("\n")
    print("You enter the west room(7).")
    print("The room is safe.")
    print("A statue is in the middle of the room.")
    print("Do you want to inspect it?")
    while True:
        response = get_input("Y, N")
        if response == "y":
            print("It's a stone statue of a large man,")
            print("wearing a winged helmet, and holding a hammer.")
            print("There's an inscription that reads:")
            print("Pray before Thor Odinson for strength.")
            print("Do you pray?")
            response = get_input("Y, N")
            if response == "y":
                print("You are healed and power surges through your veins!")
                player_character.health += 25
                player_character.base_attack += 5
                time.sleep(1)
                return action_9
            else:
                return action_9
        else:
            time.sleep(1)
            print("An ethereal hammer flies through the air and strikes you!")
            player_character.health -= 10
            return action_9


def action_8():
    global total_deaths
    global total_victories
    time.sleep(1)
    print("\n")
    print("You enter the east room(8).")
    print("Bats fly overhead.")
    print("Do you want to inspect the room?")
    while True:
        response = get_input("Y, N")
        if response == "y":
            time.sleep(1)
            spawned_bat = spawn_bat()
            print(f"A {spawned_bat.name} attacks you")
            result = run_battle(player_character, spawned_bat)
            if result == "victory":
                reward = random.randint(2, 10)  # Generate a random number between 2 and 10
                print(
                    f"You kill {spawned_bat.name}!\n"
                    f"You find {reward} gold pieces!"
                )
                inventory["gold"] += reward  # Add the reward to the inventory
                total_victories += 1  # Update the victory counter by adding 1 to whatever it currently is at
                time.sleep(1)
                print("\n")
                player_character.print_inventory()
                print("\n")
                time.sleep(1)
                print("You return to the previous room.")
                return action_6
            elif result == "defeat":
                print("Bat turns into a vampire and sucks your blood!")
                return action_exit
            else:
                print("You return to the previous room.")
                return action_6
        elif response == "n":
            time.sleep(1)
            print("You return to the previous room.")
            return action_6


def action_9():
    time.sleep(1)
    print("\n")
    print("You enter the north room(9).")
    print("There is a locked door to the west and an open door to the east.")
    print("What do you want to do?")
    print("1. Inspect door\n2. Search room\n3. Go east")
    while True:
        response = get_input("1, 2, 3")
        if response == "1":
            time.sleep(1)
            print("The locked door has no keyhole.")
            return action_9
        elif response == "2":
            time.sleep(1)
            print("There is a pillar in the middle of the room.")
            print("It doesn't seem to hold up anything.")
            print("Do you want to push it?")
            response = get_input("Y, N")
            if response == "y":
                time.sleep(1)
                print("West door opens. You go through the door.")
                return action_10
        elif response == "3":
            time.sleep(1)
            return action_11


def action_10():
    time.sleep(2)
    print("\n")
    print("You enter the west room(10).")
    print("An old man is sitting by a fire.")
    time.sleep(2)
    print("He looks at you and says,")
    time.sleep(2)
    print("Eastmost Penninsula is the secret!")
    time.sleep(2)
    print("You don't understand and slowly back away.")
    time.sleep(2)
    print("His maniacal laughter echoes through the dungeon.")
    return action_9


def action_11():
    time.sleep(1)
    print("\n")
    print("You enter the east room(11).")
    print("There are doors to the north and east.")
    print("Slimes are sliming around.")
    print("They're easy to dodge.")
    print("Which door do you choose?")
    while True:
        response = get_input("N, E")
        if response == "n":
            time.sleep(1)
            return action_12
        elif response == "e":
            time.sleep(1)
            return action_16


def action_12():
    time.sleep(1)
    print("\n")
    print("You enter the north room(12).")
    print("There's a narrow walkway leading to a door to the north.")
    print("Water lies on both sides of the walkway.")
    print("Do you cross?")
    while True:
        response = get_input("Y, N")
        if response == "y":
            time.sleep(1)
            return action_13
        elif response == "n":
            time.sleep(1)
            print("Skeletons attack!")
            return action_12

def action_13():
    global total_deaths
    global total_victories
    time.sleep(1)
    print("\n")
    print("You enter the north room(13).")
    print("Demons are playing with boomerangs.")
    print("One sees you, smiles, and throws a boomerang at you.")
    print("Do you catch it?")
    while True:
        response = get_input("Y, N")
        if response == "y":
            time.sleep(1)
            print("Demon attack!")
            spawned_demon = spawn_demon()
            result = run_battle(player_character, spawned_demon)
            if result == "victory":
                reward = random.randint(2, 10)  # Generate a random number between 2 and 10
                print(
                    f"You kill Demon!\n"
                    f"You find {reward} gold pieces!"
                )
                inventory["gold"] += reward  # Add the reward to the inventory
                total_victories += 1  # Update the victory counter by adding 1 to whatever it currently is at
                time.sleep(1)
                print("You find a Studded Leather Vest!")
                armor_1 = ChestArmor(name="Studded Leather Vest", weight=2, defense=10)
                print("\n")
                player_character.print_inventory()
                print("\n")
                print("Equip the Studded Leather Vest?")
                response = get_input("Y, N")
                if response == "y":
                    print("You have equipped the Studded Leather Vest!")
                    player_character.ChestArmor = armor_1
                    return action_14
                else:
                    player_character.inventory.append(armor_1)
                    return action_14
            elif result == "defeat":
                return action_exit
        else:
            time.sleep(1)
            print("You run through the door to the west.")
            return action_14


def action_14():
    time.sleep(1)
    print("\n")
    print("You enter the west room(14).")
    print("Spikes shoot out of the walls, nearly hitting you.")
    print("They receed. Do you move forward(f) or wait(w)?")
    while True:
        response = get_input("F, W")
        if response == "f":
            time.sleep(1)
            print("You cross into the room and spikes close behind you.")
            time.sleep(1)
            print("In the center of the room")
            print("Blocks are in the shape of a diamond.")
            print("Do you inspect them?")
            response = get_input("Y, N")
            if response == "y":
                time.sleep(1)
                print("You find a hidden passageway!")
                return action_15
            elif response == "n":
                time.sleep(1)
                print("Spikes shoot out of the walls and receed.")
                time.sleep(1)
                print("Do you move forward(f) or wait(w)?")
                response = get_input("F, W")
                if response == "f":
                    time.sleep(1)
                    print("Spikes shoot out of the walls and kill you dead!")
                    return action_exit
                elif response == "w":
                    time.sleep(1)
                    print("You cross into the room and spikes close behind you.")
                    time.sleep(1)
                    print("In the center of the room")
                    print("Blocks are in the shape of a diamond.")
                    print("Do you inspect them?")
                    response = get_input("Y, N")
                    if response == "y":
                        time.sleep(1)
                        print("You find a hidden passageway!")
                        return action_15
        elif response == "w":
            time.sleep(1)
            print("Spikes shoot out of the walls and receed.")
            time.sleep(1)
            print("Do you move forward(f) or wait(w)?")
            response = get_input("F, W")
            if response == "f":
                time.sleep(1)
                print("Spikes shoot out of the walls and kill you dead!")
                return action_exit
            elif response == "w":
                print("'What are you so afraid of?,' you hear in the distance.")
                time.sleep(1)
                print("Spikes shoot out of the walls and receed.")
                time.sleep(1)
                print("Do you move forward(f) or wait(w)?")
                response = get_input("F, W")
                if response == "f":
                    print("You hear laughter, possibly from the creator.")
                    time.sleep(1)
                    print("Spikes shoot out of the walls and kill you dead!")
                    return action_exit
                elif response == "w":
                    print("You hear laughter, possibly from the creator.")
                    time.sleep(1)
                    print("Spikes shoot out of the walls and kill you dead!")
                    return action_exit



def action_15():
    time.sleep(1)
    print("\n")
    print("You climb down stairs and see a pillar of light.")
    print("You follow the light and find a Bow!")
    weapon_2 = Weapon(name="Bow", weight=2, attack=1)
    player_character.inventory.append(weapon_2)
    print("\n")
    player_character.print_inventory()
    print("\n")
    print("You retrace your steps(15).")
    return action_11


def action_16():
    global total_deaths
    global total_victories
    time.sleep(1)
    print("\n")
    print("You enter the east room(16).")
    print("Demons are playing with boomerangs.")
    print("One sees you, smiles, and throws a boomerang at you.")
    print("Do you catch it?")
    spawned_demon = spawn_demon()
    while True:
        response = get_input("Y, N")
        if response == "y":
            time.sleep(1)
            result = run_battle(player_character, spawned_demon)
            if result == "victory":
                reward = random.randint(2, 10)  # Generate a random number between 2 and 10
                print(
                    f"You kill {spawned_demon.name}!\n"
                    f"You find {reward} gold pieces!"
                )
                inventory["gold"] += reward  # Add the reward to the inventory
                total_victories += 1  # Update the victory counter by adding 1 to whatever it currently is at
                time.sleep(1)
                print("You find a Boomerang!")
                item_4 = Item(name="Boomerang", weight=2, defense=0)
                player_character.inventory.append(item_4)
                print("\n")
                player_character.print_inventory()
                return action_17
            elif result == "defeat":
                print(f"{spawned_demon.name} shatters your skull with a boomerang!")
                return action_exit
            else:
                print("You run through the door to the east.")
                return action_17
        elif response == "n":
            print("You run through the door to the east.")
            return action_17


def action_17():
    time.sleep(1)
    print("\n")
    print("You enter the east room(17).")
    print("There is a locked door to the north")
    print("You step into the room and a giant blue hand comes out of the wall.")
    print("It moves toward you and then disapears into the wall.")
    print("Do you proceed?")
    while True:
        response = get_input("Y, N")
        if response == "y":
            time.sleep(1)
            print("The hand covers your path and once again disappears into the wall.")
            print("Do you proceed?")
            response = get_input("Y, N")
            if response == "y":
                time.sleep(1)
                print("You move forward one block.")
                print("A pillar is to your right. Do you hide?")
                response = get_input("Y, N")
                if response == "y":
                    time.sleep(1)
                    print("A hand moves down the hallway and disappears.")
                    print("You move forward another block.")
                    print("A pillar is to your right. Do you hide?")
                    response = get_input("Y, N")
                    if response == "y":
                        print("A hand moves down the hallway and disappears.")
                        print("You move forward another block.")
                        print("A pillar is to your left. Do you hide?")
                        response = get_input("Y, N")
                        if response == "y":
                            time.sleep(1)
                            print("The giant blue hand grabs you and returns you")
                            print("to the beginning of the dungeon. You cry in shame.")
                            return action_2
                        elif response == "n":
                            time.sleep(1)
                            print("The door is locked.")
                            for item in player_character.inventory:
                                if item.name == "Key":
                                    print("Door was unlocked. You enter.")
                                    return action_18
                                print("You couldn't unlock the door.")
                                print("The giant blue hand grabs you and returns you")
                                print("to the beginning of the dungeon. You cry in shame.")
                                return action_2
                    elif response == "n":
                        time.sleep(1)
                        print("The giant blue hand grabs you and returns you")
                        print("to the beginning of the dungeon. You cry in shame.")
                        return action_2
                elif response == "n":
                    time.sleep(1)
                    print("The giant blue hand grabs you and returns you")
                    print("to the beginning of the dungeon. You cry in shame.")
                    return action_2
            elif response == "n":
                time.sleep(1)
                return action_17
        else:
            time.sleep(1)
            return action_17


def action_18():
    global total_deaths
    global total_victories
    time.sleep(1)
    print("\n")
    print("You enter the north room(18).")
    time.sleep(2)
    print("A robed man stands, blocking the only door out.")
    time.sleep(2)
    print("He slowly turns around and brushes back his hood.")
    time.sleep(2)
    print(f"Hello, {player_character.name}. I was hoping you'd make it this far.")
    time.sleep(2)
    print("A sinister smile spreads across his face and his body transforms.")
    time.sleep(2)
    print("His robe tears into pieces and wings sprout from his back.")
    time.sleep(2)
    print("A black dragon stands before you. He roars and shoots a fireball over your head.")
    time.sleep(2)
    print("Are you ready?")
    while True:
        response = get_input("Y, N")
        if response == "y":
            time.sleep(1)
            # Start the combat loop
            while player_character.health > 0 and Alistair.health > 0:
                # Display the current health of each character
                print(f"{player_character.name}'s health: {player_character.health}")
                print(f"{Alistair.name}'s health: {Alistair.health}")

        # Display the options to the player
                print("\n")
                print("What would you like to do?")
                choice = get_input("1: Attack \n2: Defend \n3: Run")

    # Handle the player's choice
                if choice == "1":
                    player_character.attack(Alistair)
                elif choice == "2":
                    player_character.defend()
                elif choice == "3":
                    if player_character.run():
                        print("Alistair cooks your body and eats you whole!")
                        return action_exit
                if random.random() <= 0.9:
                    Alistair.attack(player_character)
                else:
                    Alistair.defend()
            if Alistair.health == 0:
                reward = random.randint(2, 10)  # Generate a random number between 2 and 10
                print(
                    f"You kill Alistair!\n"
                    f"You find {reward} gold pieces!"
                )
                inventory["gold"] += reward  # Add the reward to the inventory
                total_victories += 1  # Update the victory counter by adding 1 to whatever it currently is at
                time.sleep(1)
                return action_19
        elif response == "n":
            print("You are a coward who deserves eternity in the dungeon!")
            sys.exit


def action_19():
    time.sleep(2)
    print("\nAs you cross into the room, you hear cries.")
    time.sleep(2)
    print("They get louder once they see you.")
    time.sleep(2)
    print("'Please save us!' a woman pleads.")
    time.sleep(2)
    print("It's the woman who paid you to save her son.")
    time.sleep(2)
    print("He's in her arms, shaking.")
    time.sleep(2)
    print("You untie them and lead them up a staircase toward the light.")
    time.sleep(2)
    print("You're blinded as you step out into the sun.")
    time.sleep(2)
    print("Once your vision returns,")
    time.sleep(2)
    print("you see Alistair's minions have turned to stone.")
    time.sleep(2)
    print("You have completed the quest and saved the village!")
    time.sleep(10)
    return action_exit


def action_exit():
    global inventory
    time.sleep(2)
    choice = get_input("Do you want to play again? [y/n]")
    if choice in ("y", "yes", "Y", "YES"):
        return None
    else:
        print(f"Bye, {name}! Here is a summary of your exploits:")
        print(f"Victories: {total_victories}")
        print(f"Defeats: {total_deaths}")
        gold = inventory["gold"]
        silver = inventory["silver"]
        weapon = inventory["weapon"]
        helmet = inventory["helmet"]
        accessory = inventory["accessory"]
        print(f"Gold: {gold}")
        print(f"Silver: {silver}")
        print(f"Weapon: {weapon}")
        print(f"Helmet: {helmet}")
        print(f"Accessory: {accessory}")
        sys.exit()

def get_input(text):
    response = input(f"{text}\n> ").lower().strip()
    while True:
        # response.lower() lowercases the value; .strip() removes leading/trailing spaces - that way if someone types
        # something like: "  show inventory" or " SHOW INVENtory  "   it'll all still work
        if response == "show inventory":
            for key, value in inventory.items():
                print(f"{key.title()}: {value}")
            response = input("> ")
        if response in ("quit", "q", "exit"):
            print("See you loser!")
            sys.exit()
        if response in ("backpack", "show backpack"):
            print_backpack()
            response = input("> ")
        if response in ("equip", ):
            print(" ")
            response = input("> ")
        else:
            return response


def run_battle(player, enemy):
    print("*" * 30)
    print(f"Combat: {player.name} vs {enemy.name}")
    print("*" * 30)
    round = 1
    while True:
        player.temp_defense = 0
        enemy.temp_defense = 0
        print("")
        print(f"Round {round}")
        print(f"{player.name} Health: {player.health}")
        print(f"{enemy.name} Health: {enemy.health}")
        choice = get_input("1: Attack \n2: Defend \n3: Run")
        if choice == "1":
            player.attack(enemy)
        elif choice == "2":
            player.defend()
        elif choice == "3":
            if player.run():
                print(f"{enemy.name} hacks you up into little bits!")
                return "defeat"
            else:
                return "draw"
        if not player.is_alive():
            return "defeat"
        if not enemy.is_alive():
            return "victory"

        print(f"{enemy.name} attacks!")
        if random.randint(0, 5) == 1:
            enemy.defend()
        else:
            enemy.attack(player)
        if not player.is_alive():
            return "defeat"
        if not enemy.is_alive():
            return "victory"

        round += 1


def event_loop():
    current_action = None
    while True:
        if current_action is None:
            # Starting the game for the first time - OR - starting a new round.
            player_character.health = 100
            current_action = action_1()
        else:
            current_action = current_action()


def main():
    print("\n")
    print(introduction)
    time.sleep(3)
    name = input("\nDo you remember your name?: ")
    player_character.name = name
    event_loop()


if __name__ == "__main__":
    main()
