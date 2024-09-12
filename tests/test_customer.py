import pytest
from models.coffee import Coffee
from models.customer import Customer
from models.order import Order

def test_customer_initialization():
    customer = Customer("Alice")
    assert customer.name == "Alice"

def test_customer_name_validation():
    with pytest.raises(ValueError):
        Customer("A very long name")
    with pytest.raises(ValueError):
        Customer("")

def test_create_order():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    order = customer.create_order(coffee, 5.0)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0
    assert len(customer.orders()) == 1
    assert len(coffee.orders()) == 1

def test_customer_orders():
    customer = Customer("Bob")
    coffee1 = Coffee("Espresso")
    coffee2 = Coffee("Cappuccino")
    customer.create_order(coffee1, 4.0)
    customer.create_order(coffee2, 5.0)
    orders = customer.orders()
    assert len(orders) == 2
    assert orders[0].coffee == coffee1
    assert orders[1].coffee == coffee2

def test_customer_coffees():
    customer = Customer("Charlie")
    coffee1 = Coffee("Americano")
    coffee2 = Coffee("Mocha")
    customer.create_order(coffee1, 6.0)
    customer.create_order(coffee2, 7.0)
    coffees = customer.coffees()
    assert len(coffees) == 2
    assert coffee1 in coffees
    assert coffee2 in coffees
