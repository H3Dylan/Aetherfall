import json
import os
import sys

from Combat.CombatSystem import CombatSystem

class GameEngine:
    def __init__(self):
        self.player = None
        self.current_zone = None 
        self.inventory = []
        self.quest_status = 0
        
        self.combat_system = CombatSystem(self) 
        
        self.ui = None
        self.current_state = None
        self.running = True

        self.all_zones = {} 

    def setup(self, player, start_zone, ui):
        self.player = player
        self.current_zone = start_zone
        self.ui = ui
        self.notify_ui("Moteur Aetherfall Initialisé")

    def run(self):
        while self.running:
            if self.current_state:
                self.current_state.update()
            else:
                self.fallback_menu()

    def fallback_menu(self):
        z_name = self.current_zone.name if self.current_zone else "Zone Inconnue"
        cmd = input(f"\n[{z_name}] (Mode sans état) > ")
        self.handle_global_commands(cmd)

    def change_state(self, new_state):
        self.current_state = new_state

    def change_zone(self, new_zone):
        self.current_zone = new_zone
        self.notify_ui(f"Vous entrez dans : {new_zone.name}")

    def handle_global_commands(self, cmd):
        cmd = cmd.lower().strip()
        if cmd == "quit":
            self.running = False
            self.notify_ui("Fermeture du jeu...")
        elif cmd == "save":
            self.save_game()
        elif cmd == "load":
            self.load_game()
        else:
            self.notify_ui(f"Commande système '{cmd}' inconnue.")

    def notify_ui(self, message):
        if self.ui:
            self.ui.display_message(message)
        else:
            print(f"[Moteur] {message}")

    def save_game(self, filename="savegame.json"):
        if not self.player:
            return

        data = {
            "current_zone": self.current_zone.name,
            "player_data": self.player.get_save_data()
        }
        
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
            self.notify_ui("💾 Partie sauvegardée !")
        except Exception as e:
            self.notify_ui(f"Erreur sauvegarde : {e}")

    def load_game(self, filename="savegame.json"):
        if not os.path.exists(filename):
            self.notify_ui("Aucune sauvegarde trouvée.")
            return

        try:
            with open(filename, 'r') as f:
                data = json.load(f)

            p_data = data["player_data"]
            self.player.name = p_data["name"]
            self.player.hp = p_data["hp"]
            self.player.max_hp = p_data["max_hp"]
            self.player.class_name = p_data["class_name"]
            self.player.has_key = p_data["has_key"]
            self.player.stats = p_data["stats"]

            zone_name = data["current_zone"]
            if zone_name in self.all_zones:
                self.current_zone = self.all_zones[zone_name]
            
            self.notify_ui(f"Partie chargée ! Bienvenue {self.player.name}")
        except Exception as e:
            self.notify_ui(f"Erreur chargement : {e}")
