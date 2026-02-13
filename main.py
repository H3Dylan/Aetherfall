from Core.GameEngine import GameEngine

def main():
    print("AETHERFALL")

    engine = GameEngine()

    class MockPlayer:
        def __init__(self):
            self.name = "Héros Test"
            self.hp = 100
            self.max_hp = 100
            self.class_name = "Warrior"
            
    engine.setup(player=MockPlayer(), start_zone="Village", ui=None)
    engine.run()

if __name__ == "__main__":
    main()