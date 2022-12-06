def fib(c):
    arr = [0, 1]
    for i in range(1, c):
        arr.append(arr[i]+arr[i-1])
    return arr 


print(fib(int(input('Введите порядок элемента: '))))    