def bitwiseOperation(binary,mask='',operation=''):
    list1 = []
    list2 = []
    for char in binary:
        list1.append(char)
    for char in mask:
        list2.append(char)
    new = ''
    for i in range(len(list1)):
        new += eval(f'{operation}(list1[i],list2[i])')
    return new

def AND(bit1,bit2):
    if (bit1 == '1') and (bit1 == bit2):
        return '1'
    else:
        return '0'
    
def XOR(bit1,bit2):
    if bit1 != bit2:
        return '1'
    else:
        return '0'
    
def OR(bit1,bit2):
    if (bit1 == '1') or (bit2 == '1'):
        return '1'
    else:
        return '0'
    
print(Vernan_decode('10000001','11111111','AND'))