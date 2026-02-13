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

    def ask_input(self, prompt):
        return input(f"{prompt} > ")