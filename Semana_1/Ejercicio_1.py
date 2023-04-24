class BankAcount:
    def __init__(self, cbu):
        self.__cbu = cbu
        self.__balance = 0

    def deposit(self, amount):
        succes = True
        if amount > 0:
            self.__balance += amount
        else:
            succes = False

        return succes

    def withdraw(self, amount):
        success = True
        if amount < self.__balance:
            self.__balance -= amount
        else:
            success = False

        return success

    def getBalance(self):
        return self.__balance

    def getCBU(self):
        return self.__cbu

    def __str__(self):
        return 'CBU: ' + self.__cbu + ' Balance: ' + str(self.__balance)


if __name__ == '__main__':
    b1 = BankAcount('ABC123')
    b2 = BankAcount('DEF456')

    b1.deposit(5200)
    b2.deposit(4571)
    b1.withdraw(200)

    print('La cuenta', b1.getCBU(), 'tiene actualmente', b1.getBalance())
    print('La cuenta', b2.getCBU(), 'tiene actualmente', b2.getBalance())