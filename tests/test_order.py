import pytest
from models.coffee import Coffee
from models.customer import Customer
from models.order import Order

def test_order_initialization():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 5.0)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0

def test_order_customer_validation():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    with pytest.raises(ValueError):
        Order("NotACustomer", coffee, 5.0)

def test_order_coffee_validation():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    with pytest.raises(ValueError):
        Order(customer, "NotACoffee", 5.0)

def test_order_price_validation():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    with pytest.raises(ValueError):
        Order(customer, coffee, 0.5)
    with pytest.raises(ValueError):
        Order(customer, coffee, 11.0)
