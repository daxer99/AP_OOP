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


retired_bonus = 30
worker_bonus = 60
student_bonus = 40

c = Card(1)
s = Student(1, "Pedro", "Lopez",student_bonus)
s.buy_card(c)
s.charge_card(100)
print(s.check_balance())
s.pay_ticket(100)
print(s.check_balance())

