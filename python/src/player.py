class Commander:
    def name(self):
        raise NotImplementedError("Subclass responsibility")


class Player(Commander):
    def __init__(self, name):
        self._name = name

    def name(self):
        return self._name


class Neutral(Commander):
    def name(self):
        return "NEUTRAL"
