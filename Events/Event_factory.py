# events/event_factory.py
import random
from Events_impl import RestEvent, CombatEvent, ChestEvent


class EventFactory:
    def createRandomEvent(self, zoneType):
        z = zoneType.lower()

        if z == "village":
            return RestEvent()

        if z == "forest":
            if random.random() < 0.6:
                return CombatEvent(random.choice(["Goblin", "Wolf"]))
            return ChestEvent()

        if z == "dungeon":
            return CombatEvent(random.choice(["Skeleton", "Dark Knight"]))

        return RestEvent()
