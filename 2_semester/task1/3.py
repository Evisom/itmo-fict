import random 

suits = ['♤', '♡', '♢', '♧']
cards_type = ['6', '7']
# cards_type = ['6', '7', '8', '9', '10', 'J', 'Q', 'K' , 'T']
cards = []


def randomArray(arr):
    rarr = []
    while len(arr) > 0:
        r = random.randint(0, len(arr)-1)
        rarr.append(arr[r])
        arr.pop(r)
    return rarr 

def printMap(arr):
    for i in range(0, len(arr)):
        print(arr[i], end=" ")
        if (i+1) % len(cards_type) == 0:
            print()

def hideMap(arr):
    j = 0
    mp = []
    for i in range(len(arr)):
        if (i+1) % len(cards_type) == 0:
            j+=1
        if arr[i] != 'X':
            mp.append(str(j) + str((i+1) % len(cards_type)))
        else:
            mp.append('X')
    return mp 

def getIndex(n):
    x = int(n[0])
    y = int(n[1])
    index = x * len(cards_type) + y -1
    return index

for i in suits:
    for j in cards_type:
        cards.append(i+j)

cards = randomArray(cards)
printMap(cards)
print()
hidemap = hideMap(cards)
printMap(hidemap)




while cards.count('X') != len(cards):
    print()
    card1 = getIndex(input('Card1: '))
    card2 = getIndex(input('Card2: '))
    if cards[card1][1] == cards[card2][1]:
        cards[card1] = 'X'
        cards[card2] = 'X'
    else:
        print('\n Wrong')
        print(cards[card1], cards[card2], '\n')
    hidemap = hideMap(cards)
    printMap(hidemap)
    