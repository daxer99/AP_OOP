intentos = 0
while intentos < 5:
    valor = input("Ingrese un número entero: ")
    try:
        valor = int(valor)
        print(valor)
    except ValueError:
        intentos += 1
raise ValueError("Valor incorrecto ingresado en 5 intentos")