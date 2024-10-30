from src.orders.order import Order


class SupportOrder(Order):
    def __init__(self, origin, supported_origin, supported_destination):
        super().__init__()
        self._origin = origin
        self._supported_origin = supported_origin
        self._supported_destination = supported_destination

    def apply_on(self, board):
        pass

    def bounces_with_move(self, another_order):
        return False

    def bounces_with_hold(self, another_order):
        return False

    def succeeds_in_context_of(self, orders):
        return True

    def amount_supported_to_move(self, another_order):
        is_origin_supported = self._supported_origin == another_order.origin()
        is_destination_supported = self._supported_destination == another_order.destination()
        if is_origin_supported and is_destination_supported:
            return 1
        return 0

    def amount_supported_to_hold(self, another_order):
        return 0
