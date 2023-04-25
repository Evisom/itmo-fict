from Database import Database


db = Database('database.db')
db.connect()
# db.insert('tCountry', [
#     ('6', 'Georgia'),
# ])    
print(db.select('tCountry', '*'))
db.close()
