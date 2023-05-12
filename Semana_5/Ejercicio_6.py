class MenuItem:
    def __init__(self, name, description, price, type, ingredients):
        self.name = name
        self.description = description
        self.price = price
        self.type = type
        self.ingredients = ingredients

    def __str__(self):
        return f"{self.name} - {self.description} ({self.type}): ${self.price}"

    def get_price(self):
        return self.price

    def get_type(self):
        return self.type

    def get_ingredients(self):
        return self.ingredients

class Menu:
    def __init__(self, name, items):
        self.name = name
        self.items = items

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_items_by_type(self, type):
        return [item for item in self.items if item.get_type() == type]

class Order:
    def __init__(self, table_number, items):
        self.table_number = table_number
        self.items = items
        self.total_price = self.calculate_total()

    def add_item(self, item):
        self.items.append(item)
        self.total_price = self.calculate_total()

    def remove_item(self, item):
        self.items.remove(item)
        self.total_price = self.calculate_total()

    def calculate_total(self):
        return sum([item.get_price() for item in self.items])

class Restaurant:
    def __init__(self, name, menu):
        self.name = name
        self.menu = menu
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def remove_order(self, order):
        self.orders.remove(order)

    def get_orders_by_table(self, table_number):
        return [order for order in self.orders if order.table_number == table_number]

# Example usage:
menu_items = [
    MenuItem("Cheeseburger", "Juicy beef patty with melted cheddar cheese", 10.99, "Entree", ["beef", "cheddar cheese"]),
    MenuItem("Caesar Salad", "Crisp romaine lettuce with Caesar dressing", 7.99, "Appetizer", ["romaine lettuce", "Caesar dressing"]),
    MenuItem("Chocolate Cake", "Decadent chocolate cake with chocolate frosting", 5.99, "Dessert", ["chocolate cake", "chocolate frosting"])
]

menu = Menu("Main Menu", menu_items)

restaurant = Restaurant("The Bistro", menu)

order1_items = [menu_items[0], menu_items[2]]
order1 = Order(1, order1_items)
restaurant.add_order(order1)

order2_items = [menu_items[1]]
order2 = Order(2, order2_items)
restaurant.add_order(order2)

print(restaurant.get_orders_by_table(1))