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
    
class SkillCommand(BattleCommand):
    def __init__(self, skill_number):
        self.skill_number = skill_number

    def execute(self, source, target):
        player_class = source.player_class 
        
        if self.skill_number == 1:
            damage = player_class.skill_one(source)
            if source.class_name == "Mage":
                return f"{source.name} utilise Boule de Feu / Soin !"
            
            target.take_damage(damage)
            return f"{source.name} lance sa compétence 1 et inflige {damage}!"
            
        elif self.skill_number == 2:
            damage = player_class.skill_two(source)
            if source.class_name == "Mage":
                 return f"{source.name} se soigne !"
            
            target.take_damage(int(damage) if isinstance(damage, (int, float)) else 0)
            return f"{source.name} lance sa compétence 2 !"