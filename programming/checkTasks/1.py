i = True 
a = []
print('Вводите слова:')
while i:
    a.append(input())
    if len(a[len(a)-1]) == 0:
        i = False 
word = ''

for i in range(0, len(a)-1):
    word+=a[i][0]

print(word)