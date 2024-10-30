class Move:
    def __init__(self, origin, destination, being):
        self._origin = origin
        self._destination = destination
        self._being = being

    def origin(self):
        return self._origin

    def destination(self):
        return self._destination

    def apply_on(self, board):
        board.move_unit(self._origin, self._destination)

    def succeeds_in_context_of(self, orders):
        return not any(self._bounces_with(order) for order in orders)

    def _bounces_with(self, another_order):
        return self._origin != another_order.origin() and self._destination == another_order.destination()
