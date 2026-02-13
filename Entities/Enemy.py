from Entities.Character import Character
import random

class Enemy(Character):
    def __init__(self, name, hp, stats, enemy_type):
        super().__init__(name, hp, stats)
        self.type = enemy_type

    def choose_action(self, target):
        if random.random() < 0.8:
            damage = self.stats.get('str', 5)
            return ("attack", damage)
        else:
            return ("wait", 0)