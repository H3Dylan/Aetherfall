from Zone import Zone

class Village(Zone):
    def __init__(self, event_factory=None):
        super().__init__("Village", event_factory, "Village")

    def explore(self):
        return super().explore()
