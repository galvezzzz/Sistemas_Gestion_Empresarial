#1er Ejercicio

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


#2o Ejercicio

generos = {
    "realismoMagico": ["Cien años de soledad"],
    "drama": ["Cien años de soledad",  "1984"],
    "fantasia": ["El señor de los anillos"],
    "aventura": ["Don Quijote",  "El señor de los anillos"],
    "distopia": ["1984"],
    "politica": ["1984"],
    "clasico": ["Don Quijote"],
    }

generos_invertido = {}

for valores in generos.values():
    for valor in valores:
        if valor not in generos_invertido.keys():
            generos_invertido[valor] = []

for clave in generos.keys():
    for valores in generos[clave]:
        generos_invertido[valores].append(clave)
        

print(generos_invertido)

