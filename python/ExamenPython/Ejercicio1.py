num = int(input("Introduce un número entero: "))
capicua = False

if num % 10 == num % 100000:
    capicua = True
elif num % 100 == num % 10000:
    capicua = True
else:
    capicua = False

if capicua:
    print("El número " + str(num) + " es capicúa")
else:
    print("El número " + str(num) + " no es capicúa")







