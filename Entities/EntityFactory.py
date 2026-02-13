from Entities.Enemy import Enemy

class EntityFactory:

    @staticmethod
    def create_enemy(enemy_type):
        # Mouchard pour savoir si on est dans le bon fichier
        print(f"[DEBUG FACTORY] Reçu demande pour : '{enemy_type}'")
        
        t = str(enemy_type).lower().strip()

        if t == "wolf":
            return Enemy("Loup Enragé", 30, 4, 1, "Beast")

        elif t == "goblin":
            return Enemy("Gobelin", 45, 6, 2, "Humanoid")

        elif t == "skeleton":
            return Enemy("Squelette", 40, 5, 3, "Undead")
        
        elif t == "dark knight":
            return Enemy("Chevalier Noir", 80, 10, 5, "Elite")

        elif t == "boss":
            return Enemy("LE GARDIEN DU VIDE (BOSS)", 200, 15, 8, "Boss")
            
        else:
            print(f"[DEBUG FACTORY] ERREUR : '{t}' inconnu !")
            return None