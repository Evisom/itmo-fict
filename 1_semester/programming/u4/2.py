str = input("Введите строку: ")
str = list(str)

for i in range(len(str)):
    if str[i] == str[i].lower():
        str[i] = str[i].upper()
    else:
        str[i] = str[i].lower()
str = "".join(str)
print(str)