from BankAccount import BankAccount
import random as rd

class Bank:
    def __init__(self,ID,nombre):
        self.__ID = ID
        self.__nombre = nombre
        self.__cuentas = []
        
    def agregarCuenta(self,cuenta):
        self.__cuentas.append(cuenta)
    
    def crearCuenta(self):
        cbu = rd.randint(100,1000)
        nuevaCuenta = BankAccount(cbu)
        self.agregarCuenta(nuevaCuenta)
    
    def quitarCuenta(self,cbu):
        for i,o in enumerate(self.__cuentas):
            if o.getCbu() == cbu:
                del self.__cuentas[i]
                return True
            else:
                return False
    
    # def quitarCuenta(self,cbu):
    #     aux = [cuenta for cuenta in self.__cuentas if cuenta.getCbu() != cbu]
    #     self.__cuentas = aux
        
    # def quitarCuenta(self,cuenta):
    #     self.__cuentas.remove(cuenta)
    
    def transferir_dinero(self,cuenta_origen, cuenta_destino,monto):
        if(monto<cuenta_origen.getBalance()):
            cuenta_origen.withdraw(monto)
            cuenta_destino.deposit(monto)
            return True
        else:
            return False
    
    def ordenar_cuentas_cbu(self):
        lista = self.__cuentas
        lista_ordenada = sorted(lista,key = lambda x: x.getCBU())
        return lista_ordenada
    
    def ordenar_cuentas_balance(self):
        lista = self.__cuentas
        lista_ordenada = sorted(lista,key = lambda x: x.getBalance(),reverse=True)
        return lista_ordenada

if __name__ == '__main__':
    
    c1 = BankAccount(100)
    c1.deposit(1000)
    
    c2 = BankAccount(102)
    c2.deposit(15000)
    
    macro = Bank(7,'Macro')
    macro.agregarCuenta(c1)
    macro.agregarCuenta(c2)
    macro.crearCuenta()
    
    lista = macro.ordenar_cuentas_cbu()
    for i in lista:
        print(i)
    
    macro.transferir_dinero(c2,c1,152)
    lista = macro.ordenar_cuentas_cbu()
    for i in lista:
        print(i)
    