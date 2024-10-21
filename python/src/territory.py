from src.player import Neutral
from src.units import Nothing, Army, Fleet


class Territory:
    def __init__(self, name):
        self._name = name

        self._neighbors = set()
        self._unit = Nothing()
        self._commanded_by = Neutral()

    def name(self):
        return self._name

    def neighbors(self):
        return self._neighbors

    def add_neighbor(self, new_neighbor):
        self._neighbors.add(new_neighbor)

    def unit(self):
        return self._unit

    def add_unit(self, being):
        raise NotImplementedError("Subclass responsibility")

    def remove_unit(self):
        self._unit = Nothing()

    def commanded_by(self):
        return self._commanded_by

    def conquer(self, new_commander):
        self._commanded_by = new_commander

    def shares_type_with(self, another_territory):
        raise NotImplementedError("Subclass responsibility")

    def is_land(self):
        return False

    def is_sea(self):
        return False


class Land(Territory):
    def add_unit(self, being):
        self._unit = Army(being=being)

    def shares_type_with(self, another_territory):
        return another_territory.is_land()

    def is_land(self):
        return True


class Sea(Territory):
    def add_unit(self, being):
        self._unit = Fleet(being=being)

    def shares_type_with(self, another_territory):
        return another_territory.is_sea()

    def is_sea(self):
        return True
