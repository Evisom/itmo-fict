flag = True 

def checkPassword(i):
    score = 0 
    alp = 'qwertyuiopasdfghjklzxcvbnm'
    alpB = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    numbers = '0123456789'
    symbols = '!@#$%^&*()_+-=?'
    if len(i) != 0:
        score += 1
    if len(i) >= 8:
        score += 2 
    big = False 
    small = False 
    for q in alp:
        if q in i:
            small = True 
            break 
    for q in alpB:
        if q in i:
            big = True 
            break 
    if small and big:
        score +=1
    for q in numbers:
        if q in i:
            score+=1
            break 
    for q in symbols:
        if q in i:
            score+=1
            break 
    return score 
    
while flag: 
    i = input('Введите пароль: ')
    if i.lower() == 'q':
        flag = False 
        break 
    score = checkPassword(i)
    
    print('Сложность пароля - ', score)