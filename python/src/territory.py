from src.units import Nothing


class Territory:
    @classmethod
    def new_land(cls, name):
        return cls(name, is_sea=False)

    @classmethod
    def new_sea(cls, name):
        return cls(name, is_sea=True)

    def __init__(self, name, is_sea):
        self._name = name
        self._is_sea = is_sea

        self._neighbors = set()
        self._unit = Nothing()

    def name(self):
        return self._name

    def neighbors(self):
        return self._neighbors

    def add_neighbor(self, new_neighbor):
        self._neighbors.add(new_neighbor)

    def unit(self):
        return self._unit

    def add_unit(self, unit):
        self._unit = unit

    def remove_unit(self):
        self._unit = Nothing()

    def commanded_by(self):
        return self._unit.commander()

    def is_land(self):
        return not self._is_sea

    def is_sea(self):
        return self._is_sea
