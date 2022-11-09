end = False 
arr = []
i = 0
while not end:
    print('Введите '+ str(i) + ' элемент списка')
    el = input()
    try:
        el = float(el)
        arr.append(el)
        i+=1
    except:
        if el == 'Q':
            end = True 
            break
        else:
            print('Элемент должен быть числом!')

print('Количество элементов -', len(arr))
print('Сумма -',sum(arr))
print('Cреднее -',(sum(arr)/len(arr)))
print('Минимальное значение:', min(arr) ,' с индексом ' , arr.index(min(arr)))
print('Максимальное значение:' , max(arr) , ' с индексом ' , arr.index(max(arr)))
arr2 = arr[arr.index(min(arr))+1:arr.index(max(arr))]
arr3 = arr[arr.index(max(arr))+1:arr.index(min(arr))]
# print(arr2,arr3)
if len(arr2) > 1:
    p = arr2[0]
else:
    p = arr3[0]
    arr2 = arr3
# print(arr2)
# print(i)
for i in range(1, len(arr2)):
    p=p*arr2[i]
print('Произведение между минимальным и максимальным:', p)

