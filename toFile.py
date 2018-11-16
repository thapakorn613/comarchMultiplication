
filllist = []

def numToBinary(n,rangeOffbit):
    result = ''
    for x in range(rangeOffbit):
        r = n % 2
        n = n // 2
        result += str(r)
    result = result[::-1]
    return result

def write(code):
    f = open('file/MachineCode.txt', 'a')
    f.write(code + '\n')
    f.close()

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