#DATOS.csv
'''dni,nombre,apellido,edad
16,rodrigo,peralta,30
23,juan,perez,23
3,lucia,gomez,42
45,maria,ruhl,19'''

import pandas as pd

def read_file(filename):
    data = pd.read_csv(filename,sep=",")
    return data.values.tolist()

class Persona:
    def __init__(self,dni,nomb,ape,edad):
        self.dni = dni
        self.nombre = nomb
        self.apellido = ape
        self.edad = edad
    def get_dni(self):
        return self.dni
    def get_nombre(self):
        return self.nombre
    def get_apellido(self):
        return self.apellido
    def get_edad(self):
        return self.edad

class Sala:
    def __init__(self,nombre):
        self.nombre = nombre
        self.personas = []
    def get_nombre(self):
        return self.nombre
    def add_persona(self,persona):
        self.personas.append(persona)
    def calcular_promedio_edad(self):
        sum = 0
        for p in self.personas:
            sum = sum + p.get_edad()
        promedio = sum/len(self.personas)
        return round(promedio,2)
    def ordenar_lista_apellido(self):
        return sorted(self.personas,key = lambda x:x[2])
    #    return sorted( self.personas, key=lambda x: x.get_apellido() )

    def ordenar_lista_edad(self):
        return sorted(self.personas,key=lambda x:x[3])
    #    return sorted( self.personas, key=lambda x: x.get_edad() )


filename = "datos.csv"
datos = read_file(filename)

aula1 = Sala("Aula_1")
for i in range(len(datos)):
    aula1.add_persona([datos[i][0],datos[i][1],datos[i][2],datos[i][3]])
    # aula1.add_persona(Persona(datos[i][0],datos[i][1],datos[i][2],datos[i][3]))

lista_edad = aula1.ordenar_lista_edad()
# lista_apellido = aula1.ordenar_lista_apellido()
for i in lista_edad:
    print(i[1],i[2],i[3])
# print()
# for i in lista_apellido:
#     print(i.get_nombre(),i.get_apellido(),i.get_edad())