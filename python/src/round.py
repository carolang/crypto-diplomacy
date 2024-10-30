class Round:
    def __init__(self):
        super().__init__()
        self._orders = []

    def add_order(self, order):
        self._orders.append(order)

    def apply_all_to(self, board):
        for order in self._orders:
            if order.succeeds_in_context_of(self._orders):
                order.apply_on(board)
