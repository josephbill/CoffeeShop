class Coffee:
    def __init__(self, name):
        self.name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) >= 3:
            self._name = value
        else:
            raise ValueError("Coffee name must be a string with at least 3 characters.")

    def add_order(self, order):
        self._orders.append(order)

    def orders(self):
        return self._orders

    def customers(self):
        return list(set(order.customer for order in self._orders))

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if self._orders:
            total_price = sum(order.price for order in self._orders)
            return total_price / len(self._orders)
        return 0
