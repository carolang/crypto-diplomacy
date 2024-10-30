from src.board import Board


class TestMoveOrder:
    def test_can_move_to_an_adjacent_territory(self):
        land1 = "land1"
        land2 = "land2"
        land_names = [land1, land2]

        player1 = "Player1"

        board = Board(land_names=land_names, sea_names=[], player_names=[player1])
        board.make_neighbors(land1, land2)

        board.add_new_army(territory_name=land1, being=player1)

        board.move_unit(origin_name=land1, destination_name=land2)

        assert board.unit_of(land1).is_nothing()
        assert board.unit_of(land2).is_army()
        assert board.unit_of(land2).commander().name() == player1

    def test_cannot_move_to_a_not_adjacent_territory(self):
        land1 = "land1"
        land2 = "land2"
        land_names = [land1, land2]

        player1 = "Player1"

        board = Board(land_names=land_names, sea_names=[], player_names=[player1])

        board.add_new_army(territory_name=land1, being=player1)

        board.move_unit(origin_name=land1, destination_name=land2)

        assert board.unit_of(land1).is_army()
        assert board.unit_of(land2).is_nothing()

    def test_an_army_cannot_move_from_land_to_sea(self):
        land = "land"
        sea = "sea"

        player1 = "Player1"

        board = Board(land_names=[land], sea_names=[sea], player_names=[player1])
        board.make_neighbors(land, sea)

        board.add_new_army(territory_name=land, being=player1)

        board.move_unit(origin_name=land, destination_name=sea)

        assert board.unit_of(land).is_army()
        assert board.unit_of(sea).is_nothing()

    def test_a_fleet_can_move_to_a_coastal_territory(self):
        land = "land"
        sea = "sea"

        player1 = "Player1"

        board = Board(land_names=[land], sea_names=[sea], player_names=[player1])
        board.make_neighbors(land, sea)

        board.add_new_fleet(territory_name=sea, being=player1)

        board.move_unit(origin_name=sea, destination_name=land)

        assert board.unit_of(land).is_fleet()
        assert board.unit_of(sea).is_nothing()

    def test_a_fleet_cannot_move_to_an_inland_territory(self):
        coast = "coast"
        inland = "inland"
        sea = "sea"

        player1 = "Player1"

        board = Board(land_names=[coast, inland], sea_names=[sea], player_names=[player1])
        board.make_neighbors(coast, sea)
        board.make_neighbors(coast, inland)

        board.add_new_fleet(territory_name=coast, being=player1)

        board.move_unit(origin_name=coast, destination_name=inland)

        assert board.unit_of(coast).is_fleet()
        assert board.unit_of(inland).is_nothing()
