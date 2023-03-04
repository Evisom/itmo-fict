import math 
import copy 

def StringToArray(string: str) -> list:
    arr = []
    for i in string:
        arr.append(ord(i))
    return arr 


def multiplicative_hash(arr: list) -> list:
    M = len(arr)
    C = (5**(1/2)-1)/2
    arr = StringToArray(arr)
    hash = []
    for i in arr:
        h = round(M*((i*C)%1))
        hash.append(str(h))
    hash = "".join(hash)
    return hash 

def MD5_hash(string: str) -> bytearray:
    # эх если бы мне читали лекции по алгоритмам

    # Round functions
    def F(x,y,z): 
        x = int(x, 2)
        y = int(y, 2)
        z = int(z, 2)
        return bin(x & y | ~x & z).replace("-","")[2:]
    
    def G(x,y,z):
        x = int(x, 2)
        y = int(y, 2)
        z = int(z, 2)
        return bin(x & z | y & ~z ).replace("-","")[2:]
    
    def H(x,y,z):
        x = int(x, 2)
        y = int(y, 2)
        z = int(z, 2)
        return bin(x ^ y ^ z).replace("-","")[2:]
    
    def I(x,y,z):
        x = int(x, 2)
        y = int(y, 2)
        z = int(z, 2)
        return (bin(y ^ (x | ~ z))).replace("-","")[2:]
    
    def addition(x,y, m=2**32):
        x = int(x, 2)
        y = int(y, 2)
        z = (x+y) % m 
        return bin(z)[2:]

    def shift(x, s):
        x = int(x, 2)
        return bin(x<<2).replace("-","")[2:]


    # 512 bits 
    # 448 bits - body 
    # 64 - length 
    
    message = bin(0)
    
    for i in string:
        message+=bin(ord(i))[2:]
    message+=bin(1)[2:]
    message+= (bin(0)[2:]*(448 - len(message)%512 + 2))
    length = bin(len(message)-2)[2:]
    message = message + (bin(0)[2:] * (64 - len(length))) + length
    message = message[2:]
    
    # Buffers 
    A = bin(1732584193)[2:]
    B = bin(4023233417)[2:]
    C = bin(2562383102)[2:]
    D = bin(10325476)[2:]
    buffers = [A, B, C, D]

    S = [ # Shift values
        [7,12,17,22],
        [5,9,14,20],
        [4,11,14,23],
        [6,10,15,21]
    ]

    P = [F, G, H, I]

    T = [] # Constants 

    for i in range(1,65):
        T.append(bin(round(2**32 * abs(math.sin(i))))[2:])

    iteration = 0
    for b in range(0, len(message), 512):
        block512 = (message[b:b+513])
        for r in range(0, 4):
            for i in range(0, 16):
                block = (block512[i*16:i*16+17])
                bufferCopy = copy.deepcopy(buffers)
                processResult = P[r](buffers[1], buffers[2], buffers[3]) 

                buffers[0] = addition(buffers[0], processResult)
                buffers[0] = addition(buffers[0], block)
                buffers[0] = addition(buffers[0], T[iteration-1])
                buffers[0] = shift(buffers[0], S[r][i%4])
                buffers[0] = addition(buffers[0], buffers[1])

                buffers = buffers[3:4] + buffers[0:3]
                iteration+=1

    hex_string = hex(int("".join(buffers), 2))

    return hex_string

text = input()
print('Multiplicative hash: ', multiplicative_hash(text))
print('MD5 hash: ', MD5_hash(text))
