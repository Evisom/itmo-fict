def getExt(filename):
    filename = filename.split('.')
    if len(filename) == 1:
        return "У файла нет расширения" 
    else:
        return filename[-1]

print(getExt(input('Введите имя файла: ')))        