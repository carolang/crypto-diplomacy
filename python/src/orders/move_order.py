from src.orders.order import Order


class MoveOrder(Order):
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
        for another_order in orders:
            if another_order.bounces_with_move(self):
                return self.support_in_context_of(orders) > another_order.support_in_context_of(orders)
        return True

    def bounces_with_move(self, another_order):
        return self._origin != another_order.origin() and self._destination == another_order.destination()

    def bounces_with_hold(self, another_order):
        return self._destination == another_order.territory()

    def support_in_context_of(self, orders):
        return sum(another_order.amount_supported_to_move(self) for another_order in orders)

    def amount_supported_to_hold(self, another_order):
        return 0

    def amount_supported_to_move(self, another_order):
        return 0
