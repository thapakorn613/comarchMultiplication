
filllist = []
filllist2 = []
numline = 0


def write(code):
    f = open('file/instruction.txt', 'a')
    f.write(code + '\n')
    f.close()


def write_for_fill(code):
    f = open('file/fillcode.txt', 'w')
    for i in range(len(code)):
        if code[i] != '':
            f.write('\t' + code[i])

    f = open('file/fillcode.txt', 'r')
    s = f.readline()
    f.close()
    return s

def read_for_fill(filePath):
    file = open(filePath, 'r')
    num_lines = sum(1 for line in open(filePath))
    for i in range(num_lines):
        s = file.readline()
        if s == '':  # check file end
            break
        fill = s.rstrip().split('\t');
        if fill[1] == '.fill':
            filllist.append(fill)

def check_for_fill(fillcheck):
    for i in range(len(filllist)):
        filllist2.append(filllist[i][0])
           # return filllist[i][2]
    #print(filllist2)
    #print(fillcheck)
    if fillcheck in filllist2:
        #return  filllist2[i]
        filllist2.clear()
        #print('im here')
        for j in range(len(filllist)):
            if fillcheck == filllist[j][0]:
                return filllist[j][2]
    else: #print('ERROR Undefined Label!!!')
        return 'ERROR'
    return 'ERROR'