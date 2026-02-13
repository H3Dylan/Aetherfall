class Player:
    MAX_slot = 10

    def __init__(self, name, HP,ATK,INT,VIT,DEF,DEFM,CRIT):
        self.name = name
        self.hp = HP
        self.stats = {
            "ATK": ATK,
            "INT": INT,
            "VIT": VIT,
            "DEF": DEF,
            "DEFM": DEFM,
            "CRIT": CRIT
        }
        self.inventory = []
        self.equipped_weapon = None
        self.equipped_armor = None
    
    def set_class(self, player_class):
        self.player_class = player_class
        print(f"{self.name} a choisi la classe : {player_class}")
        
    def set_weapon(self, weapon):
        self.equipped_weapon = weapon
        print(f"{self.name} a équipé l'arme : {weapon.name}")
    
    def set_armor(self, armor):
        self.equipped_armor = armor
        print(f"{self.name} a équipé l'armure : {armor.name}")
    
    def set_class(self, player_class):
        self.player_class = player_class
        print(f"{self.name} a choisi la classe : {player_class}")
    
    def add_to_inventory(self, item):
        if len(self.inventory)>= Player.MAX_slot:
            print("inventaire plein")
            return False
        else :
            self.inventory.append(item)
            print(f"{item} ajouter à votre inventaire")
    