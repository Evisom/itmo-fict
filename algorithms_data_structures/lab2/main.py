import sqlite3
import random  

def select(params):
    if params == {}:
        sql = 'SELECT * FROM students'
    else:
        sql = 'SELECT * FROM students WHERE '
        keys = list(params)
        for i in range(len(keys)):
            sql+=keys[i] + '="' + str(params[keys[i]]) +'" and '
        sql = sql[:-4]+';'
    try:
        db = sqlite3.connect('students.db')
        cursor = db.cursor()
        cursor.execute(sql)
        record = cursor.fetchall()
        cursor.close()
        db.close()
        return record
    except:
        print('Ошибка подключения к базе')
        return False

questions = [
    ["Студент девочка?", "girl"],
    ["Студенту 18 лет?", "is18"],
    ["Студент носит очки?", "glasses"],
    ["У студента карие глаза?", "brownEyes"],
    ["У студента темные волосы?", "darkHair"],
    ["У студента есть брат или сестра?", "siblings"],
    ["У стадента есть домашнее животное?", "pet"],
    ["Студент из Санкт-Петербурга?", "fromSPb"],
    ["У студента iPhone?", "iphone"],
    ["У студента практик по линейной алгебре Тушавин?", "tushavin"],
    ["Студенту больше нравится кофе, чем чай?", "coffe"],
    ["Студенту нравится больше домашняя еда, чем фастфуд?", "homefood"],
    ["Студент носит часы?", "watch"],
    ["Имя студента начинается с гласной?", "nameVowel"],
    ["Студент любит больше пиццу, чем суши?", "pizza"],
    ["Студент курит?", "smoke"],
    ["Рост студента больше 175", "heightOver175"],
    ["У студента есть вторая половинка?", "partner"],
    ["Студент родился зимой или весной?", "winterOrSpring"],
    ["Студент играет в кс или доту?", "gaming"],
    ["Студент живет в общежитии?", "campus"],
    ["Студент любит больше фильмы, чем сериалы?", "movies"],
    ["Студент смотрит аниме?", "anime"],
]


def inp(q):
    a = input(q + ' [Y/N]: ')
    while a.lower() not in ['y', 'n']:
        print('Некорректный ввод!')
        a = input(q + ' [Y/N]: ')
    if a.lower() == 'y':
        return True
    else:
        return False


flag = True
params = dict()
prev_res = select({})
print('\nЗагадайте любого студента из группы К3121')
print('Программа будет задавать вопросы и попытается угадать!\n')
while len(questions) > 0 and flag:
    i = random.randint(0, len(questions)-1)
    params[questions[i][1]] = str(inp(questions[i][0]))
    questions.remove(questions[i])
    res = select(params)
    if len(res) == 1:
        print('\nСтудент нашелся!')
        print('Его имя - ' + res[0][1])
        flag = False
    elif len(res) == 0:
        print('\nТакого студента не существует!')
        if len(prev_res) == 1:
            print('Самый похожий студент - ' + prev_res[0][1])
            flag = False
        else:
            s = ''
            for q in range(len(prev_res)):
                s+=prev_res[q][1]+', '
            s = s[:-2]
            print('Самые похожие студенты - '+ s)
            flag = False
    prev_res = res
