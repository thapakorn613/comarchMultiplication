#!/usr/bin/python
import toFile as function
mcand = 10383
mplier = 32766
x1 = 0
result = int(mcand*mplier)
print ("result[x1] = " , result )
print("-----------------------------------")

sizeOfMulti = 15
sizeOfProduct = 32
# initial value
x2 = function.numToBinary(mcand,sizeOfMulti) # mcand
x3 = function.numToBinary(mplier,sizeOfMulti) # mplier
result = function.numToBinary(result,sizeOfProduct) #
x1 = function.numToBinary(mplier,sizeOfProduct) # Product
print ("mcand  : " , x2) # x2 is mcand in bin
print ("mplier : " , x3) # x3 is mplier in bin
print ("result[Multi] : " , result)
print ("product : " , x1) # x1 is Product in bin
#
product = list(x1) # for check
temp = function.numToBinary((int(x2,2)+ int(x3,2)),sizeOfMulti) # add binary
print ("temp: ",temp)
x2 = x2 + function.numToBinary(0,sizeOfMulti)
zero = function.numToBinary(0,sizeOfProduct)
print ("--------------------------------")
for x in range ( sizeOfMulti ):
    print("state[", x+1, "] : ")
    if(product[ sizeOfProduct - 1 ] == '1'):
        print("1 -> PI = PI + M ")
        print("product : ", x1)
        x1 = function.numToBinary((int(x1, 2) + int(x2, 2)), sizeOfProduct)
    elif (product[ sizeOfProduct - 1 ] == '0'):
        print ("0 -> no op")
        print("product : ", x1)
        x1 = function.numToBinary(int(x1, 2) + int(zero, 2), sizeOfProduct)
    # ----- shift right
    print("Mcand : ", x2)
    # shift right 1 bit and store to x1
    x1 = bin(int(x1,base = 2) >> 1) # convert x1 to binary on form 0bxxxxxxx
    tempx1 = x1.split('b')
    x1 = function.numToBinary(int(tempx1[1],2),sizeOfProduct)
    print("Product  : ", x1)
    product = list(x1)
    print("--------------------------------")


