class CombatSystem:
    def __init__(self, game_engine):
        self.engine = game_engine
        self.enemy = None
        self.turn_count = 0

    def start_combat(self, enemy):
        self.enemy = enemy
        self.turn_count = 1
        p = self.engine.player
        self.engine.notify_ui(f"--- COMBAT STARTED: {p.name} vs {self.enemy.name} ---")

    def play_turn(self, player_command):
        player = self.engine.player
        
        player.is_defending = False
        log_message = player_command.execute(player, self.enemy)
        self.engine.notify_ui(f"[Turn {self.turn_count}] {log_message}")

        if self.enemy.is_dead():
            self.engine.notify_ui(f"VICTORY! {self.enemy.name} has been defeated.")
            return False

        self.enemy.is_defending = False

        action_name = self.enemy.choose_action() 
        enemy_command = None
        
        if action_name == "Attack":
            from Combat.BattleCommand import AttackCommand
            enemy_command = AttackCommand()
        else:
            from Combat.BattleCommand import DefendCommand
            enemy_command = DefendCommand()

        log_enemy = enemy_command.execute(self.enemy, player)
        self.engine.notify_ui(f"[Enemy] {log_enemy}")

        if player.is_dead():
            self.engine.notify_ui("GAME OVER... You died.")
            return False

        self.turn_count += 1
        return True