class IGameEvent:
    def trigger(self, engine):
        raise NotImplementedError()
