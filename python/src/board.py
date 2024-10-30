from src.player import Player
from src.territory import Territory
from src.units import Army, Fleet


class Board:
    def __init__(self, land_names, sea_names, player_names):
        lands = {name: Territory.new_land(name) for name in land_names}
        seas = {name: Territory.new_sea(name) for name in sea_names}
        self._territories = lands
        self._territories.update(seas)

        self._players = {name: Player(name) for name in player_names}

    def neighbors(self, territory):
        return self._territories[territory].neighbors()

    def make_neighbors(self, a_territory, another_territory):
        self._territories[a_territory].add_neighbor(another_territory)
        self._territories[another_territory].add_neighbor(a_territory)

    def unit_of(self, a_territory):
        return self._territories[a_territory].unit()

    def add_new_army(self, territory_name, being):
        commander = self._players[being]
        if self._is_territory_with_name_land(territory_name):
            self.add_unit(territory_name, Army(commander))

    def add_new_fleet(self, territory_name, being):
        commander = self._players[being]
        if self._is_territory_with_name_sea(territory_name) or self._is_terriroty_with_name_coast(territory_name):
            self.add_unit(territory_name, Fleet(commander))

    def add_unit(self, territory_name, unit):
        self._territories[territory_name].add_unit(unit)

    def remove_unit(self, on):
        self._territories[on].remove_unit()

    def move_unit(self, origin_name, destination_name):
        origin = self._territories[origin_name]
        destination = self._territories[destination_name]

        if self._is_move_allowed(destination, origin):
            self.add_unit(destination.name(), origin.unit())
            self.remove_unit(origin.name())

    def commander_of(self, a_territory):
        return self._territories[a_territory].commanded_by()

    def apply(self, round):
        round.apply_all_to(self)

    def _is_move_allowed(self, destination, origin):
        are_neighbors = destination.name() in origin.neighbors()
        destination_territory_is_compatible = self._is_territory_compatible_with_unit(destination, origin.unit())
        destination_is_unoccupied = destination.unit().is_nothing()

        return are_neighbors and destination_territory_is_compatible and destination_is_unoccupied

    def _is_territory_with_name_land(self, territory_name):
        return self._territories[territory_name].is_land()

    def _is_terriroty_with_name_coast(self, territory_name):
        territory = self._territories[territory_name]
        return self._is_territory_coast(territory)

    def _is_territory_with_name_sea(self, territory_name):
        return self._territories[territory_name].is_sea()

    def _is_territory_compatible_with_unit(self, territory, unit):
        if territory.is_sea():
            return unit.is_fleet()
        else:
            # Territory is land
            return unit.is_army() or self._is_territory_coast(territory)

    def _is_territory_coast(self, territory):
        return territory.is_land() and any(
            self._is_territory_with_name_sea(neighbor_name) for neighbor_name in territory.neighbors()
        )
