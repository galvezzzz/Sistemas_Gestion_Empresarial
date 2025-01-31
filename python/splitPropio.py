def mysplit(strng):

    cont = 0
    arr = []

    for i in range(len(strng)):
        if i.isspace():
            cont += 0
        else:
            arr[cont] = i
            cont += 1
        

print(mysplit("Ser o no ser, esa es la pregunta"))
print(mysplit("Ser o no ser,esa es la pregunta"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
