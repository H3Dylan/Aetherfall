from abc import ABC, abstractmethod

class BattleCommand(ABC):
    @abstractmethod
    def execute(self, source, target):
        pass

class AttackCommand(BattleCommand):
    def execute(self, source, target):
        damage = source.strength - target.defense
        if damage < 1:
            damage = 1
        target.take_damage(damage)
        return f"{source.name} attacks {target.name} for {damage} damage!"

class DefendCommand(BattleCommand):
    def execute(self, source, target):
        source.is_defending = True
        return f"{source.name} assumes a defensive stance!"

class UseItemCommand(BattleCommand):
    def __init__(self, item):
        self.item = item

    def execute(self, source, target):
        self.item.use(target)
        return f"{source.name} uses {self.item.name}!"