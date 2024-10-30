class Order:
    def apply_on(self, board):
        raise NotImplementedError("Subclass responsibility")

    def bounces_with_move(self, another_order):
        raise NotImplementedError("Subclass responsibility")

    def bounces_with_hold(self, another_order):
        raise NotImplementedError("Subclass responsibility")

    def succeeds_in_context_of(self, orders):
        raise NotImplementedError("Subclass responsibility")

    def amount_supported_to_move(self, another_order):
        raise NotImplementedError("Subclass responsibility")

    def amount_supported_to_hold(self, another_order):
        raise NotImplementedError("Subclass responsibility")
