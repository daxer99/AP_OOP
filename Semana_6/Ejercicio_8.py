def unir_diccionarios(dict1, dict2):
    res = dict2
    (res.update(dict1))
    return res

def unir_diccionarios_2(dict1, dict2):
    res = dict1 | dict2
    return res

dict1 = {'a': 10, 'b': 8, 'c': 8}
dict2 = {'d': 6, 'c': 4, 'e': 8}

print(unir_diccionarios(dict1, dict2))
print(unir_diccionarios_2(dict1, dict2))