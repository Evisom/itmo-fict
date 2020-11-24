names=[]
for i in range(17):
    names.append('name'+str(i))
    

def chooseLead(arr, k):
    # arr - список людей стоящих кругу
    # k - шаг 

    while len(arr) != 1:
        d = k % len(arr)
        if d == 0:
            d = len(arr)

        del arr[d - 1]
        d -= 1
        arr = arr[d:] + arr[:d] 
                  
        
    return arr


print(chooseLead(names,16))