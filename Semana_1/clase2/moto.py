class Moto:
    def __init__(self, a, b, c, d):
        self.__nivel_combustible = a  # litros
        self.__velocidad_actual = b
        self.__estado_motor = c
        self.__cambio_actual = d

    def informar_nivel_combustible(self):
        return self.__nivel_combustible

    def modificar_nivel_combustible(self, cg):
        self.__nivel_combustible = self.__nivel_combustible - cg


moto_1 = Moto(10, 0, 8, "N")
cg = int(input("Nivel de combustible gastado: "))  # 5
moto_1.modificar_nivel_combustible(cg)
print(moto_1.informar_nivel_combustible())  # 5