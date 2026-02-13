# World/forest.py
from Zone import Zone

class Forest(Zone):
    def __init__(self, event_factory=None):
        super().__init__("Forêt", event_factory, "Forest")

    def explore(self):
        return super().explore()
