# CREATE TABLE tMusician (
#     id INTEGER PRIMARY KEY,
#     canonicalName TEXT,
#     age INT,
#     gender TEXT
# );

# CREATE TABLE tComments (
#     id INTEGER PRIMARY KEY,
#     textComm TEXT,
#     id_Musician INT,
#     id_Song INT,
#     FOREIGN KEY(id_Musician) REFERENCES tMusician(id),
#     FOREIGN KEY(id_Song) REFERENCES tSongs(id)
# );


# CREATE TABLE tSongs (
#     id INTEGER PRIMARY KEY,
#     id_Musician INT,
#     title TEXT,
#     describtion TEXT,
#     FOREIGN KEY(id_Musician) REFERENCES tMusician(id)
# );


from Database import Database


db = Database('music.db')
db.connect()
# db.insert('tComments', [
#     (1, 'text1', 1, 1 ),
#     (2, 'text2', 2, 2 ),
#     (3, 'text3', 3, 3 )
# ])    
print(db.select('tMusician', 'WHERE id = 1;'))
print(db.select('tComments', ''))
print(db.select('tSongs', ''))
db.close()
