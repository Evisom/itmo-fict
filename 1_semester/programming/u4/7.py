a1 = [2,4,6,8,10,12,14,18,20]
s = int(input('Сдвиг: '))

def shift(arr, s):
    if s > len(arr):
        print('так нельзя')
        return 
    return arr[s:] + arr[:s]

print(shift(a1,s))

a2 = input('Введите список через пробел: ')
a2 = a2.split()
s = int(input('Сдвиг: '))

print(shift(a2, s))