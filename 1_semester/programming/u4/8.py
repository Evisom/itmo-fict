s = [190, 186, 185, 180, 176, 167, 160, 150]


st = True 
while st:
    n = int(input('Введите рост нового человека: (-1 если закончить) '))
    if n == -1:
        st = False
        break
    s.append(n)
    s.sort(reverse=True)
    print('Встать в строй!')
    print(s, s.index(n))

print(s)

