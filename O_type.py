def oType (assembly):
    zero = "00000000"
    zeroOfInstruction = "000000000000000000000"
    temp_inst = assembly.split('\t')
    inst = (str(temp_inst[1])).split('\n')
    if ( inst[0] == 'halt'):
        opcode = '110'
    elif ( inst[0] == 'noop'):
        opcode = '111'
    else:
        opcode = 'error'
    MachineCode = zero + opcode + zeroOfInstruction
    return MachineCode



