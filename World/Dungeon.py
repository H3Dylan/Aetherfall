from World.Zone import Zone
from Events.EventsImpl import BossEvent # Importe l'event du boss

class Dungeon(Zone):
    def __init__(self, event_factory=None):
        super().__init__("Donjon Noir", event_factory, "dungeon")

    def canEnter(self, player):
        return player.has_key

    def explore(self):
        return BossEvent()