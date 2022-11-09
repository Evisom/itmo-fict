a = open("transl.txt").readlines()
ru_a = []
en_a = []
for i in a:
    # print(i.split())
    ru_a.append(i.split()[0].lower())
    en_a.append(i.split()[2].lower())
# print(ru_a, en_a)

str = input("Введите строку на русском: ")
new_str = ""
for i in str:
    if i.lower() in ru_a:
        new_str+=en_a[ru_a.index(i.lower())] 
    else:
        new_str+=i
print(new_str)
