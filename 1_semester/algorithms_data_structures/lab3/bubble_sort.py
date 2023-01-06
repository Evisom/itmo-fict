from random import randint as rand
array = [9, 8, 7, 4, 5, 24, 1]

def bubblesort(s):
    for i in range(len(s)):
        flag = True
        for j in range(1, len(s)):
            if s[j] < s[j-1]:
                s[j-1], s[j] = s[j], s[j-1]
                flag = False
        if flag:
            return s

print(bubblesort(array))

