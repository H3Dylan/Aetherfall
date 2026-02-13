class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Weapon(Item):
    def __init__(self, name, description, type, damage):
        super().__init__(name, description)
        self.type = type
        self.damage = damage

class armor(Item):
    def __init__(self, name, description, type, defense):
        super().__init__(name, description)
        self.type = type
        self.defense = defense

class Consumable(Item):
    def __init__(self, name, description, value, effect):
        super().__init__(name, description, value)
        self.effect = effect
    def use(self): 
        return f"Vous utilisez {self.name} et {self.effect}"

class ContextItem:
    def __init__(self, strategy):
        self.strategy = strategy
    def use(self,strategy):
        print("vous utilisez : " + strategy.name)
        return strategy.use()
    def set_weapon_strategy(self, strategy):
        self.strategy = strategy
        print("vous avez équiper l'arme : " + self.strategy.name)
    def set_armor_strategy(self, strategy):
        self.strategy = strategy
        print("vous avez équiper l'armure : " + self.strategy.name)
    
arme = Weapon("épée", "une épée en acier", "ATK", 10)
armure = armor("armure en cuir", "une armure légère en cuir", "DEF", 5)
consommable = Consumable("potion de soin", "une potion qui soigne 20 points de vie", 50, "soigne 20 PV")
arme_context = ContextItem(arme)
armure_context = ContextItem(armure)
consommable_context = ContextItem(consommable)
arme_context.set_weapon_strategy(arme)
armure_context.set_armor_strategy(armure)
consommable_context.use(consommable)