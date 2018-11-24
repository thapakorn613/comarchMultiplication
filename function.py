import toFile as toFile
def numToBinary(n,rangeOffbit):
    result = ''
    for x in range(rangeOffbit):
        r = n % 2
        n = n // 2
        result += str(r)
    result = result[::-1]
    return result

def binToDecimal(str):
    n = 0
    temp = 0
    sum = 0
    str_exe = list (str)
    for x in reversed(str_exe):
        if x == "1":
            temp = 2 ** n
        elif x == "0":
            temp = 0
        sum = sum + temp
        n = n + 1
    return sum

def andFunction(a,b): # ไม่ต้องนำไปทำใน inst
    tempA = list(a)
    tempB = list(b)
    sum = 0
    for x in range(len(a)):
        if (int(tempA[x]) and int(tempB[x]) ) == 1:
            sum = sum + 1
        elif (int(tempA[x]) and int(tempB[x]) ) == 0:
            sum =  sum + 0
    return sum

def shiftLeft(str, num):
    tempNum = binToDecimal(str)
    toFile.write("  add  8   8   8")  # == == == == == == == == == == ==
    if (num == 1):
        tempNum = tempNum + tempNum
    else :
        for x in range(num ):
            tempNum = tempNum + tempNum
    return bin(tempNum)
# ---------------- Error check ------------------
# not complete all
def error_detect(mchcodee):
    listop = ['000','001','010','011','100','101','110','111']

    if len(mchcodee)!= 32:
        print('ERROR Machinecode out of bound!!!')
    elif mchcodee[7:10] not in listop: # opcode check
        print('ERROR Opcode not found!!!')
    elif mchcodee[0:7] != '0000000': # bit 25-31 is 0
        print('ERROR syntax error!!!!')
    else:
        print('Anything is pass!!!')

def isint(value):
    try:
        int(value)
        return True
    except ValueError:
        return False