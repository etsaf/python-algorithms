#Bit manipulations
def getBit(num, i):
    a = num
    b = 2 ** (i - 1)
    return a & b != 0

def setBit(num, i):
    a = num
    b = 2 ** (i - 1)
    return a | b

def clearBit(num, i):
    a = num
    b = ~ (2 ** (i - 1))
    return a & b

def updateBit(num, i, v):
    a = num
    b = ~ (2 ** (i - 1))
    c = v << i
    return a & b | c