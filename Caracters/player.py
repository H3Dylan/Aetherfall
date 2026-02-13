from Caracters.item import Weapon, Armor, Consumable

class Player:
    MAX_SLOT = 10

    def __init__(self, name):
        self.name = name
        self.player_class = None
        self.class_name = "Aventurier"
        self.hp = 100
        self.max_hp = 100
        self.stats = {"ATK": 10, "DEF": 5, "INT": 5, "VIT": 5, "DEFM": 5, "CRIT": 5}
        
        self.inventory = []
        self.equipped_weapon = None
        self.equipped_armor = None

        self.is_defending = False
        self.status_effects = []
        self.has_key = False

    @property
    def strength(self):
        return self.stats.get("ATK", 10)

    @property
    def defense(self):
        return self.stats.get("DEF", 5)

    def take_damage(self, amount):
        real_damage = max(0, amount - self.defense)
        self.hp -= real_damage
        print(f"{self.name} perd {real_damage} PV ! (Reste: {self.hp})")

    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)
        print(f"{self.name} se soigne de {amount} PV.")

    def is_dead(self):
        return self.hp <= 0

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
        if weapon in self.inventory:
            self.inventory.remove(weapon)
        self.stats[weapon.stat_type] += weapon.damage
        print("Vous avez équipé l'arme : " + self.equipped_weapon.name)

    def set_armor(self, armor):
        if self.equipped_armor:
            self.inventory.append(self.equipped_armor)
        self.equipped_armor = armor
        if armor in self.inventory:
            self.inventory.remove(armor)
        self.stats["DEF"] += armor.defense
        print("Vous avez équipé l'armure : " + self.equipped_armor.name)

    def add_to_inventory(self, item):
        if len(self.inventory) >= Player.MAX_SLOT:
            print("Inventaire plein")
            return False
        self.inventory.append(item)
        print(f"{item.name} ajouté à l'inventaire.")
        return True