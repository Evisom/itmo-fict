logins = [
    'root',
    'dmitriy'
]

access = False 

while not access:
    l = input('Введите логин:')
    if not(l in logins):
        a = input('Хотите добавить логин '+ l + ' в разрешенный список? [y/n]')
        if a.lower() == 'y':
            logins.append(l)
    else:
        print('Доступ разрешен')
        access = True
print(logins)