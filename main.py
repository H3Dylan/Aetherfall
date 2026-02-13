from Core.GameEngine import GameEngine
from Caracters.player import Player
from Caracters.classe import FactoryClass
from Caracters.item import Weapon, Armor, Consumable

def main():
    print("AETHERFALL")

    engine = GameEngine()

    name = input("entre ton nom de perso")
    class_choice = input("choisi ta classe (guerrier,mage,voleur)")

    player = Player(name)
    player_class = FactoryClass.create_class(class_choice)
    player.set_class(player_class)
            
    engine.setup(player=player, start_zone="Village", ui=None)
    engine.run()

if __name__ == "__main__":
    main()