"""Implement the UML class diagram for a restaurant in code"""


class Restaurant:
    """Represents a restaurant."""
    def __init__(self, name, location, menu):
        """Initialize Restaurant with name, location, and menu."""
        self.name = name
        self.location = location
        self.menu = menu
        self.staff = []

    @staticmethod
    def place_order(order):
        """Places an order."""
        print(f"Placing order {order.order_id} for {order.customer.name}")

    @staticmethod
    def process_payment(payment):
        """Processes a payment."""
        print(f"Processing payment with ID: {payment.payment_id}")

    @staticmethod
    def prepare_food(order):
        """Prepares food for an order."""
        print(f"Preparing food for order {order.order_id}")

    @staticmethod
    def deliver_order(order):
        """Delivers an order."""
        print(f"Delivering order {order.order_id} to {order.customer.name}")


class Menu:
    """Represents a menu."""
    def __init__(self):
        """Initialize Menu with dishes."""
        self.dishes = []

    def add_dish(self, dish):
        """Adds a dish to the menu."""
        self.dishes.append(dish)

    def remove_dish(self, dish):
        """Removes a dish from the menu."""
        self.dishes.remove(dish)


class Dish:
    """Represents a dish."""
    def __init__(self, name, price, description):
        """Initialize Dish with name, price, and description."""
        self.name = name
        self.price = price
        self.description = description


class Order:
    """Represents an order."""
    total_amount_all_orders = 0.0  # Static attribute to track total amount for all orders

    def __init__(self, order_id, customer):
        """Initialize Order with order ID and customer."""
        self.order_id = order_id
        self.customer = customer
        self.items = []
        self._total_amount = 0.0

    def add_item(self, item):
        """Adds an item to the order."""
        self.items.append(item)

    def remove_item(self, item):
        """Removes an item from the order."""
        self.items.remove(item)

    @staticmethod
    def calculate_total(order):
        """Calculates the total amount of the order."""
        total = sum(item.dish.price * item.quantity for item in order.items)
        order._total_amount = total
        Order.total_amount_all_orders += total
        return total

    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        raise AttributeError("Cannot set total_amount directly. Please use calculate_total() method.")


class Customer:
    """Represents a customer."""
    def __init__(self, name, address, phone_number):
        """Initialize Customer with name, address, and phone number."""
        self.name = name
        self.address = address
        self.phone_number = phone_number


class Staff:
    """Represents staff members."""
    def __init__(self, name, position):
        """Initialize Staff with ID, name, and position."""
        self.name = name
        self.position = position

    @staticmethod
    def take_order(order):
        """Takes an order."""
        print(f"Taking order {order.order_id}")

    @staticmethod
    def serve_order(order):
        """Serves an order."""
        print(f"Serving order {order.order_id}")

    @staticmethod
    def process_payment(payment):
        """Processes a payment."""
        print(f"Processing payment with ID: {payment.payment_id}")


class DeliveryStaff(Staff):
    """Represents delivery staff."""

    @staticmethod
    def deliver_order(order):
        """Delivers an order."""
        print(f"Delivering order {order.order_id} to {order.customer.name}")


class Payment:
    """Represents a payment."""
    def __init__(self, payment_id, amount, payment_method):
        """Initialize Payment with ID, amount, and payment method."""
        self.payment_id = payment_id
        self.amount = amount
        self.payment_method = payment_method


class Item:
    """Represents an item in an order."""
    def __init__(self, dish: 'Dish', quantity: int):
        """Initialize Item with dish and quantity."""
        self.dish = dish
        self.quantity = quantity


# Some Testing Examples:
# Creating a menu with some dishes
if __name__ == "__main__":
    menu1 = Menu()
    dish1 = Dish("Sushi", 15.99, "Fresh sushi rolls with salmon and avocado")
    dish2 = Dish("Pasta", 12.99, "Spaghetti with marinara sauce and meatballs")
    menu1.add_dish(dish1)
    menu1.add_dish(dish2)

    # Creating a customer
    customer1 = Customer("Mohammed Zoraiki", "egytem ter 1", "+36204935984")

    # Creating an order
    order1 = Order("98765", customer1)
    item1 = Item(dish1, 3)  # 3 sushi rolls
    item2 = Item(dish2, 2)  # 2 plates of pasta
    order1.add_item(item1)
    order1.add_item(item2)

    # Placing the order
    Restaurant.place_order(order1)

    # Calculating the total amount for the order
    Order.calculate_total(order1)

    # Preparing food for the order
    Restaurant.prepare_food(order1)

    # Delivering the order
    Restaurant.deliver_order(order1)

    # Processing payment for the order
    payment1 = Payment("54321", order1.total_amount, "Credit Card")
    Restaurant.process_payment(payment1)

    # Creating staff
    staff = Staff("Alice", "Server")

    # Taking the order by staff
    staff.take_order(order1)

    # Serving the order by staff
    staff.serve_order(order1)

    # Processing payment by staff
    staff.process_payment(payment1)

    # Creating delivery staff
    delivery_guy = DeliveryStaff("Bob", "Delivery Driver")

    # Delivering the order by delivery staff
    delivery_guy.deliver_order(order1)
