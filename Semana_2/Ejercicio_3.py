class Persona:
    def __init__(self,nombre, apellido):
        self.__nombre=nombre
        self.__apellido = apellido
    
    def __str__(self):
        return self.__nombre +' '+self.__apellido 
    
    def __repr__(self):
        return self.__str__()

class PhoneBill:
    def __init__(self,ID,usuario):
        self.__ID = ID
        self.__usuario = usuario
        self.__registroLlamadas = []
        self.__saldo = 0
        self.__precioSegundo = 0.1
        
    def registrarLlamada(self,destinatario,duracion):
        llamada = (destinatario,duracion)
        self.__registroLlamadas.append(llamada)
        self.__saldo += duracion*self.__precioSegundo
    
    def mostrarMovimientos(self):
        return self.__registroLlamadas
    
    def consultarSaldo(self):
        return self.__saldo
    
    def ajustarPrecioSegundo(self,nuevoPrecio):
        self.__precioSegundo = nuevoPrecio
        
if __name__ == '__main__':
    
    f1 = PhoneBill(12,'RPeralta')
    f1.ajustarPrecioSegundo(0.5)
    f1.registrarLlamada('JPerez',120)
    f1.registrarLlamada('LDiaz',90)
    f1.registrarLlamada('JRuhl',78)
    print('Movimientos \n')
    print(f1.mostrarMovimientos())
    print('\n')
    print('El saldo actual es: $',f1.consultarSaldo())

    u1 = Persona('Rodrigo','Peralta')
    f2 = PhoneBill(52,u1)
    d1= Persona('j','p')
    f2.registrarLlamada(d1,154)
    print(f2.mostrarMovimientos())