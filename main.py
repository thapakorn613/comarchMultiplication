#!/usr/bin/python
import toFile as toFile
import function as function
import os
os.remove("file/instruction.txt")
mcand = 6
toFile.write("  add 0   2   0")
toFile.write("  lw  2   0   mcand")
mplier = 2
toFile.write("  add 0   3   0")
toFile.write("  lw  3   0   mplier")
x1 = 0
toFile.write("  add 0   1   0")
result = int(mcand*mplier)
print ("result[x1] = " , result )
print("-----------------------------------")
sizeOfMulti = 4
toFile.write("  add 0   3   0")
toFile.write("  lw  3   0   #15#")
sizeOfProduct = 8
# initial value
x2 = function.numToBinary(mcand,sizeOfMulti) # mcand

x3 = function.numToBinary(mplier,sizeOfMulti) # mplier
result = function.numToBinary(result,sizeOfProduct) #
x1 = function.numToBinary(0,sizeOfProduct) # Product
print ("mcand  : " , x2) # x2 is mcand in bin
print ("mplier : " , x3) # x3 is mplier in bin
print ("result[Multi] : " , result)
# x1 is Product in bin
#
tempMcand = function.numToBinary(mcand,sizeOfProduct)
tempMcand = "0b" + tempMcand # no in inst
check = function.numToBinary(1,sizeOfMulti)
temp = function.numToBinary((int(x2,2)+ int(x3,2)),sizeOfMulti) # add binary
print ("--------------------------------")
for x in range ( sizeOfMulti ):
    check = function.shiftLeft("1",x) # 1 shift left x bit
    tempCheck = check.split('b')
    check = function.numToBinary(int(tempCheck[1], 2), sizeOfMulti)
    exe = function.andFunction(check,x3)
    if exe == 1:
        x1 = function.numToBinary((int(x1, 2) + int(tempMcand, 2)), sizeOfProduct)  # add
    tempMcand = tempMcand.split('b') # no in instruction
    tempMcand = function.shiftLeft(tempMcand[1],1) # shift left 1 bit

print ("Product : ",x1)
