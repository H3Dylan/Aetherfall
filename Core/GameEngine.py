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
            self.notify_ui("Impossible de sauvegarder : Aucun joueur.")
            return

        data = {
            "quest_status": self.quest_status,
            "current_zone_name": self.current_zone.name if self.current_zone else "Village",
            "player": {
                "name": self.player.name,
                "hp": self.player.hp,
                "max_hp": self.player.max_hp,
                "class": getattr(self.player, "class_name", "Aventurier"),
                "inventory_ids": [item.name for item in self.player.inventory] 
            }
        }
        
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
            self.notify_ui(f"Partie sauvegardée avec succès dans '{filename}'.")
        except Exception as e:
            self.notify_ui(f"Erreur critique lors de la sauvegarde : {e}")

    def load_game(self, filename="savegame.json"):
        if not os.path.exists(filename):
            self.notify_ui("Aucun fichier de sauvegarde trouvé.")
            return

        try:
            with open(filename, 'r') as f:
                data = json.load(f)

            self.quest_status = data["quest_status"]

            p_data = data["player"]
            if self.player:
                self.player.name = p_data["name"]
                self.player.hp = p_data["hp"]
                self.player.max_hp = p_data["max_hp"]
                self.notify_ui(f"Restauration de {self.player.name} (PV: {self.player.hp}) terminée.")
            else:
                self.notify_ui("Erreur: Impossible de charger le joueur (Builder manquant).")

            saved_zone_name = data.get("current_zone_name")

            found_zone = None
            for key, zone in self.all_zones.items():
                if zone.name == saved_zone_name:
                    found_zone = zone
                    break

            if not found_zone and saved_zone_name in self.all_zones:
                found_zone = self.all_zones[saved_zone_name]

            if found_zone:
                self.current_zone = found_zone
                self.notify_ui(f"Retour dans la zone : {found_zone.name}")
            else:
                self.notify_ui(f"Zone sauvegardée '{saved_zone_name}' introuvable, on reste ici.")

        except Exception as e:
            self.notify_ui(f"Fichier de sauvegarde corrompu : {e}")