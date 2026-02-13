import random
from Events import IGameEvent

class RestEvent(IGameEvent):
    def trigger(self, engine):
        engine.ui.displayMessage("Tu te reposes. Zone sûre.")
        if hasattr(engine.player, "hp") and hasattr(engine.player, "max_hp"):
            engine.player.hp = engine.player.max_hp
            engine.ui.displayMessage("PV restaurés.")


class CombatEvent(IGameEvent):
    def __init__(self, enemy_type):
        self.enemy_type = enemy_type

    def trigger(self, engine):
        engine.ui.displayMessage("Combat contre : " + self.enemy_type)

        if hasattr(engine, "combatSystem"):
            engine.combatSystem.startCombat()
        else:
            engine.ui.displayMessage("(CombatSystem pas encore branché)")


class ChestEvent(IGameEvent):
    def trigger(self, engine):
        engine.ui.displayMessage("Tu trouves un coffre...")

        # chance de drop la clé du donjon
        if random.random() < 0.35:
            engine.ui.displayMessage("Tu obtiens la Clé du Donjon !")

            if hasattr(engine.player, "setDungeonKey"):
                engine.player.setDungeonKey(True)
            else:
                engine.player.has_key = True
        else:
            engine.ui.displayMessage("Le coffre est vide.")
