import sqlite3 

class Database:
    def __init__ (self, name):
        self.name = name
        
        self.connection = False 
        self.cursor = False
        self.sqlite3 = sqlite3

    def connect(self):
        try:
            self.connection = self.sqlite3.connect(self.name)
            self.cursor = self.connection.cursor()
            print('Connected')
            
        except:
            raise Exception 
    
    def insert(self, table, data):
        try:
            self.cursor.execute('PRAGMA table_info('+table+');')
            collumns = self.cursor.fetchall()
            for i in data:
                if len(i) != len(collumns):
                    raise Exception
            v = (len(collumns)*'?,')[0:-1]
            self.cursor.executemany('INSERT INTO '+table+' VALUES('+v+')', data)
        except:
            raise Exception
        
    def delete(self,table,  query):
        try:
            sql = 'DELETE FROM ' + table + ' ' + query
            print(sql)
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except:
            raise Exception
        
    def select(self,table,  query):
        try:
            sql = 'SELECT * FROM ' + table + ' ' + query
            print(sql)
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except:
            raise Exception
        
    def close(self):
        if self.connection:
            self.connection.commit()
            self.connection.close()
            print('Connection closed')





# CREATE TABLE "trucks" (
# 	"name" TEXT(20) NOT NULL,
# 	"cap" INT(20) NOT NULL,
# 	"w" INT(20) NOT NULL,
# 	"l" INT(20) NOT NULL,
# 	"h" INT(20) NOT NULL,
# 	"isBooked" INT(20),
#     "plate" TEXT(20),
# 	PRIMARY KEY ("plate")
# );