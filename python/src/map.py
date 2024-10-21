from src.territory import Land, Sea


class Map:
    def __init__(self, land_names, sea_names):
        lands = {name: Land(name) for name in land_names}
        seas = {name: Sea(name) for name in sea_names}
        self._territories = lands
        self._territories.update(seas)

    def neighbors(self, territory):
        return self._territories[territory].neighbors()

    def make_neighbors(self, a_territory, another_territory):
        self._territories[a_territory].add_neighbor(another_territory)
        self._territories[another_territory].add_neighbor(a_territory)

    def unit_of(self, a_territory):
        return self._territories[a_territory].unit()

    def add_unit(self, territory_name, being):
       self._territories[territory_name].add_unit(being=being)

    def remove_unit(self, on):
        self._territories[on].remove_unit()

    def move_unit(self, origin_name, destination_name):
        origin = self._territories[origin_name]
        destination = self._territories[destination_name]

        if self._is_move_allowed(destination, origin):
            self.add_unit(destination.name(), origin.commanded_by())
            self.remove_unit(origin.name())

    def commander_of(self, a_territory):
        return self._territories[a_territory].commanded_by()

    def conquer(self, territory, new_commander):
        self._territories[territory].conquer(new_commander)

    def _is_move_allowed(self, destination, origin):
        are_neighbors = destination.name() in origin.neighbors()
        is_same_territory_type = origin.shares_type_with(destination)
        destination_is_unoccupied = destination.unit().is_nothing()

        return are_neighbors and is_same_territory_type and destination_is_unoccupied
