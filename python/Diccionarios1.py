tienda1 = {"manzanas": 10, "naranjas": 15, "plátanos": 5}
tienda2 = {"manzanas": 8, "naranjas": 20, "uvas": 13}
tienda3 = {}

for clave, valor in tienda1.items():
    if clave not in tienda3:
        tienda3[clave] = valor


for clave, valor in tienda2.items():
    if clave in tienda3:
        tienda3[clave] += valor
    else:
        tienda3[clave] = valor

print(tienda1)
print(tienda2)
print(tienda3)