class Product:
    def __init__(self, product_id, name, price, description):
        self.data = {
            'product_id': product_id,
            'name': name,
            'price': price,
            'description': description,
            'reviews': []
        }

    def add_review(self, review_text):
        self.data['reviews'].append(review_text)

    def display_info(self):
        print(f"Product ID: {self.data['product_id']}")
        print(f"Name: {self.data['name']}")
        print(f"Price: ${self.data['price']}")
        print(f"Description: {self.data['description']}")
        if self.data['reviews']:
            print("Reviews:")
            for review in self.data['reviews']:
                print(f"  - {review}")
        else:
            print("No reviews yet.")

class Customer:
    def __init__(self, cus_id, name):
        self.data = {
            'cus_id': cus_id,
            'name': name,
        }
    def make_product_review(self,product,review_text):
        product.add_review(review_text)

p1 = Product(1,"Motorola Moto G32",75000,"Celular motorola")
p2 = Product(2,"Samsung Galaxy j7",83000,"Celular samsung")
c1 = Customer(1,"Juan Perez")
c2 = Customer(10,"Lalo Landa")
c1.make_product_review(p1,"Excelente camara, saca fotos muy nitidas")
c1.make_product_review(p1, "La bateria dura mas de lo que esperaba")
c2.make_product_review(p2,"Excelente diseño ergonomico")

p1.display_info()
print()
p2.display_info()