import random


class Character:
    def __init__(self, name, health, attackPower, defense):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.defense = defense

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
        self.health += round(self.health * 0.10)
        print(f"{self.name}'s health is now {self.health}.")


    def pray(self):
        print(f"{self.name} You pray to Thor Odinson!.")
        self.health += round(self.health * 0.25)
        print(f"{self.name}'s health is now {self.health}.")


    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def run(self):
        if random.random() <= 0.5:
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
    else:
        name = "Skeleton"
        health = random.randint(40, 80)
        attack = random.randint(5, 15)
        defense = random.randint(1, 10)
    return Character(name, health, attack, defense)


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
        attack = random.randint(10, 40)
        defense = random.randint(5, 30)
    else:
        name = "Demon"
        health = random.randint(60, 100)
        attack = random.randint(10, 20)
        defense = random.randint(3, 8)
    return Character(name, health, attack, defense)


def spawn_enemy():
    val = random.randint(1, 11)
    if val in (1, 2):
        return spawn_demon()
    if val in (3, 4, 5):
        return spawn_skeleton()
    else:
        return spawn_bat()