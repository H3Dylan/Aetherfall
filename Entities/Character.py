from abc import ABC, abstractmethod

class Character(ABC):

    def __init__(self, name, hp, strength, defense):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.strength = strength
        self.defense = defense
        self.status_effects = []

    def take_damage(self, amount):

        real_damage = amount - self.defense

        if real_damage > 0:
            self.hp = self.hp - real_damage
            print(f"{self.name} perd {real_damage} PV !")
        else:
            print(f"{self.name} encaisse le coup (0 dégât) !")

    def heal(self, amount):
        self.hp = self.hp + amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        print(f"{self.name} récupère {amount} PV.")

    def is_dead(self):
        if self.hp <= 0:
            return True
        else:
            return False

    def add_status(self, effect):
        self.status_effects.append(effect)
        print(f"{self.name} est affecté par {effect.name} !")