import pytest
from models.coffee import Coffee
from models.customer import Customer
from models.order import Order

def test_coffee_initialization():
    coffee = Coffee("Mocha")
    assert coffee.name == "Mocha"

def test_coffee_name_validation():
    with pytest.raises(ValueError):
        Coffee("T")
    with pytest.raises(ValueError):
        Coffee("")

def test_add_order():
    coffee = Coffee("Latte")
    customer = Customer("Alice")
    order = customer.create_order(coffee, 5.0)
    assert len(coffee.orders()) == 1
    assert coffee.orders()[0] == order

def test_coffee_orders():
    coffee = Coffee("Espresso")
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")
    customer1.create_order(coffee, 4.0)
    customer2.create_order(coffee, 5.0)
    orders = coffee.orders()
    assert len(orders) == 2
    assert orders[0].customer == customer1
    assert orders[1].customer == customer2

def test_coffee_customers():
    coffee = Coffee("Cappuccino")
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")
    customer1.create_order(coffee, 4.0)
    customer2.create_order(coffee, 5.0)
    customers = coffee.customers()
    assert len(customers) == 2
    assert customer1 in customers
    assert customer2 in customers

def test_num_orders():
    coffee = Coffee("Latte")
    customer = Customer("Charlie")
    customer.create_order(coffee, 5.0)
    customer.create_order(coffee, 4.0)
    assert coffee.num_orders() == 2

def test_average_price():
    coffee = Coffee("Mocha")
    customer = Customer("Alice")
    customer.create_order(coffee, 6.0)
    customer.create_order(coffee, 8.0)
    assert coffee.average_price() == 7.0
