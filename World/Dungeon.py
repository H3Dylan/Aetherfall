# World/dungeon.py
from Zone import Zone

class Dungeon(Zone):
    def __init__(self, event_factory=None):
        super().__init__("Donjon", event_factory, "Dungeon")

    def canEnter(self, player):
        if hasattr(player, "hasDungeonKey"):
            return player.hasDungeonKey()

        if hasattr(player, "has_key"):
            return player.has_key is True

        return False
