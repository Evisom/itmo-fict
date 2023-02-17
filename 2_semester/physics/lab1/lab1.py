file = open('lab1.txt').readlines()
data = []
for i in file: 
    data.append(float(i[0:-1]))


avg = sum(data)/len(data)
T = []
T2 = []

for i in range(0, len(data)):
    T.append(data[i] - avg)

for i in range(0, len(data)):
    T2.append(T[i]**(2))

G = (sum(T2)/(len(data)-1))**(1/2)
print(T)
print(T2)

print(G)