from src.units import Nothing


class Territory:
    def __init__(self, name):
        self._name = name

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

    def shares_type_with(self, another_territory):
        raise NotImplementedError("Subclass responsibility")

    def is_land(self):
        raise NotImplementedError("Subclass responsibility")

    def is_sea(self):
        raise NotImplementedError("Subclass responsibility")


class Land(Territory):
    def shares_type_with(self, another_territory):
        return another_territory.is_land()

    def is_land(self):
        return True

    def is_sea(self):
        return False


class Sea(Territory):
    def shares_type_with(self, another_territory):
        return another_territory.is_sea()

    def is_land(self):
        return False

    def is_sea(self):
        return True
