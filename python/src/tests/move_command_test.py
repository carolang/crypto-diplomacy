from src.board import Board


class TestMoveCommand:
    def test_can_move_to_an_adjacent_territory(self):
        land1 = "land1"
        land2 = "land2"
        land_names = [land1, land2]

        player1 = "Player1"

        board = Board(land_names=land_names, sea_names=[], player_names=[player1])
        board.make_neighbors(land1, land2)

        board.add_unit(territory_name=land1, being=player1)

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

        board.add_unit(territory_name=land1, being=player1)

        board.move_unit(origin_name=land1, destination_name=land2)

        assert board.unit_of(land1).is_army()
        assert board.unit_of(land2).is_nothing()

    def test_cannot_move_from_land_to_sea(self):
        land = "land"
        sea = "sea"

        player1 = "Player1"

        board = Board(land_names=[land], sea_names=[sea], player_names=[player1])
        board.make_neighbors(land, sea)

        board.add_unit(territory_name=land, being=player1)

        board.move_unit(origin_name=land, destination_name=sea)

        assert board.unit_of(land).is_army()
        assert board.unit_of(sea).is_nothing()

    def test_cannot_move_to_occupied_territory(self):
        land1 = "land1"
        land2 = "land2"
        land_names = [land1, land2]

        player1 = "Player1"

        board = Board(land_names=land_names, sea_names=[], player_names=[player1])
        board.make_neighbors(land1, land2)

        board.add_unit(territory_name=land1, being=player1)
        board.add_unit(territory_name=land2, being=player1)

        board.move_unit(origin_name=land1, destination_name=land2)

        assert board.unit_of(land1).is_army()
        assert board.unit_of(land2).is_army()
