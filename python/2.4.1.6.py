linea1 = "# ### ### # # ### ### ### ### ### ###"
linea2 = "#   #   # # # #   #     # # # # # # #"
linea3 = "# ### ### ### ### ###   # ### ### # #"
linea4 = "# #     #   #   # # #   # # #   # # #"
linea5 = "# ### ###   # ### ###   # ### ### ###"

num = int(input("Introduce un número: "))

arr = [int(i) for i in str(num)]

output1 = ""
output2 = ""
output3 = ""
output4 = ""
output5 = ""

for i in range(len(str(num))):
    if arr[i] == 1:
        output1 += linea1[0:2] + " "
        output2 += linea2[0:2] + " "
        output3 += linea3[0:2] + " "
        output4 += linea4[0:2] + " "
        output5 += linea5[0:2] + " "

    elif arr[i] == 2:
        output1 += linea1[2:5] + " "
        output2 += linea2[2:5] + " "
        output3 += linea3[2:5] + " "
        output4 += linea4[2:5] + " "
        output5 += linea5[2:5] + " "

    elif arr[i] == 3:
        output1 += linea1[5:9] + " "
        output2 += linea2[5:9] + " "
        output3 += linea3[5:9] + " "
        output4 += linea4[5:9] + " "
        output5 += linea5[5:9] + " "

    elif arr[i] == 4:
        output1 += linea1[9:13] + " "
        output2 += linea2[9:13] + " "
        output3 += linea3[9:13] + " "
        output4 += linea4[9:13] + " "
        output5 += linea5[9:13] + " "

    elif arr[i] == 5:
        output1 += linea1[13:17] + " "
        output2 += linea2[13:17] + " "
        output3 += linea3[13:17] + " "
        output4 += linea4[13:17] + " "
        output5 += linea5[13:17] + " "

    elif arr[i] == 6:
        output1 += linea1[17:21] + " "
        output2 += linea2[17:21] + " "
        output3 += linea3[17:21] + " "
        output4 += linea4[17:21] + " "
        output5 += linea5[17:21] + " "

    elif arr[i] == 7:
        output1 += linea1[21:25] + " "
        output2 += linea2[21:25] + " "
        output3 += linea3[21:25] + " "
        output4 += linea4[21:25] + " "
        output5 += linea5[21:25] + " "

    elif arr[i] == 8:
        output1 += linea1[25:29] + " "
        output2 += linea2[25:29] + " "
        output3 += linea3[25:29] + " "
        output4 += linea4[25:29] + " "
        output5 += linea5[25:29] + " "

    elif arr[i] == 9:
        output1 += linea1[29:33] + " "
        output2 += linea2[29:33] + " "
        output3 += linea3[29:33] + " "
        output4 += linea4[29:33] + " "
        output5 += linea5[29:33] + " "
        
    else:
        print("Invalid number")

print(output1)
print(output2)
print(output3)
print(output4)
print(output5)