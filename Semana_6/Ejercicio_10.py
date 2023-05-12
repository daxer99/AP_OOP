lugares = {("31°44′S", "60°32′W"): "Paraná",
           ("34°35′59″S", "58°22′55″W"): "Buenos Aires",
           ("22°54′41″S", "43°12′21″W"): "Rio de Janeiro"}

print(lugares)
print('\n')

latitud = []
longitud = []
ciudad = []
for i in lugares:
    latitud.append(i[0])
    longitud.append(i[1])
    ciudad.append(lugares[i[0], i[1]])

print(latitud)
print(longitud)
print(ciudad)

print('coordenadas')
coordenadas = list(zip(latitud, longitud))
print(coordenadas)