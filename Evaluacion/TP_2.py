class Store:
    def __init__(self):
        self.store_products = []
        self.users = []
    def add_product_to_store(self,product,quantity):
        self.store_products.append([product,quantity])
    def add_user(self,user):
        self.users.append(user)
    def find_product_by_name(self,product):
        finded = False
        for i in self.store_products:
            if product.get_name() == i[0].get_name():
                self.store_products[i][1] -= 1
                product = self.store_products[i][0]
                finded = True
        if finded:
            return product
        else:
            return None

class Product:
    def __int__(self,name,price):
        self.name = name
        self.price = price
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price

class Cart:
    def __int__(self):
        self.products = []
    def add_product(self,product):
        self.products.append(product)
    def calculate_cost(self):
        cost = 0
        for i in self.products:
            cost +=i.get_price()
    def check_product_stock(self,product,store):
        pass


class User:
    def __int__(self,id, name):
        self.id = id
        self.name = name
        self.cart = None

    def create_cart(self):
        self.cart = Cart()
