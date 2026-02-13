import json
import os
import sys

# from Entities.Player import Player
# from World.Zone import Zone
# from UI.UIObserver import UIObserver

class GameEngine:
    def __init__(self):
        self.player = None
        self.current_zone = None
        self.inventory = []
        self.quest_status = 0
        self.current_state = None
        self.running = True

        self.ui = None

    def setup(self, player, start_zone, ui):
        self.player = player
        self.current_zone = start_zone
        self.ui = ui
        self.notify_ui("Moteur initialisé")

    def run(self):
        while self.running:
            if self.current_state:
                self.current_state.update(self)
            else:
                cmd = input(f"\n[{self.current_zone}] Que voulez-vous faire ? > ")
                self.handle_global_commands(cmd)

    def handle_global_commands(self, cmd):
        if cmd.lower() == "quit":
            self.running = False
            print("Fermeture du jeu...")
        elif cmd.lower() == "save":
            self.save_game()
        elif cmd.lower() == "load":
            self.load_game()
        else:
            print(f"Commande '{cmd}' non reconnue (État manquant).")

    def notify_ui(self, message):
        if self.ui:
            self.ui.display_message(message)
        else:
            print(f"[LOG] {message}")

    def save_game(self, filename="savegame.json"):
        if not self.player:
            print("Erreur: Pas de joueur à sauvegarder.")
            return

        data = {
            "quest_status": self.quest_status,
            "current_zone_name": self.current_zone if self.current_zone else "Village",
            "player": {
                "name": self.player.name,
                "hp": self.player.hp,
                "max_hp": self.player.max_hp,
                "class": getattr(self.player, "class_name", "Unknown") 
            },
            "inventory": [item.name for item in self.inventory]
        }
        
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
            self.notify_ui(f"Partie sauvegardée dans {filename} !")
        except Exception as e:
            self.notify_ui(f"Erreur de sauvegarde : {e}")

    def load_game(self, filename="savegame.json"):
        if not os.path.exists(filename):
            self.notify_ui("Aucun fichier de sauvegarde trouvé.")
            return

        try:
            with open(filename, 'r') as f:
                data = json.load(f)

            self.quest_status = data["quest_status"]

            p_data = data["player"]
            self.notify_ui(f"Chargement terminé. Retour de {p_data['name']} ({p_data['class']}).")
            
        except Exception as e:
            self.notify_ui(f"Fichier de sauvegarde corrompu : {e}")