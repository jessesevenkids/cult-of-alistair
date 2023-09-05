import random
import math

from rad_alistair import constants


class Item:

    def __init__(self, name, weight, defense):
        self.name = name
        self.weight = weight
        self.defense = defense

    def __str__(self):
        return f"{self.name}: Weight: {self.weight}  -  Defense: {self.defense}"

    def __repr__(self):
        return self.__str__()


class Helmet:
    def __init__(self, name, weight, defense):
        self.name = name
        self.weight = weight
        self.defense = defense

    def __str__(self):
        return f"{self.name}: Weight: {self.weight}  -  Defense: {self.defense}"

    def __repr__(self):
        return self.__str__()


class BaseArmor:
    def __init__(self, name, weight, defense):
        self.name = name
        self.weight = weight
        self.defense = defense

    def __str__(self):
        return f"{self.name}: Weight: {self.weight}  -  Defense: {self.defense}"

    def __repr__(self):
        return self.__str__()

    @classmethod
    def new(cls):
        """Generate a new piece of armor."""
        item_type = cls.__name__
        if item_type == "HeadArmor":
            item_name = "Helmet"
            base_weight = 2
            base_defense = 3
        elif item_type == "ChestArmor":
            item_name = "Armor"
            base_weight = 5
            base_defense = 10
        elif item_type == "WaistArmor":
            item_name = "Belt"
            base_weight = 1
            base_defense = 2
        elif item_type == "LegArmor":
            item_name = "Leg Armor"
            base_weight = 2
            base_defense = 4
        elif item_type == "FeetArmor":
            item_name = "Boots"
            base_weight = 2
            base_defense = 3
        else:
            item_name = item_type
            base_weight = 2
            base_defense = 2

        # First there is approximately an 80% chance that it will be a crappy item
        is_crappy = random.randint(0, 10) <= 8
        if not is_crappy:
            # It's not crappy, but now there is a 10% chance that it will be elite
            is_elite = random.randint(0, 10) == 10
            if is_elite:
                adjective_idx = random.randint(0, len(constants.EXOTIC_ADJ) - 1)
                adjective = constants.EXOTIC_ADJ[adjective_idx]
                adjective = adjective.title()  # Make sure it's capitalized
                final_name = f"{adjective} {item_name}"

                # Elite items are nice and lightweight; up to 50% lighter
                weight_mod = random.randint(5, 10)
                weight = math.floor((weight_mod / 10) * base_weight)  # round down

                # Elite defense is up to 2x higher than base
                defense_mod = math.ceil((base_defense * random.randint(20, 100)) / 100)
                defense = base_defense + defense_mod
            else:
                adjective_idx = random.randint(0, len(constants.POSITIVE_ADJ) - 1)
                adjective = constants.POSITIVE_ADJ[adjective_idx]
                adjective = adjective.title()  # Make sure it's capitalized
                final_name = f"{adjective} {item_name}"

                # Non-crappy (but not elite) items should be + or - 30 percent of base weight
                heavier = random.randint(1, 2) == 1
                weight_mod = math.floor(base_weight * (random.randint(0, 30) / 100))  # math.floor == round down
                if heavier:
                    weight = base_weight + weight_mod
                else:
                    weight = base_weight - weight_mod

                # Non-crappy (but not elite) items should be + or - 30 percent of base defense
                stronger = random.randint(1, 2) == 1
                defense_mod = math.ceil(base_defense * (random.randint(0, 30) / 100))  # math.ceil == round up
                if stronger:
                    defense = base_defense + defense_mod
                else:
                    defense = base_defense - defense_mod

        else:
            adjective_idx = random.randint(0, len(constants.NEGATIVE_ADJ) - 1)
            adjective = constants.NEGATIVE_ADJ[adjective_idx]
            adjective = adjective.title()  # Make sure it's capitalized
            final_name = f"{adjective} {item_name}"

            # Crappy items are up to 40% heavier than their base weight
            weight_mod = round(base_weight * (random.randint(0, 30) / 100))
            weight = base_weight + weight_mod

            # Crappy items provide up to 40% less defense
            defense_mod = round(base_defense * (random.randint(0, 40) / 100))
            defense = base_defense - defense_mod
        return cls(final_name, weight, defense)


class HeadArmor(BaseArmor):

    def __init__(self, name, weight, defense):
        self.name = name
        self.weight = weight
        self.defense = defense

    def __str__(self):
        return f"{self.name}: Weight: {self.weight}  -  Defense: {self.defense}"

    def __repr__(self):
        return self.__str__()


class ChestArmor(BaseArmor):

    def __init__(self, name, weight, defense):
        self.name = name
        self.weight = weight
        self.defense = defense

    def __str__(self):
        return f"{self.name}: Weight: {self.weight}  -  Defense: {self.defense}"

    def __repr__(self):
        return self.__str__()


class WaistArmor(BaseArmor):

    def __init__(self, name, weight, defense):
        self.name = name
        self.weight = weight
        self.defense = defense

    def __str__(self):
        return f"{self.name}: Weight: {self.weight}  -  Defense: {self.defense}"

    def __repr__(self):
        return self.__str__()


class LegArmor(BaseArmor):

    def __init__(self, name, weight, defense):
        self.name = name
        self.weight = weight
        self.defense = defense

    def __str__(self):
        return f"{self.name}: Weight: {self.weight}  -  Defense: {self.defense}"

    def __repr__(self):
        return self.__str__()


class FeetArmor(BaseArmor):

    def __init__(self, name, weight, defense):
        self.name = name
        self.weight = weight
        self.defense = defense

    def __str__(self):
        return f"{self.name}: Weight: {self.weight}  -  Defense: {self.defense}"

    def __repr__(self):
        return self.__str__()


class Accessory:
    def __init__(self, name, weight, defense):
        self.name = name
        self.weight = weight
        self.defense = defense

    def __str__(self):
        return f"{self.name}: Weight: {self.weight}  -  Defense: {self.defense}"

    def __repr__(self):
        return self.__str__()


class Weapon:
    def __init__(self, name, weight, attack):
        self.weight = weight
        self.attackPower = attack
        self.name = name

    def __str__(self):
        return f"{self.name}: Weight: {self.weight}  -  Attack: {self.attackPower}"

    def __repr__(self):
        return self.__str__()
