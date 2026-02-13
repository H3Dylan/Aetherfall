from Entities.Character import Character
import random

class Enemy(Character):
    def __init__(self, name, hp, strength, defense, type_enemy):
        super().__init__(name, hp, strength, defense)
        self.type = type_enemy

    def choose_action(self):
        chance = random.randint(1, 10)
        if chance <= 8:
            return "Attack"
        else:
            return "Defend"