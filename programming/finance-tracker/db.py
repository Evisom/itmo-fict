import sqlite3

keys = ['name', 'cost', 'date', 'categories']

def db_init():
    sql = [
        'CREATE TABLE transactions (\
            tr_id INTEGER PRIMARY KEY,\
            product_name TEXT NOT NULL,\
            cost INTEGER NOT NULL,\
            date INTEGER NOT NULL,\
            categories TEXT NOT NULL\
        );'
    ]
    for i in sql:
        request(i)

def request(sql):
    print(sql)
    try:
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        cursor.execute(sql)
        response = cursor.fetchall()
        cursor.close()
        db.commit()
        db.close()
        return response or True
    except ValueError:
        print(ValueError)
        return False

def db_write(data):
    for i in list(data.keys()):
        if i not in keys:
            return False 
    sql = 'INSERT INTO transactions (product_name, cost, date, categories)VALUES('
    for i in keys:
        sql+='"' + str(data[i]) + '",'
    sql = sql[0:-1] + ');'

    print(sql)
    if request(sql):
        return True 
    else: return False

def db_readAll():
    return request('SELECT * FROM transactions')

def db_delete(data):
    if 'id' in list(data.keys()):
        sql = 'DELETE FROM transactions WHERE tr_id = ' + str(data['id']) +';'
        if request(sql): return True 
        else: return False 
    return False

def db_getCategories():
    return request('SELECT DISTINCT categories FROM transactions;')
