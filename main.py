#!/usr/bin/python
import function as function
#f1 = 0b010111010
#f2 = bin(f1 << 1)

mcand = 32766
mplier = 10383
x1 = 0
x1 = int(mcand*mplier)
print ("result[x1] = " , x1 )
tempX2 = function.numToBinary(mcand,15)
tempX3 = function.numToBinary(mplier,15)
tempX1 = function.numToBinary(x1,32)
print ("mcand  : " , tempX2)
print ("mplier : " , tempX3)
print ("result[x1] : " , tempX1)
print("-----------------------------------")
tempMplier = str(tempX3).split('')
print("mplier",tempMplier)