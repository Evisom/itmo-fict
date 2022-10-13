import sqlite3

def select(params):
    sql = 'SELECT * FROM students WHERE '
    keys = list(params)
    print(keys)
    print(params[keys[0]])
    for i in range(len(keys)):
        sql+=keys[i] + '="' + str(params[keys[i]]) +'" and '
    sql = sql[:-4]+';'
    print(sql)
    try:
        db = sqlite3.connect('students.db')
        cursor = db.cursor()
        cursor.execute(sql)
        record = cursor.fetchall()
        cursor.close()
        db.close()
        print(record)
        return record
    except:
        print('Ошибка подключения к базе')
        return False

