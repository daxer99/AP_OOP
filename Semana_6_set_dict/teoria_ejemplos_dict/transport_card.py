from abc import abstractmethod

class Card:
    def __init__(self,id):
        self.__id = id
        self.__balance = 0
    def get_id(self):
        return self.__id
    def get_balance(self):
        return self.__balance
    def charge(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount
    def discount(self,amount):
        self.__balance = self.__balance - amount

class User:
    def __init__(self, dni, first_name, last_name):
        self.__dni = dni
        self.__first_name = first_name
        self.__last_name = last_name
        self.__card = 0
    def buy_card(self, card):
        self.__card = card
    def charge_card(self, amount):
        self.__card.charge(amount)
    @abstractmethod
    def pay_ticket(self,rate):
        pass
    def check_balance(self):
        return self.__card.get_balance()
    def get_card(self):
        return self.__card
    def __str__(self):
        return self.__first_name +" "+self.__last_name

class Student(User):
    def __init__(self, id, first_name, last_name, bonus):
        User.__init__( self, id, first_name, last_name )
        self.__bonus = bonus
    def pay_ticket(self,rate):
        if self.__bonus > 0:
            self.get_card().discount(rate-rate*0.5)
            self.__bonus = self.__bonus - 1
        else:
            self.get_card().discount(rate)

class Worker(User):
    def __init__(self, id, first_name, last_name, bonus):
        User.__init__( self, id, first_name, last_name )
        self.__bonus = bonus
    def pay_ticket(self,rate):
        if self.__bonus > 0:
            self.get_card().discount(rate-rate*0.35)
            self.__bonus = self.__bonus - 1
        else:
            self.get_card().discount(rate)

class Retired(User):
    def __init__(self, id, first_name, last_name, bonus):
        User.__init__( self, id, first_name, last_name )
        self.__bonus = bonus
    def pay_ticket(self,rate):
        if self.__bonus > 0:
            self.get_card().discount(rate-rate*0.75)
            self.__bonus = self.__bonus - 1
        else:
            self.get_card().discount(rate)

class Card_Manager:
    card_id = 0
    def __init__(self):
        self.__distributed_cards = {}

    def generate_card(self):
        Card_Manager.card_id += 1
        return Card(Card_Manager.card_id)

    def sell_card(self,user):
        card = self.generate_card()
        user.buy_card(card)
        self.__distributed_cards.update({card.get_id():user})

    def get_distributed_cards(self):
        return self.__distributed_cards


retired_bonus = 30
worker_bonus = 60
student_bonus = 40

cm = Card_Manager()
s = Student(1, "Pedro", "Lopez",student_bonus)
cm.sell_card(s)
w = Worker(2,"Lalo","Landa",worker_bonus)
cm.sell_card(w)

s.charge_card(100)
print(s.check_balance())
s.pay_ticket(100)
print(s.check_balance())

print()
for key, value in cm.get_distributed_cards().items():
    print( f"Card_id: {key}, Titular: {value}" )