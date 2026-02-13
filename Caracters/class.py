import abc
from Entities.Character import Character
class ClassPlayer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self, HP, ATK, INT, VIT, DEF, DEFM, CRIT):
        pass

class Guerrier:
    def __init__(HP, ATK, INT, VIT, DEF, DEFM, CRIT):
        HP = 120
        ATK = 15
        INT = 5
        VIT = 6
        DEF = 10
        DEFM = 5
        CRIT = 5
    def Coup_puissant(self, ATK):
        return ATK + 10
    def ChargeSuicidaire(self, ATK, HP):
        HP -= 20
        if HP <= 0:
           return "Vous êtes mort"
        return ATK *1.5 + 10

class Mage:
    def __init__(self, HP, ATK, INT, VIT, DEF, DEFM, CRIT):
        self.HP = 80
        self.ATK = 6
        self.INT = 20
        self.VIT = 4
        self.DEF = 5
        self.DEFM = 10
        self.CRIT = 5
    def Boule_de_feu(self, INT):
        return INT + 15
    def Heal(self, INT, HP):
        HP += 25
        return HP
    
class Voleur:
    def __init__(self, HP, ATK, INT, VIT, DEF, DEFM, CRIT):
        self.HP = 100
        self.ATK = 11
        self.INT = 10
        self.VIT = 12
        self.DEF = 7
        self.DEFM = 7
        self.CRIT = 35
    def Attaque_sournoise(self, ATK):
        return ATK + 5
    def Frappe_critique(self, ATK, CRIT):
        if CRIT >= 10:
            return ATK * 2
        return ATK + 5
    
class FactoryClass:
    @staticmethod
    def create_class(class_type):
        class_type = class_type.lower()
        if class_type == "guerrier":
            return Guerrier(120, 15, 5, 6, 10, 5, 5)
        elif class_type == "mage":
            return Mage(80, 6, 20, 4, 5, 10, 5)
        elif class_type == "voleur":
            return Voleur(100, 11, 10, 12, 7, 7, 35)
        else:
            raise ValueError(f"Type de classe inconnu : {class_type}")
    
