from src.board import Board
from src.move import Move
from src.round import Round


class TestRound:
    def test_can_apply_a_round_with_one_simple_move_action(self):
        land1 = "land1"
        land2 = "land2"
        player = "P1"

        board = Board([land1, land2], [], [player])
        board.make_neighbors(land1, land2)
        board.add_new_army(land1, player)

        round = Round()
        round.add_order(Move(land1, land2, player))

        board.apply(round)
        assert board.unit_of(land2).is_army()

    def test_two_moves_to_the_same_place_bounce(self):
        land1 = "land1"
        land2 = "land2"
        land3 = "land3"
        player = "P1"

        board = Board([land1, land2, land3], [], [player])
        board.make_neighbors(land1, land2)
        board.make_neighbors(land3, land2)
        board.add_new_army(land1, player)
        board.add_new_army(land3, player)

        round = Round()
        round.add_order(Move(land1, land2, player))
        round.add_order(Move(land3, land2, player))

        board.apply(round)
        assert board.unit_of(land1).is_army()
        assert board.unit_of(land2).is_nothing()
        assert board.unit_of(land3).is_army()