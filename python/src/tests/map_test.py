from src.map import Map
from src.player import Player


class TestMap:
    def test_initially_a_territory_has_no_neighbors(self):
        territories = ["a"]
        my_map = Map(land_names=territories, sea_names=[])

        neighbors = my_map.neighbors("a")

        assert neighbors == set()

    def test_can_add_a_neighbor(self):
        territories = ["a", "b"]
        my_map = Map(land_names=territories, sea_names=[])

        my_map.make_neighbors("a", "b")

        neighbors = my_map.neighbors("a")

        assert neighbors == {"b"}

    def test_initially_territories_are_neutral(self):
        territories = ["a"]
        my_map = Map(land_names=territories, sea_names=[])

        assert my_map.commander_of("a").name() == "NEUTRAL"

    def test_a_player_can_control_a_territory(self):
        territories = ["a"]
        my_map = Map(land_names=territories, sea_names=[])

        my_name = "Me"
        player = Player(my_name)

        my_map.conquer(territory="a", new_commander=player)

        assert my_map.commander_of("a").name() == my_name
