def divisionHash (string: str) -> str: 
    codes = []
    for i in string:
        codes.append(ord(i))

    # print(codes)

    l = 999983

    hash = []
    for i in codes:
        hash.append(hex(i%l)[2:])
    return "0x"+"".join(hash)

def dehash(hash: str) -> str:
    print(hash)
    hash = hash[2:]
    string = ''
    for i in range(0, len(hash), 2):
        string+=chr(int(hash[i:i+2], 16))
    print(string)
    

dehash(divisionHash(input()))