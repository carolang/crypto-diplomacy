from src.board import Board


class TestAddUnit:
    def test_territories_are_initially_empty(self):
        territories = ["a"]
        my_map = Board(land_names=territories, sea_names=[], player_names=[])

        assert my_map.unit_of("a").is_nothing()

    def test_can_create_an_army_on_a_land(self):
        territories = ["a"]
        players = ["Player1"]
        my_map = Board(land_names=territories, sea_names=[], player_names=players)

        my_map.add_new_army(territory_name="a", being="Player1")

        assert my_map.unit_of("a").is_army()
        assert my_map.unit_of("a").commander().name() == "Player1"

    def test_cannot_create_an_army_on_a_sea(self):
        territories = ["a"]
        players = ["Player1"]
        my_map = Board(land_names=[], sea_names=territories, player_names=players)

        my_map.add_new_army(territory_name="a", being="Player1")

        assert my_map.unit_of("a").is_nothing()

    def test_can_create_a_fleet_on_a_sea(self):
        territories = ["a"]
        players = ["Player1"]
        my_map = Board(land_names=[], sea_names=territories, player_names=players)

        my_map.add_new_fleet(territory_name="a", being="Player1")

        assert my_map.unit_of("a").is_fleet()

    def test_can_remove_unit_from_territory(self):
        territories = ["a"]
        players = ["Player1"]
        my_map = Board(land_names=territories, sea_names=[], player_names=players)

        my_map.add_new_army(territory_name="a", being="Player1")
        my_map.remove_unit(on="a")

        assert my_map.unit_of("a").is_nothing()


    def test_cannot_create_a_fleet_on_an_inland_land(self):
        territories = ["a"]
        players = ["Player1"]
        my_map = Board(land_names=territories, sea_names=[], player_names=players)

        my_map.add_new_fleet(territory_name="a", being="Player1")

        assert my_map.unit_of("a").is_nothing()

    def test_can_create_a_fleet_on_a_coastal_land(self):
        lands = ["land"]
        seas = ["sea"]
        players = ["Player1"]
        board = Board(land_names=lands, sea_names=seas, player_names=players)
        board.make_neighbors("land", "sea")

        board.add_new_fleet(territory_name="land", being="Player1")

        assert board.unit_of("land").is_fleet()
