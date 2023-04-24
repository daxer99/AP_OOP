class BankAccount:
    def __init__(self,cbu):
        self.__cbu = cbu
        self.__balance = None
    
    def deposit(self,amount):
        success = True
        if amount > 0:
            self.__balance = amount
        else:
            success = False
        return success
            
    def withdraw(self,amount):
        success = True
        if amount < self.__balance:
            self.__balance = self.__balance - amount
        else:
            success = False
        return success
    
    def getBalance(self):
        return self.__balance
    
    def getCBU(self):
        return self.__cbu
    
    def __str__(self):
        return '(CBU: '+ str(self.__cbu)+', '+'Balance: '+ str(self.__balance)+ ')'