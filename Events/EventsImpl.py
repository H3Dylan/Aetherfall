import random
from Events.IGameEvent import IGameEvent
from Core.GameStates import CombatState
from Entities.EntityFactory import EntityFactory

class RestEvent(IGameEvent):
    def trigger(self, engine):
        engine.notify_ui("Tu te reposes dans une zone sûre.")
        engine.player.heal(30)

class CombatEvent(IGameEvent):
    def __init__(self, enemy_name_from_colleague):
        self.enemy_name = enemy_name_from_colleague

    def trigger(self, engine):
        engine.notify_ui(f"ATTENTION ! Un {self.enemy_name} approche !")
        
        try:
            # 1. Nettoyage du nom
            target_name = self.enemy_name.lower().strip()
            print(f"[DEBUG] EventsImpl demande à la Factory : '{target_name}'")

            # 2. Création via la Factory
            enemy = EntityFactory.create_enemy(target_name)
            print(f"[DEBUG] La Factory a renvoyé : {enemy}")

            # 3. VÉRIFICATION CRITIQUE
            if enemy is None:
                print(f"[ERREUR] La Factory a renvoyé 'None' pour '{target_name}' !")
                print("[INFO] Création d'un Loup de secours pour éviter le crash.")
                enemy = EntityFactory.create_enemy("wolf") # Tentative de sauvetage

            # 4. Lancement du combat
            if enemy:
                engine.change_state(CombatState(engine, enemy))
            else:
                engine.notify_ui("L'ennemi s'est enfui (Bug de création).")

        except Exception as e:
            # On imprime l'erreur complète pour comprendre
            import traceback
            traceback.print_exc()
            engine.notify_ui(f"Erreur lancement combat : {e}")

class ChestEvent(IGameEvent):
    def trigger(self, engine):
        engine.notify_ui("Tu trouves un coffre...")
        if random.random() < 0.4:
            engine.notify_ui("Tu obtiens la Clé du Donjon !")
            engine.player.has_key = True
        else:
            engine.notify_ui("Il est vide.")