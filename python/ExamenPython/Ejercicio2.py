# Solicitamos una palabra al usuario
palabra = input("Introduce una palabra: ")
contA = 0
contE = 0
contI = 0
contO = 0
contU = 0

# Recorremos la palabra contando sus vocales
for i in palabra: 
    if(i == "a"):
        contA += 1
    elif(i == "e"):
        contE += 1
    elif(i == "i"):
        contI += 1
    elif(i == "o"):
        contO += 1
    elif(i == "u"):
        contU += 1

print("a: " + str(contA))
print("e: " + str(contE))
print("i: " + str(contI))
print("o: " + str(contO))
print("u: " + str(contU))