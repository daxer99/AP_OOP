def contador_vocales(string):
    count = 0
    vocales = set("aeiouAEIOU")

    for letra in string:
        if letra in vocales:
            count = count + 1

    return count


p1 = 'hola'
p2 = 'murcielago'

print(contador_vocales(p1))
print(contador_vocales(p2))