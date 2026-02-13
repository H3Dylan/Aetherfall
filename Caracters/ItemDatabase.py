from Caracters.item import Weapon, Armor, Consumable

class Epee(Weapon):
    def __init__(self):
        super().__init__("épée", "une épée en acier (on se fait chier)", "ATK", 10)
class Armure_cuir(Armor):
    def __init__(self):
        super().__init__("armure en cuir", "une armur en cuir , armure de base", 5)
class Hache(Weapon):
    def __init__(self):
        super().__init__("hache","une hache en diamand ","ATK",20)
class Slip(Armor):
    def __init__(self):
        super().__init__("Le slip", "vazy met toi tous nu ca va plus vite", 1)
class Armure_fer(Armor):
    def __init__(self):
        super().__init__("armure en fer", "une armure en fer pour riche", 10)
class Baton(Weapon):
    def __init__(self):
        super().__init__("baton","un baton en bois classique","INT",15)
class SuperBatonDeRichesse(Weapon):
    def __init__(self):
        super().__init__("Super Baton de richesse","ancien baton qui aurrait appartenue a Benichou le gobelin", "INT", 40)
class PotionSoin(Consumable):
    def __init__(self):
        super().__init__("potion de soin", "une potion qui soigne 20 points de vie", 30, "heal")
class Grenade(Consumable):
    def __init__(self):
        super().__init__("grenade", "SA VA PETER", 40, "damage")
class ItemFactory:
    @staticmethod
    def create_item(item_type):
        item_type = item_type.lower()
        if item_type == "epee":
            return Epee()
        elif item_type == "armure_cuir":
            return Armure_cuir()
        elif item_type == "hache":
            return Hache()
        elif item_type == "armure_fer":
            return Armure_fer()
        elif item_type == "baton":
            return Baton()
        elif item_type == "superbatonderichesse":
            return SuperBatonDeRichesse()
        elif item_type == "potionsoin":
            return PotionSoin()
        elif item_type == "grenade":
            return Grenade()
        elif item_type == "slip":
            return Slip()
        else:
            print("Type d'item inconnu")
            return None