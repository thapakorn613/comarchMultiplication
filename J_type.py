instruction="start jalr   2   4"
#instruction="jalr   2   4"
    
def jType(instruction):
    totalWords = sum(1 for word in instruction.split() if word.isalpha())
    if(totalWords>1):
        able,command,regA,regB=instruction.split()
    else:
        command,regA,regB=instruction.split()
    regA=int(regA)
    regB=int(regB)
    regA="{0:b}".format(regA) 
    regB="{0:b}".format(regB)
    regA=str(regA)
    regB=str(regB) 
    regA=regA.zfill(3)
    regB=regB.zfill(3)
    zero = "0000000000000000"
    obcode = "101"
    zeroBack = "0000000"
    matchineCode= zeroBack + obcode + regA + regB + zero
    #print(regA,regB)
    print(matchineCode)
    return matchineCode;