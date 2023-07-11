from citizen import Citizen

ciudadano1 = Citizen(1, 'rodrigo', 'peralta', 29)
ciudadano0 = Citizen(1, 'rodrigo', 'peralta', 29)
print(id(ciudadano0))
print(id(ciudadano1))
ciudadano2 = Citizen(7, 'luciana', 'paez', 28)

# print(ciudadano1 == ciudadano0)
# print(ciudadano1 == ciudadano2)
# print(ciudadano1 > ciudadano2)
print(Citizen.mayor_que(ciudadano1, ciudadano2))
