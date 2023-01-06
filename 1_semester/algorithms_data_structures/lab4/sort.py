def quicksort(array):

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quicksort(less)+equal+quicksort(greater)
    else:
        return array


def combsort(array):
    gap=len(array)
    swapped = True
    temp=0
    while gap!=1 or swapped == True:
        swapped=False
        gap = int(gap/1.3)
        if gap < 1:
            gap=1
        for i in range(0, len(array)-gap): 
            if array[i] > array[i + gap]:
                temp=array[i]
                array[i]=array[i + gap]
                array[i + gap]=temp
                swapped = True


def bucketsort(array):
    largest = max(array)
    length = len(array)
    size = largest / length
    buckets = [[] for i in range(length)]
    for i in range(length):
        index = int(array[i] / size)
        if index != length:
            buckets[index].append(array[i])
        else:
            buckets[length - 1].append(array[i])
    for i in range(len(array)):
        buckets[i] = sorted(buckets[i])
    result = []
    for i in range(length):
        result = result + buckets[i]

    return result


def heapify(arr, n, i):
    largest = i 
    l = 2 * i + 1  
    r = 2 * i + 2  

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i] 
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)

    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] 
        heapify(arr, i, 0)
    return arr