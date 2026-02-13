from Entities.Enemy import Enemy

class EntityFactory:

    @staticmethod
    def create_enemy(enemy_type):
        enemy_type = enemy_type.lower()   
        if enemy_type == "loup":
            return Enemy("Loup Sauvage", hp=30, stats={'str': 4, 'def': 1, 'spd': 10}, enemy_type="Wolf", xp_reward=20)          
        elif enemy_type == "bandit":
            return Enemy("Bandit", hp=45, stats={'str': 6, 'def': 2, 'spd': 5}, enemy_type="Humanoid", xp_reward=35)         
        elif enemy_type == "squelette":
            return Enemy("Squelette", hp=40, stats={'str': 5, 'def': 5, 'spd': 2}, enemy_type="Undead", xp_reward=40)           
        elif enemy_type == "champion":
            return Enemy("Champion Corrompu", hp=80, stats={'str': 10, 'def': 6, 'spd': 4}, enemy_type="Elite", xp_reward=100)            
        elif enemy_type == "boss":
            return Enemy("Gardien du Donjon", hp=200, stats={'str': 15, 'def': 10, 'spd': 5}, enemy_type="Boss", xp_reward=500)          
        else:
            raise ValueError(f"Type d'ennemi inconnu : {enemy_type}")