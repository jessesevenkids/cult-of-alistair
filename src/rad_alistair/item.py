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
        self.attack = attack
        self.name = name

    def __str__(self):
        return f"{self.name}: Weight: {self.weight}  -  Attack: {self.attack}"

    def __repr__(self):
        return self.__str__()