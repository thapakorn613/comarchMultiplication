import function as convert
def create_register(num):
    num = int(num)
    keepnum = ""
    for i in range(3):
        if ((num >> i) & 1 == 1):
            keepnum += '1'
        else:
            keepnum += '0'
    return keepnum[::-1]

def create_machine(case, num1, num2, num3):
    zero = "0000000"
    if case == "add":
        opcode = "000"
    elif case == "nand":
        opcode = "001"
    othernum = "0000000000000"
    alll = zero + opcode + num2 + num1 + othernum + num3
    return alll



def rType(instruction):
    name = ""
    name += instruction
    keep_type = ""
    num1 = ""
    num2 = ""
    num3 = ""
    num = name.find('\t')
    # start add x1 x2 x3
    for i in range(len(name)):
        if (name[num + i] != '\t'):
            num = num + i
            break;


    nums = name.find('\t', num + 1)

    for i in range(nums - num):
        keep_type = keep_type + name[i + num]

    for i in range(len(name)):
        if (name[nums + i] != '\t'):
            num = nums + i
            break;

    for i in range(len(name)):
        if (name[num + i] == '\t'):
            nums = num + i
            break;

    keep1 = num
    for i in range((nums - num)):
        num1 += name[num]
        keep1 = keep1 + 1

    for i in range(len(name)):
        if (name[nums + i] != '\t'):
            num = nums + i
            break;

    for i in range(len(name)):
        if (name[num + i] == '\t'):
            nums = num + i
            break;

    keep2 = num
    for i in range((nums - num)):
        num2 += name[num]
        keep2 = keep2 + 1

    for i in range(len(name)):
        if (name[nums + i] != '\t'):
            num = nums + i
            break;

    nums = len(name)
    for i in range(len(name)):
        if (name[nums - 1] != '\t'):
            break;
        nums = nums - 1

    keep3 = num

    for i in range((nums - num)-1):
        num3 += name[num]
        keep3 += 1
    tempnum3 = int(num3)
    tempnum2 = int(num2)
    tempnum1 = int(num1)
    num3 = convert.numToBinary(tempnum3, 3)
    num2 = convert.numToBinary(tempnum2, 3)
    num1 = convert.numToBinary(tempnum1, 3)

    return create_machine(keep_type, num1, num2, num3)

#run_R_type("start      nand      55  22  33    ")