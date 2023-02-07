def merge(arr1, arr2):
    print(arr1, arr2)
    marr = arr1+arr2 
    marr.sort()
    return marr 


def mergeSort(arr):
    if len(arr) < 2:
        return arr 
    arr1 = arr[:len(arr)//2]
    arr2 = arr[len(arr)//2:]
    return merge(mergeSort(arr1),mergeSort(arr2))


a = [6,5,12,10,9,1]
print(a)
print(mergeSort(a))