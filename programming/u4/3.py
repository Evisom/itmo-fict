str = 'asdfew123brbb321'

n = '0123456789'
s = 0
for i in n:
    s+=str.count(i)*int(i)
print(s)