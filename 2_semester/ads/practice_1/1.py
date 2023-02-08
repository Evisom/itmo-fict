def merge(arr1, arr2, i):
    marr = arr1+arr2 
    marr.sort()
    print(marr)
    return marr 

def mergeSort(arr, i):
    if len(arr) < 2:
        return arr 
    arr1 = arr[:len(arr)//2]
    arr2 = arr[len(arr)//2:]
    print(arr1, arr2)
    return merge(mergeSort(arr1,i+1),mergeSort(arr2, i+1), i+1)


a = [6,5,12,10,9,1] 
mergeSort(a, 0)


