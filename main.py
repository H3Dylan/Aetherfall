import sys

from Core.GameEngine import GameEngine
from Core.GameStates import ExplorationState
from UI.UIConsole import ConsoleUI

from Caracters.player import Player
from Caracters.classe import FactoryClass
from World.Village import Village
from World.Forest import Forest
from World.Dungeon import Dungeon
from Events.EventFactory import EventFactory

def main():
    print("==========================================")
    print("        ⚔️  AETHERFALL : ORIGINS  ⚔️      ")
    print("==========================================")

    engine = GameEngine()
    ui = ConsoleUI()

    print("\n--- CRÉATION DU HÉROS ---")
    name = ui.ask_input("Quel est votre nom, aventurier ?")
    player = Player(name)

    print(f"Bienvenue {name}. Choisissez votre destin :")
    print("1. Guerrier (Fort et Résistant)")
    print("2. Mage (Intelligent et Magique)")
    print("3. Voleur (Rapide et Critique)")
    
    choice = input("Votre choix (nom ou numéro) > ").lower()

    class_map = {"1": "guerrier", "2": "mage", "3": "voleur"}
    if choice in class_map:
        choice = class_map[choice]

    try:
        player_class = FactoryClass.create_class(choice)
        player.set_class(player_class)
    except Exception as e:
        print(f"Choix invalide ({e}). Vous serez un Guerrier par défaut.")
        player.set_class(FactoryClass.create_class("guerrier"))

    evt_factory = EventFactory()
    
    village = Village(evt_factory)
    forest = Forest(evt_factory)
    dungeon = Dungeon(evt_factory)

    engine.all_zones = {
        "Village": village,
        "Forêt": forest,
        "Donjon": dungeon
    }

    engine.setup(player=player, start_zone=village, ui=ui)

    print("\nLancement du jeu...")
    engine.change_state(ExplorationState(engine))

    engine.run()

if __name__ == "__main__":
    main()