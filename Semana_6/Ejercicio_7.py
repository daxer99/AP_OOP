from operator import itemgetter

lista = [{ "nombre" : "Rodrigo","apellido" : "Peralta", "edad" : 27},
         { "nombre" : "Lucia","apellido" : "Perez", "edad" : 20 },
         { "nombre" : "Sofia","apellido" : "Ruhl", "edad" : 59 },
         { "nombre" : "Pedro","apellido" : "Ruhl", "edad" : 34 },
         { "nombre" : "Juan" ,"apellido" : "Lopez", "edad" : 19 }]

print('Lista original')
print(lista)

print('Orden por nombre')
print (sorted(lista, key=itemgetter('nombre')))

print('Orden por apellido')
print (sorted(lista, key=itemgetter('apellido')))

print('Orden por edad')
print (sorted(lista, key=itemgetter('edad')))

print('Orden por apellido y edad')
print (sorted(lista, key=itemgetter('apellido','edad')))