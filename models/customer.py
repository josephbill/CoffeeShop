class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")

    def orders(self):
        return self._orders

    def coffees(self):
        return list(set(order.coffee for order in self._orders))

    def create_order(self, coffee, price):
        from models.order import Order  # Avoid circular imports
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee.add_order(order)
        return order

    @classmethod
    def most_aficionado(cls, coffee):
        customers_spending = {}
        for order in coffee.orders():
            customer = order.customer
            customers_spending[customer] = customers_spending.get(customer, 0) + order.price

        if customers_spending:
            return max(customers_spending, key=customers_spending.get)
        return None