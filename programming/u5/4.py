def strToBin(string):
    binStr = ''
    for i in string:
        binSymb = (bin(ord(i))[2:])
        if len(binSymb) < 8:
            binSymb = '0'*(8-len(binSymb)) + binSymb
        binStr+=binSymb
    return binStr

def binToStr(binStr):
    string = ''
    for i in range(0, len(binStr), 8):
        string += (chr(int(binStr[i:i+8], 2)))
    return string

def crypt(string, key):
    string = strToBin(string)
    key = strToBin(key)
    cryptedString = ''
    for i in range(len(string)):
        keysymb = i % len(key)
        cryptedString+= str( int(string[i]) ^ int(key[keysymb]) )
    return(binToStr(cryptedString))

string = input("Введите строку: ")
key = input("Введите ключ: ")

print("Результат: " , crypt(string, key))
print("Обратная расшифровка -", crypt(crypt(string, key), key ))
