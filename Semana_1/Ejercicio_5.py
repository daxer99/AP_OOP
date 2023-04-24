import random

class Dado:
    def __init__(self, caras):
        self.__caras = caras
        self.__valor = None

    def tirar(self):
        self.__valor = random.randint(1, self.__caras)

    def obtenerValor(self):
        return self.__valor

if __name__ == '__main__':
    d1 = Dado(8)
    d1.tirar()
    print(d1.obtenerValor())
