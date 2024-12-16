my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Escribe tu código aquí.
#
sinRepes = []
for i in my_list:
    if i not in sinRepes:
        sinRepes.append(i)

print("La lista con elementos únicos:")
print(sinRepes)