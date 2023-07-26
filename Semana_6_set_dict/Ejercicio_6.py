def sumar_valores_dict_1(diccionario):
    sum = 0
    for i in diccionario:
        sum = sum + diccionario[i]
    return sum

def sumar_valores_dict_2(diccionario):
     sum = 0
     for i in diccionario.values():
         sum = sum + i
     return sum

my_dict_1 = {'a': 10, 'b':20, 'c':30}
print("Suma :", sumar_valores_dict_1(my_dict_1))

my_dict_2 = {'a': 1, 'b': 2, 'c': 3}
print("Suma :", sumar_valores_dict_2(my_dict_2))