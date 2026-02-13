from World.Zone import Zone

class Dungeon(Zone):
    def __init__(self, event_factory=None):
        super().__init__("Donjon", event_factory, "Dungeon")

    def canEnter(self, player):
        return player.has_key
