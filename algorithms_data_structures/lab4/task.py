import random
import timeit
import sort 

print('[0] - Quick sort')
print('[1] - Comb sort')
print('[2] - Bucket sort')
print('[3] - Heap sort')
print('')
print('[4] - Сравнение сортировок с помощью timeit')

correct = False

while not correct:
    option1 = input("\n Выберите сортировку:")
    if option1 not in ["0", "1", "2", "3", "4"]:
        print("Некорректный ввод!")
    else:
        correct = True
if option1 != "4":
    correct = False 
    print('\n Выберите способ ввода')
    print('[0] Список из 10 случайных элементов')
    print('[1] Ввод вручную')
    option2 = None
    while not correct and option1.lower() != 't':
        option2 = input("\n Выберите способ:")
        if option2 not in ["0", "1"]:
            print("Некорректный ввод!")
        else:
            correct = True

    array = []
    if option2 == '0':
        for i in range(0, 10):
            array.append(random.randint(0, 100))
    elif option2 == '1':
        correct = False
        while not correct:
            array = input('Введите элементы списка через пробел: ').split()
            try:
                for i in range(len(array)):
                    array[i] = int(array[i])
                correct = True
            except:
                print("Вводите только целые числа!")
                correct = False 

    print('\nИсходный список:\n')
    print(array)
    print('\nОтсортированный список:\n')

    if option1 == '0':
        print(sort.quicksort(array))
    elif option1 == '1':
        print(sort.combsort(array))
    elif option1 == '2':
        print(sort.bucketsort(array))
    elif option1 == '3':
        print(sort.heapsort(array))
else:
    array = []
    ln = 100000
    for i in range(0, ln+1):
        array.append(random.randint(0, 1000000))
    starttime = timeit.default_timer()
    sort.quicksort(array)
    print("Quick sort - ", timeit.default_timer() - starttime)

    starttime = timeit.default_timer()
    sort.combsort(array)
    print("Comb sort - ", timeit.default_timer() - starttime)

    starttime = timeit.default_timer()
    sort.bucketsort(array)
    print("Bucket sort - ", timeit.default_timer() - starttime)


    starttime = timeit.default_timer()
    sort.heapsort(array)
    print("Heap sort - ", timeit.default_timer() - starttime)

