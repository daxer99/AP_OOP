while True:
    print("Ingrese A (Altas) - B (Bajas) - M (Modificaciones): ")
    opcion = input().upper()
    if opcion in ["A", "B", "M"]:
        print(opcion)
        break;