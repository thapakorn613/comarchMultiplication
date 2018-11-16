#!/usr/bin/python
import toFile as function
#f1 = 0b010111010
#f2 = bin(f1 << 1)

mcand = 2
mplier = 6
x1 = 0
result = int(mcand*mplier)
print ("result[x1] = " , x1 )
print("-----------------------------------")

indexOfM = 4
indexOfP = 8
# initial value
x2 = function.numToBinary(mcand,4)
x3 = function.numToBinary(mplier,4)
result = function.numToBinary(result,8)
x1 = function.numToBinary(mplier,8)
print ("mcand  : " , x2) # x2 is mcand in bin
print ("mplier : " , x3) # x3 is mplier in bin
print ("result[Multi] : " , result)
print ("x1 : " , x1) # x1 is Product in bin
#
product = list(x1) # for check
temp = function.numToBinary((int(x2,2)+ int(x3,2)),4) # add binary
print ("temp: ",temp)
counter = 0;
print ("--------------------------------")
for x in range(1):
    print("state[", x+1, "] : ")

    if(product[ indexOfP - 1 ] == '1'):
        print("1 ")
        print("product : ", x1)
        x2 = x2 + "0000"
        x1 = function.numToBinary((int(x1, 2) + int(x2, 2)), 8)
    elif (product[ indexOfP - 1 ] == '0'):
        print ("0")
        print("product : ", x1)
        zero = "00000000"
        tempResult = int(x1, 2) + int(zero, 2)
        x1 = function.numToBinary(tempResult, 8)
    # ----- shift right
    print("Mcand : ", x2)
    print("Product  : ", x1)
    # how to convert x1 to binary on form 0bxxxxxxx
    x1 = bin(int(x1) >> 1)
    #
    print(x1)
    tempx1 = x1.split('b')
    x1 = function.numToBinary(int(tempx1[1],2),8)
    print ("product : ",x1)
    product = list(x1)
    print("--------------------------------")


