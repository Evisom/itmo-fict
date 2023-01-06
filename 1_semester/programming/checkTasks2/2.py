from random import randint 

def randomList(ln):
    # ln - кол-во элементов
    l = []
    for i in range(ln):
        l.append(randint(0, 30))

    errorCount = randint(1, len(l))

    for i in range(errorCount):
        l[randint(0, len(l)-1)] = None
    return l 


def getAverage(arr):
    # arr - список измерений
    clean_arr = []
    for i in arr: 
        if i: 
            # записываем в новый список элементы не равные None 
            clean_arr.append(i)
    print(clean_arr)
    return round(sum(clean_arr)/len(clean_arr),2)


print(getAverage(randomList(10)))