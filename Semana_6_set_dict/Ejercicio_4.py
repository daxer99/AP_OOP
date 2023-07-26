def discriminador_frases_por_vocales(string):
    string = string.lower()
    vocales = set("aeiou")
    s = set({})

    for char in string:
        if char in vocales:
            s.add(char)

    if len(s) == len(vocales):
        print("Frase aceptada")
    else:
        print("Frase denegada")


frase1 = 'Hola mundo'
discriminador_frases_por_vocales(frase1)

frase2 = 'Hola murcielago'
discriminador_frases_por_vocales(frase2)