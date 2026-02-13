from UI.UIObserver import UIObserver
import sys

class ConsoleUI(UIObserver):
    def display_message(self, message):
        print(f"[GAME] {message}")
    def display_status(self, player):
        print(f"\n--- {player.name} (HP: {player.hp}/{player.max_hp}) ---")
        if player.max_hp > 0:
            percent = int((player.hp / player.max_hp) * 10)
            bar = "█" * percent + "-" * (10 - percent)
            print(f"Health: [{bar}]")
        print("-------------------------------")
    def display_inventory(self, player):
        print("\n--- INVENTAIRE ---")
        if not player.inventory:
            print("Votre inventaire est vide.")
        else:
            for item in player.inventory:
                print(f"- {item.name} ({item.__class__.__name__})")
        print("------------------")
        print("---------- OBJET EQUIPE --------")
        if player.equipped_weapon:
            print(f"Arme : {player.equipped_weapon.name} (Dégâts: {player.equipped_weapon.damage})")
        else:
            print("Arme : Aucune")
        if player.equipped_armor:
            print(f"Armure : {player.equipped_armor.name} (Défense: {player.equipped_armor.defense})")
        else:
            print("Armure : Aucune")
        print("--------------)")
    def ask_input(self, prompt):
        return input(f"{prompt} > ")