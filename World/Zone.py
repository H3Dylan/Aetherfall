class Zone:
    def __init__(self, name, event_factory=None, zone_type="Zone"):
        self.name = name
        self.event_factory = event_factory
        self.zone_type = zone_type

    def canEnter(self, player):
        return True

    def explore(self):
        if self.event_factory is None:
            raise Exception("EventFactory not set")
        return self.event_factory.createRandomEvent(self.zone_type)
