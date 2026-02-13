from abc import ABC, abstractmethod

class Character(ABC):

    def __init__(self, name, hp, stats):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.stats = stats 
        self.status_effects = []

    def take_damage(self, amount):
        defense = self.stats.get('def', 0)
        actual_damage = max(0, amount - defense)
        
        self.hp -= actual_damage
        print(f"{self.name} prend {actual_damage} dégâts (Déf: {defense}). PV restants: {self.hp}/{self.max_hp}")
        
        if self.is_dead():
            print(f"{self.name} est mort !")

    def is_dead(self):
        return self.hp <= 0

    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)
        print(f"{self.name} soigne {amount} PV.")