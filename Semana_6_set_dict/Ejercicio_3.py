def elemento_comun(lista1, lista2):
    a_set = set(lista1)
    b_set = set(lista2)
    if (a_set & b_set):
        return True
    else:
        return False


lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = [1, 6, 7]

print(elemento_comun(lista1, lista2))
print(elemento_comun(lista1, lista3))
print(elemento_comun(lista2, lista3))