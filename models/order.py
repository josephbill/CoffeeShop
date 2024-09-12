class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        from models.customer import Customer
        if isinstance(value, Customer):
            self._customer = value
        else:
            raise ValueError("Customer must be a Customer instance.")

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        from models.coffee import Coffee
        if isinstance(value, Coffee):
            self._coffee = value
        else:
            raise ValueError("Coffee must be a Coffee instance.")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, float) and 1.0 <= value <= 10.0:
            self._price = value
        else:
            raise ValueError("Price must be a float between 1.0 and 10.0.")