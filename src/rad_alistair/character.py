import random
from rad_alistair.item import HeadArmor, ChestArmor, WaistArmor, LegArmor, FeetArmor


class Character:
    def __init__(self, name, health, attackPower, defense):
        self.name = name
        self.health = health
        self.base_attack = attackPower
        self.base_defense = defense
        self.temp_defense = 0

        # Equipment slots
        self.lhand = None
        self.rhand = None
        self.head = None
        self.chest = None
        self.waist = None
        self.legs = None
        self.feet = None
        self.accessory = None
        self.accessory2 = None

        self.ability = []
        # Inventory
        self.inventory = []
    
    def has_key(self):
        for item in self.inventory:
            if item.name.lower() == "key":
                return True
        return False

    def print_inventory(self):
        max_len = 9
        for item in self.inventory:
            item_len = len(item.name)
            if item_len > max_len:
                max_len = item_len

        column = max_len + 4
        print("=" * column)
        title = "Inventory".center(max_len)
        print(f"| {title} |")
        print("=" * column)

        for item in self.inventory:
            centered_item = item.name.center(column)
            print(centered_item)
        print("=" * column)

    def print_equiped(self):
        if self.lhand:
            print(f"Left Hand: {self.lhand.name}")
        else:
            print("Left Hand: <empty>")

    def equip_head(self, item):
        if isinstance(item, HeadArmor):
            self.chest = item
        else:
            print(f"Sorry, {item} cannot be equipt to your head.")

    def equip_chest(self, item):
        if isinstance(item, ChestArmor):
            self.chest = item
        else:
            print(f"Sorry, {item} cannot be equipt to your chest.")

    def equip_waist(self, item):
        if isinstance(item, WaistArmor):
            self.chest = item
        else:
            print(f"Sorry, {item} cannot be equipt to your Waist.")

    def equip_legs(self, item):
        if isinstance(item, LegArmor):
            self.chest = item
        else:
            print(f"Sorry, {item} cannot be equipt to your legs.")

    def equip_feet(self, item):
        if isinstance(item, FeetArmor):
            self.chest = item
        else:
            print(f"Sorry, {item} cannot be equipt to your feet.")

    @property
    def defense(self):
        total = self.base_defense
        if self.lhand:
            total += getattr(self.lhand, "defense", 0)
        if self.rhand:
            total += getattr(self.rhand, "defense", 0)
        if self.accessory:
            total += getattr(self.accessory, "defense", 0)
        if self.accessory2:
            total += getattr(self.accessory2, "defense", 0)
        if self.head:
            total += self.head.defense
        if self.chest:
            total += self.chest.defense
        if self.waist:
            total += self.waist.defense
        if self.legs:
            total += self.legs.defense
        if self.feet:
            total += self.feet.defense
        if self.accessory:
            total += self.accessory.defense
        if self.accessory2:
            total += self.accessory2.defense
        return total

    @property
    def attackPower(self):
        total = self.base_attack
        if self.head:
            total += getattr(self.head, "attackPower", 0)
        if self.chest:
            total += getattr(self.chest, "attackPower", 0)
        if self.waist:
            total += getattr(self.waist, "attackPower", 0)
        if self.legs:
            total += getattr(self.legs, "attackPower", 0)
        if self.feet:
            total += getattr(self.feet, "attackPower", 0)
        if self.accessory:
            total += getattr(self.accessory, "attackPower", 0)
        if self.accessory2:
            total += getattr(self.accessory2, "attackPower", 0)
        if self.lhand:
            total += self.lhand.attackPower
        if self.rhand:
            total += self.rhand.attackPower
        if self.head:
            total += self.head.attackPower
        if self.chest:
            total += self.chest.attackPower
        if self.waist:
            total += self.waist.attackPower
        if self.legs:
            total += self.legs.attackPower
        if self.feet:
            total += self.feet.attackPower
        if self.accessory:
            total += self.accessory.attackPower
        if self.accessory2:
            total += self.accessory2.attackPower
        return total

    def attack(self, enemy):
        print(f"{self.name} attacks {enemy.name}!")
        try:
            chance = enemy.defense * 20 / self.attackPower
        except Exception:
            chance = 0

        if chance == 0:
            block = False
        else:
            block = random.randint(0, 100) <= chance

        if block:
            print(f"{enemy.name} blocks the attack!")
        else:
            attack_percent = random.randint(80, 120)
            attack = int(self.attackPower - self.defense)
            attack += round(attack_percent * self.attackPower / 100)
            print(f"{self.name} strikes with {attack}")
            enemy.health -= attack
            if enemy.health < 0:
                enemy.health = 0
            print(f"{enemy.name}'s health is now {enemy.health}.")

    def defend(self):
        print(f"{self.name} defends against the enemy attack.")
        self.temp_defense = 10

    def pray(self):
        print(f"{self.name} You pray to Thor Odinson!.")
        self.health += 20
        print(f"{self.name}'s health is now {self.health}.")


    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def run(self):
        if random.random() <= 0.99:
            print(f"{self.name} successfully flees from the enemy!")
            return True
        else:
            print(f"{self.name} fails to flee from the enemy!")
            return False


def spawn_skeleton():
    # 1 in 100 chance of special skeleton
    if random.randint(1, 100) == 1:
        name = "Elite Skeleton"
        health = random.randint(80, 300)
        attack = random.randint(10, 40)
        defense = random.randint(5, 30)
        skeleton = Character(name, health, attack, defense)
        skeleton.equip_head(HeadArmor.new())
        skeleton.equip_chest(ChestArmor.new())
        skeleton.equip_legs(LegArmor.new())
        skeleton.equip_feet(FeetArmor.new())
    else:
        name = "Skeleton"
        health = random.randint(40, 80)
        attack = random.randint(5, 15)
        defense = random.randint(1, 10)
        skeleton = Character(name, health, attack, defense)
    return skeleton


def spawn_bat():
    # 1 in 100 chance of special bat
    if random.randint(1, 100) == 1:
        name = "Mongrel Bat"
        health = random.randint(40, 100)
        attack = random.randint(5, 30)
        defense = random.randint(5, 15)
    else:
        name = "Bat"
        health = random.randint(10, 25)
        attack = random.randint(4, 10)
        defense = random.randint(1, 3)
    return Character(name, health, attack, defense)


def spawn_demon():
    # 1 in 100 chance of special demon
    if random.randint(1, 100) == 1:
        name = "Shiny Demon"
        health = random.randint(80, 300)
        attack = random.randint(15, 40)
        defense = random.randint(5, 30)
        demon = Character(name, health, attack, defense)
        demon.equip_head(HeadArmor.new())
        demon.equip_chest(ChestArmor.new())
        demon.equip_legs(LegArmor.new())
        demon.equip_feet(FeetArmor.new())
    else:
        name = "Demon"
        health = random.randint(60, 100)
        attack = random.randint(10, 20)
        defense = random.randint(3, 8)
        demon = Character(name, health, attack, defense)
    return demon


def spawn_enemy():
    val = random.randint(1, 11)
    if val in (1, 2):
        return spawn_demon()
    if val in (3, 4, 5):
        return spawn_skeleton()
    else:
        return spawn_bat()
