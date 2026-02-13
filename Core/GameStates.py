from Combat.BattleCommand import AttackCommand, DefendCommand, SkillCommand

class ExplorationState:
    def __init__(self, game_engine):
        self.engine = game_engine

    def update(self):
        zone = self.engine.current_zone
        print(f"\n--- LIEU : {zone.name} ---")
        print("1. Explorer (Lancer un événement)")
        print("2. Voyager (Changer de zone)")
        print("3. Voir mes Stats")
        print("4. Quitter le jeu")
        print("5. affiche ton inventaire")
        print("6. ajouter un item, fais gaffe c'est de la triche")
        choice = input("Que voulez-vous faire ? > ")

        if choice == "1":
            try:
                event = zone.explore()
                event.trigger(self.engine)
            except Exception as e:
                print(f"Erreur d'exploration : {e}")
        
        elif choice == "2":
            self.choose_travel_destination()

        elif choice == "3":
            self.engine.ui.display_status(self.engine.player)
            
        elif choice == "4":
            print("Au revoir !")
            self.engine.running = False
        elif choice == "5":
            self.engine.ui.display_inventory(self.engine.player)
        elif choice == "6":
            item_name = input("Nom de l'item à ajouter > ")
            fake_item = type('FakeItem', (object,), {'name': item_name})
            self.engine.player.add_to_inventory(fake_item)
        else:
            print("Choix invalide.")

    def choose_travel_destination(self):
        print("\n--- CARTE DU MONDE ---")
        zones_names = list(self.engine.all_zones.keys())
        
        for i, name in enumerate(zones_names):
            print(f"{i+1}. {name}")
            
        try:
            choix = int(input("Aller vers > ")) - 1
            if 0 <= choix < len(zones_names):
                target_name = zones_names[choix]
                target_zone = self.engine.all_zones[target_name]
                if target_zone.canEnter(self.engine.player):
                    self.engine.change_zone(target_zone)
                else:
                    print("Accès refusé (Il vous manque la Clé !)")
            else:
                print("Zone inexistante.")
        except ValueError:
            print("Entrée incorrecte.")

class CombatState:
    def __init__(self, game_engine, enemy):
        self.engine = game_engine
        self.combat_system = game_engine.combat_system
        self.combat_system.start_combat(enemy)

    def update(self):
        if self.engine.player.is_dead():
            print("--- GAME OVER ---")
            self.engine.running = False
            return
            
        if self.combat_system.enemy.is_dead():
            print(f"--- VICTOIRE FINALE ! {self.combat_system.enemy.name} est tombé ! ---")
            
            if self.combat_system.enemy.type == "Boss":
                print("Félicitations ! Vous avez libéré Aetherfall de l'emprise du vide.")
                print("FIN DU JEU")
                self.engine.running = False
            else:
                print("Appuyez sur Entrée pour continuer...")
                self.engine.change_state(ExplorationState(self.engine))
            return
        
        print(f"\n--- TOUR DE {self.engine.player.name} ---")
        print(f"PV Joueur: {self.engine.player.hp}/{self.engine.player.max_hp} | Ennemi: {self.combat_system.enemy.hp}")
        print("1. Attaquer")
        print("2. Défendre")
        print("3. Compétence Spéciale 1")
        print("4. Compétence Spéciale 2")

        choice = input("Votre choix > ")

        command = None
        if choice == "1":
            command = AttackCommand()
        elif choice == "2":
            command = DefendCommand()
        elif choice == "3":
            command = SkillCommand(1)
        elif choice == "4":
            command = SkillCommand(2)
        else:
            print("Choix invalide, vous perdez votre tour !")
            command = DefendCommand()

        self.combat_system.play_turn(command)