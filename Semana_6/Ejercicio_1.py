import sys

set1 = {"A", 1, "B", 2, "C", 3}
set2 = set('DEF456')
print(set1)
print(set2)
print("Tamaño set1: " + str(sys.getsizeof(set1)) + "bytes")
print("Tamaño set2: " + str(set2.__sizeof__()) + "bytes")

lista = [[1,2,3],[1,2,3],[1,2,3]]
tupla = [(1,2,3),(1,2,3),(1,2,3)]

print(lista.__sizeof__(), tupla.__sizeof__())