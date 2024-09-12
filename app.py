from models.customer import Customer
from models.coffee import Coffee
from models.order import Order

def main():
    # Create some Coffee instances
    espresso = Coffee("Espresso")
    latte = Coffee("Latte")
    cappuccino = Coffee("Cappuccino")

    # Print coffee details
    print(f"Created coffee: {espresso.name}")
    print(f"Created coffee: {latte.name}")
    print(f"Created coffee: {cappuccino.name}")

    # Create some Customer instances
    alice = Customer("Alice")
    bob = Customer("Bob")
    charlie = Customer("Charlie")

    # Print customer details
    print(f"Created customer: {alice.name}")
    print(f"Created customer: {bob.name}")
    print(f"Created customer: {charlie.name}")

    # Create Orders
    order1 = alice.create_order(espresso, 4.5)
    order2 = bob.create_order(latte, 5.0)
    order3 = charlie.create_order(cappuccino, 6.0)
    order4 = alice.create_order(latte, 5.5)
    order5 = bob.create_order(cappuccino, 6.5)

    # Print order details
    print(f"Order 1: Customer={order1.customer.name}, Coffee={order1.coffee.name}, Price={order1.price}")
    print(f"Order 2: Customer={order2.customer.name}, Coffee={order2.coffee.name}, Price={order2.price}")
    print(f"Order 3: Customer={order3.customer.name}, Coffee={order3.coffee.name}, Price={order3.price}")
    print(f"Order 4: Customer={order4.customer.name}, Coffee={order4.coffee.name}, Price={order4.price}")
    print(f"Order 5: Customer={order5.customer.name}, Coffee={order5.coffee.name}, Price={order5.price}")

    # Check orders for each customer
    print(f"\nOrders for {alice.name}:")
    for order in alice.orders():
        print(f"  Coffee: {order.coffee.name}, Price: {order.price}")

    print(f"\nOrders for {bob.name}:")
    for order in bob.orders():
        print(f"  Coffee: {order.coffee.name}, Price: {order.price}")

    # Check coffees for each customer
    print(f"\nCoffees ordered by {alice.name}:")
    for coffee in alice.coffees():
        print(f"  Coffee: {coffee.name}")

    print(f"\nCoffees ordered by {bob.name}:")
    for coffee in bob.coffees():
        print(f"  Coffee: {coffee.name}")

    # Check orders for each coffee
    print(f"\nOrders for {espresso.name}:")
    for order in espresso.orders():
        print(f"  Customer: {order.customer.name}, Price: {order.price}")

    print(f"\nOrders for {latte.name}:")
    for order in latte.orders():
        print(f"  Customer: {order.customer.name}, Price: {order.price}")

    # Check customers who ordered each coffee
    print(f"\nCustomers who ordered {espresso.name}:")
    for customer in espresso.customers():
        print(f"  Customer: {customer.name}")

    print(f"\nCustomers who ordered {latte.name}:")
    for customer in latte.customers():
        print(f"  Customer: {customer.name}")

    # Test aggregate methods
    print(f"\nTotal number of orders for {latte.name}: {latte.num_orders()}")
    print(f"Average price for {latte.name}: {latte.average_price()}")

    # Test most aficionado method
    most_aficionado = Customer.most_aficionado(latte)
    if most_aficionado:
        print(f"\nCustomer who spent the most on {latte.name}: {most_aficionado.name}")
    else:
        print(f"\nNo customers have ordered {latte.name}")

if __name__ == "__main__":
    main()
