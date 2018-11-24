#!/usr/bin/python
import toFile as toFile
import function as function
import os
os.remove("file/instruction.txt")
mcand = 3
mplier = 4
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
x1 = function.numToBinary(0,sizeOfProduct) # Product
print ("mcand  : " , x2) # x2 is mcand in bin
print ("mplier : " , x3) # x3 is mplier in bin
print ("result[Multi] : " , result)
tempMcand = function.numToBinary(mcand,sizeOfProduct)
tempMcand = "0b" +   tempMcand # no in inst
check = function.numToBinary(1,sizeOfMulti)
print ("--------------------------------")
for x in range ( sizeOfMulti ):
    check = function.shiftLeft("1",x) # 1 shift left x bit
    tempCheck = check.split('b')
    check = function.numToBinary(int(tempCheck[1], 2), sizeOfMulti)
    exe = function.andFunction(check,x3) # x3 and x4
    if exe == 1:
        x1 = function.numToBinary((int(x1, 2) + int(tempMcand, 2)), sizeOfProduct)  # add
    tempMcand = tempMcand.split('b') # no in instruction
    tempMcand = function.shiftLeft(tempMcand[1],1) # shift left 1 bit
print ("Product : ",x1)
