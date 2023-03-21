arr = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
# arr = [[2, 11], [0, 17], [6, 9], [7, 9], [1, 15], [0, 12], [5, 11], [6, 10], [0, 10], [1, 11]]
# for i in range(0, len(arr)):
    # carr[i] = arr[i][::-1]
    
# [[10, 0], [12, 0], [11, 1], [11, 2], [17, 0], [15, 1], [9, 6], [9, 7], [10, 6], [11, 5]]
order = []
mn = [9999, 0]

for i in arr:
    if i[1] == 0 and i[0] < mn[0]:
        mn = i 
order.append(mn)
arr.remove(mn)

h = [order[0][0]]

def m(n):
    c = 0
    for i in h:
        if i >=      n:
            c+=1
    return c 

while len(arr) != 0:
    c = []
    for i in arr:
        if m(i[0]) == i[1]:
            c.append(i)
    mn = [9999, 0]
    for i in c:
        if i[0] < mn[0]:
            mn = i
    order.append(mn)
    h.append(mn[0])    
    arr.remove(mn)
    

print(order)

