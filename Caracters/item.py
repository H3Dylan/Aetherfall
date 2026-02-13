class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return self.name

class Weapon(Item):
    def __init__(self, name, description, stat_type, damage):
        super().__init__(name, description)
        self.stat_type = stat_type 
        self.damage = damage

class Armor(Item):
    def __init__(self, name, description, defense):
        super().__init__(name, description)
        self.defense = defense

class Consumable(Item):
    def __init__(self, name, description, value, effect_type):
        super().__init__(name, description)
        self.value = value
        self.effect_type = effect_type

    def use(self, player):
        if self.effect_type == "heal":
            player.hp += self.value
            if player.hp > player.max_hp:
                player.hp = player.max_hp
            print(f"vous récupez {self.value} HP")

        elif self.effect_type == "damage":
            player.hp -= self.value
            print(f" vous subissez {self.value} degat")

        elif self.effect_type == "unlock":
            player.has_key = True
            print("Vous obtenez la clé du donjon !")

        else:
            print("item pas connue")
