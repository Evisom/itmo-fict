arr = [1, 2, 4 ,5, 6, 7, 19 , 23 , 24 , 25 ,26 ,34 ,36 ,41 ,42 , 43, 45, 46, 50 ,51 , 53 ,54 ,56, 58, 60]

def binary_search(array, target):
    low = 0
    high = len(array) - 1
    mid = ((low + high)//2)
    c = 0
    while low < high:
        c+=1
        if target < array[mid]:
            high = mid
            mid = ((low + high)//2)
        elif target > array[mid]:
            low = mid 
            mid = ((low + high)//2)
        else:
            return [mid, c]
    return False 

print(binary_search(arr, 25))
print(arr.index(25))
