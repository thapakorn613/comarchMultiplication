#!/usr/bin/python
import toFile as toFile
import function as function
mcand = 3
mplier = 4
x3 = 0
sizeOfMulti = 15
sizeOfProduct = 32
x1 = function.numToBinary(mcand,sizeOfMulti)
x2 = function.numToBinary(mplier,sizeOfMulti)
x3 = function.numToBinary(0,sizeOfProduct)
tempMcand = function.numToBinary(mcand,sizeOfProduct)
check = function.numToBinary(1,sizeOfMulti)
for x in range ( sizeOfMulti ):
    check = function.shiftLeft("1",x)
    exe = function.andFunction(check,x2)
    if exe == 1:
        x3 = function.numToBinary((int(x3, 2) + int(tempMcand, 2)), sizeOfProduct)
    tempMcand = function.shiftLeft(tempMcand[1],1)
