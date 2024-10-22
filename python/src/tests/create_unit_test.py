from src.map import Map


class TestCreateUnit:
    def test_territories_are_initially_empty(self):
        territories = ["a"]
        my_map = Map(land_names=territories, sea_names=[], player_names=[])

        assert my_map.unit_of("a").is_nothing()

    def test_can_create_an_army_on_a_land(self):
        territories = ["a"]
        players = ["Player1"]
        my_map = Map(land_names=territories, sea_names=[], player_names=players)

        my_map.add_unit(territory_name="a", being="Player1")

        assert my_map.unit_of("a").is_army()
        assert my_map.unit_of("a").commander().name() == "Player1"

    def test_can_create_a_fleet_on_a_sea(self):
        territories = ["a"]
        players = ["Player1"]
        my_map = Map(land_names=[], sea_names=territories, player_names=players)

        my_map.add_unit(territory_name="a", being="Player1")

        assert my_map.unit_of("a").is_fleet()

    def test_can_remove_unit_from_territory(self):
        territories = ["a"]
        players = ["Player1"]
        my_map = Map(land_names=territories, sea_names=[], player_names=players)

        my_map.add_unit(territory_name="a", being="Player1")
        my_map.remove_unit(on="a")

        assert my_map.unit_of("a").is_nothing()
