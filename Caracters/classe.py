from abc import ABC, abstractmethod
from Caracters.ItemDatabase import ItemFactory
class ClassPlayer(ABC):
    def __init__(self, name, hp, atk, intell, vit, def_phys, def_mag, crit):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.intell = intell
        self.vit = vit
        self.def_phys = def_phys
        self.def_mag = def_mag
        self.crit = crit
       
    @abstractmethod
    def skill_one(self, player):
        pass

    @abstractmethod
    def skill_two(self, player):
        pass

class Guerrier(ClassPlayer):
    def __init__(self):
        super().__init__("Guerrier", 120, 15, 5, 6, 10, 5, 5)
    def skill_one(self, player):
        print("Coup puissant")
        return player.stats["ATK"] + 10
    def skill_two(self, player):
        print("Charge suicidaire")
        player.hp -= 20
        if player.hp <= 0:
            return "Vous êtes mort"
        return player.stats["ATK"] * 1.5 + 10    

class Mage(ClassPlayer):
    def __init__(self):
        super().__init__("Mage", 80, 6, 20, 4, 5, 10, 5)
    def skill_one(self, player):
        print("Boule de feu")
        return player.stats["INT"] + 15
    def skill_two(self, player):
        print("Heal")
        player.hp += 25
        return player.hp
    
class Voleur(ClassPlayer):
    def __init__(self):
        super().__init__("Voleur", 100, 11, 10, 12, 7, 7, 35)
    def skill_one(self, player):
        print("Attaque sournoise")
        return player.stats["ATK"] + 5
    def skill_two(self, player):
        print("Frappe critique")
        if player.stats["CRIT"] >= 10:
            return player.stats["ATK"] * 2
        return player.stats["ATK"] + 5
    
class FactoryClass:
    @staticmethod
    def create_class(class_type):
        class_type = class_type.lower()
        if class_type == "guerrier":
            return Guerrier()
        elif class_type == "mage":
            return Mage()
        elif class_type == "voleur":
            return Voleur()
        else:
            raise ValueError(f"Type de classe inconnu : {class_type}")
    def get_starting_weapon(self, class_type):
        class_type = class_type.lower()
        if class_type == "guerrier":
            return ItemFactory().create_item("hache")
        elif class_type == "mage":
            return ItemFactory().create_item("baton")
        elif class_type == "voleur":
            return ItemFactory().create_item("epee")
        else:
            raise ValueError(f"Type de classe inconnu : {class_type}")
    def get_starting_armor(self, class_type):
        class_type = class_type.lower()
        if class_type == "guerrier":
            return ItemFactory().create_item("armure_fer")
        elif class_type == "mage":
            return ItemFactory().create_item("slip")
        elif class_type == "voleur":
            return ItemFactory().create_item("armure_cuir")
        else:
            raise ValueError(f"Type de classe inconnu : {class_type}")
