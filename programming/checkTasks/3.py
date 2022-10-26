import random 

arr1 = []
arr2 = []
m1 = 25
for i in range(25):
    arr1.append(random.randint(1, 51))
# print(arr1)
for i in arr1:
    if i >= m1:
        arr2.append('High')
    else:
        arr2.append('Low')

# print(arr2)


alp = list('йцукенгшщзхфывапролджэячсмитьбю')
alp.sort()
# print(alp)
names = []
for i in range(50):
    names.append(alp[random.randint(0,len(alp)-1)] + alp[random.randint(0,len(alp)-1)] + alp[random.randint(0,len(alp)-1)] + alp[random.randint(0,len(alp)-1)] + alp[random.randint(0,len(alp)-1)] + alp[random.randint(0,len(alp)-1)] + alp[random.randint(0,len(alp)-1)])
print(names)

names1 = []
names2 = []
print(alp)

for i in names:
    if alp.index(i[0]) <= alp.index('к'):
        names1.append(i)
    else:
        names2.append(i)

print(names1)
print(names2)
