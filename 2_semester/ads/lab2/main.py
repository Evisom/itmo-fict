import math 
import copy 
import binascii

def StringToArray(string: str) -> list: # Эта функция представляет строку как массив из их ASCII кодов
    arr = []
    for i in string:
        arr.append(ord(i))
    return arr 

def multiplicative_hash(arr: list) -> list: # Функция для хэширования методом умножения
    M = len(arr) 
    C = (5**(1/2)-1)/2 # Оптимальная константа которую вывел Дональд Кнут
    arr = StringToArray(arr)
    hash = []
    for i in arr: # Хэшируем каждую букву
        h = round(M*((i*C)%1))
        hash.append(str(h))
    hash = "".join(hash) # Объединяем получившийся массив в одну строку
    return hash 



def crc32(string: str) -> str:
    message = ''
    for i in string:
        message+=bin(ord(i))[2:]
    g = '100110000010001110110110111' # 0x04C11DB7 
    message = message + '0'*(len(g)-1)

    block = message[0:len(g)]
    i = len(g) - 1
    while i < len(message):
        block = bin(int(block, 2) ^ int(g, 2))[2:]
        while len(block) < len(g):
            i+=1
            if i < len(message):
                block+=message[i]
            else:
                return hex(int(block,2))
            
def MD5_hash(string: str) -> str:
    # эх если бы мне читали лекции по алгоритмам

    # Функции F, G, H, I - функции для каждого раунда
    # Используем побитовые логические операции
    def F(x: int,y: int,z: int) -> int: 
        result = (x & y | ~x & z)
        return result 
    
    def G(x: int,y: int,z: int) -> int: 
        result = x & z | y & ~z 
        return result 
    
    def H(x: int,y: int,z: int) -> int: 
        result = x ^ y ^ z
        return result 
    
    def I(x: int,y: int,z: int) -> int: 
        result = y ^ (x | ~ z)
        return result 
    
    def addition(x: int,y: int, m=2**32) -> int: # Функция для сложения по модулю 2**32
        z = (x+y) % m 
        return z 

    def shift(x: int, s: int) -> int: # Функция для битового сдвига
        x = bin(x)[2:]
        x = x[s:] + x[:s]
        return int(x,2)
    

    # Ниже мы составим строку из 16тиричных представлений ASCII кодов каждого символа 
    message = ''
    for i in string:
        message+=hex(ord(i))[2:] #

    length = str(hex(len(message)*4)) # Сохраним длину исходной строки в битах
    message += '8' # Добавим 1 в конце (8_16 = 1000_2)
    message += ('0' *(112 - len(message)%128 +4)) # Добавим нули в конец
    message= message + '0' * (16-len(length)) + length[2:] # Сформируем сообщение длинной 512 бит
    
    buffers = [ # Буферы с их начальными значениями 
        0x12AC2375, # A
        0x3B341042, # B
        0x5F62B97C, # C
        0x4BA763E   # D
    ]

    S = [ # Значения дли сдвигов в каждом раунде
        [7,12,17,22],
        [5,9,14,20],
        [4,11,16,23],
        [6,10,15,21]
    ]

    P = [F, G, H, I] # Для удобства массив с функциями для каждого раунда

    T = [] # Константы  
    for i in range(1,65):
        T.append(round(2**32 * abs(math.sin(i))))

    blocks = []
    for i in range(2, len(message), 128): # Разобьем сообщение на блоки длинной 512 бит
        blocks.append(message[i:i+128])
    
    for b in range(0, len(blocks)): # Разобьем каждый 512битный блок на 16 32х битных блоков
        block = copy.deepcopy(blocks[b])
        blocks[b] = []
        for i in range(0, 128, 8):
            blocks[b].append(int(block[i:i+8], 16))


    iteration = 0
    for b in range(0, len(blocks)): # Перебираем каждый 512 битный блок 
        for r in range(0, 4): # 4 раунда
            for i in range(0, len(blocks[b])): # Перебираем каждый из 16ти 32х битных блоков
                bufferCopy = copy.deepcopy(buffers) # Копируем начальные значения буфера
                processFunction = P[r](buffers[1], buffers[2], buffers[3]) # Получаем значение для фукнции текущего раунда
                buffers[0] = addition(buffers[0], processFunction) # Добавляем значение функции к буферу А
                buffers[0] = addition(buffers[0], blocks[b][i]) # Добавляем значение текущего 32х битного блока к буферу А
                buffers[0] = addition(buffers[0], T[iteration]) # Добавляем соответствующую константу к буферу А
                buffers[0] = shift(buffers[0], S[r][i%4]) # Делаем побитовый сдвиг для буфера А
                # Константы которые хранятся в массиве S я нагуглил 
                # Они рассчитаны каким-то умным путем, но дано всего 16 констант
                # Каждые 4 константы для каждого из 4х раундов, но в каком порядке их использовать я не разобрался
                # Тут я использую константу по i%4, так как посчитал, что так логичнее всего
                buffers[0] = addition(buffers[0], bufferCopy[0]) # Добавляем к буферу А изначальное значение буфера А
                buffers = buffers[3:4] + buffers[0:3] # Перемещаем наши буферы (ABCD => DABC => CDAB => BCDA => ABCD)
                iteration+=1 # Счетчик итераций чисто что бы константы T прибавлять легче было 

    # По результату выполнения кода выше имеем наш хэш в массиве buffers в десятиричной системе счисления


    hex_string = '0x'
    for i in buffers: # Проходимся по всем буферам
        hi = hex(i)[2:] # Перевод из 10 в 16 систему счисления
        if len(hi) < 8: # Проверяем если не хватает нулей в конце, если что добавляем
            hi = '0'*(8-len(hi)) + hi 
        hex_string+=hi 

    return hex_string # Возвращаем наш хэш в шестнадцатиричном формате
    
text = input()
print('Multiplicative hash: ', multiplicative_hash(text))
print('MD5 hash: ', MD5_hash(text))
print('CRC32 hash: ', crc32(text))