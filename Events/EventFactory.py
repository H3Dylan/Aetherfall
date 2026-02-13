import random
from Events.EventsImpl import RestEvent, CombatEvent, ChestEvent


class EventFactory:
    def createRandomEvent(self, zoneType):
        z = zoneType.lower()

        if z == "village":
            return RestEvent()

        if z == "forest":
            if random.random() < 0.6:
                return CombatEvent(random.choice(["goblin", "wolf"]))
            return ChestEvent()

        if z == "dungeon":
            return CombatEvent(random.choice(["skeleton", "dark knight"]))

        return RestEvent()
