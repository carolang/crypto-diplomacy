from src.map import Map


class TestCommands:
    def test_can_move_to_an_adjacent_territory(self):
        land1 = "land1"
        land2 = "land2"
        land_names = [land1, land2]
        my_map = Map(land_names=land_names, sea_names=[])
        my_map.make_neighbors(land1, land2)

        my_map.add_unit(territory_name=land1, being="Player1")

        my_map.move_unit(origin_name=land1, destination_name=land2)

        assert my_map.unit_of(land1).is_nothing()
        assert my_map.unit_of(land2).is_army()

    def test_cannot_move_to_a_not_adjacent_territory(self):
        land1 = "land1"
        land2 = "land2"
        land_names = [land1, land2]
        my_map = Map(land_names=land_names, sea_names=[])

        my_map.add_unit(territory_name=land1, being="Player1")

        my_map.move_unit(origin_name=land1, destination_name=land2)

        assert my_map.unit_of(land1).is_army()
        assert my_map.unit_of(land2).is_nothing()

    def test_cannot_move_from_land_to_sea(self):
        land = "land"
        sea = "sea"
        my_map = Map(land_names=[land], sea_names=[sea])
        my_map.make_neighbors(land, sea)

        my_map.add_unit(territory_name=land, being="Player1")

        my_map.move_unit(origin_name=land, destination_name=sea)

        assert my_map.unit_of(land).is_army()
        assert my_map.unit_of(sea).is_nothing()

    def test_cannot_move_to_occupied_territory(self):
        land1 = "land1"
        land2 = "land2"
        land_names = [land1, land2]
        my_map = Map(land_names=land_names, sea_names=[])
        my_map.make_neighbors(land1, land2)

        my_map.add_unit(territory_name=land1, being="Player1")
        my_map.add_unit(territory_name=land2, being="Player1")

        my_map.move_unit(origin_name=land1, destination_name=land2)

        assert my_map.unit_of(land1).is_army()
        assert my_map.unit_of(land2).is_army()
