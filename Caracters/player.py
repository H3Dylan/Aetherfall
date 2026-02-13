from Caracters.item import Weapon, Armor, Consumable
class Player:
    MAX_SLOT = 10

    def __init__(self, name):
        self.name = name
        self.player_class = None
        self.class_name = None

        self.hp = 0
        self.max_hp = 0

        self.stats = {}
        self.inventory = []

        self.equipped_weapon = None
        self.equipped_armor = None

    def set_class(self, class_object):
        self.player_class = class_object
        self.class_name = class_object.name

        self.max_hp = class_object.hp
        self.hp = class_object.hp

        self.stats = {
            "ATK": class_object.atk,
            "INT": class_object.intell,
            "VIT": class_object.vit,
            "DEF": class_object.def_phys,
            "DEFM": class_object.def_mag,
            "CRIT": class_object.crit
        }

        print(f"{self.name} est maintenant {self.class_name}")

    def set_weapon(self, weapon):
        if self.equipped_weapon:
            self.inventory.append(self.equipped_weapon)
        self.equipped_weapon = weapon
        self.inventory.remove(weapon)
        self.stats[weapon.stat_type]+= weapon.damage
        print("vous avez euquipe l'arme : " + self.equipped_weapon.name)

    def set_armor(self, armor):
        if self.equipped_armor:
            self.intenvory.append(self.equipped_armor)
        self.equipped_armor = armor
        self.inventory.remove(armor)
        self.stats["DEF"]+= armor.defence
        print("vous avez mis cette armure : " + self.equipped_armor.name)

    def add_to_inventory(self, item):
        if len(self.inventory) >= Player.MAX_SLOT:
            print("inventaire plein")
            return False

        self.inventory.append(item)
        print(f"{item.name} ajouté à l'inventaire.")
        return True
