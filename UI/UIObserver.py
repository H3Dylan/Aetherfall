from abc import ABC, abstractmethod

class UIObserver(ABC):
    @abstractmethod
    def display_message(self, message):
        pass

    @abstractmethod
    def display_status(self, player):
        pass
 