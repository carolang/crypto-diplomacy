from src.player import Neutral


class Unit:
    def is_nothing(self):
        return False

    def is_army(self):
        return False

    def is_fleet(self):
        return False

    def commander(self):
        raise NotImplementedError("Subclass responsibility")


class Nothing(Unit):
    def is_nothing(self):
        return True

    def commander(self):
        return Neutral()


class Army(Unit):
    def __init__(self, being):
        super().__init__()
        self._commander = being

    def commander(self):
        return self._commander

    def is_army(self):
        return True


class Fleet(Unit):
    def __init__(self, being):
        super().__init__()
        self._commander = being

    def commander(self):
        return self._commander

    def is_fleet(self):
        return True
