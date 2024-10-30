from src.orders.order import Order


class HoldOrder(Order):
    def __init__(self, territory):
        super().__init__()
        self._territory = territory

    def territory(self):
        return self._territory

    def apply_on(self, board):
        pass

    def bounces_with_move(self, another_order):
        return self._territory == another_order.destination()

    def bounces_with_hold(self, another_order):
        return False

    def succeeds_in_context_of(self, orders):
        for another_order in orders:
            if another_order.bounces_with_hold(self):
                return self.support_in_context_of(orders) >= another_order.support_in_context_of(orders)
        return True

    def support_in_context_of(self, orders):
        return sum(another_order.amount_supported_to_hold(self) for another_order in orders)

    def amount_supported_to_hold(self, another_order):
        return 0

    def amount_supported_to_move(self, another_order):
        return 0
