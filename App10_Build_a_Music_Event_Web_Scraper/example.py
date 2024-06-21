import sqlite3

# establish a connection and a cursor
connection = sqlite3.connect('data1.db')
cursor = connection.cursor()

# query data
cursor.execute('SELECT * FROM events WHERE date = "2088.10.15"')
row = cursor.fetchall()
print(row)

cursor.execute('SELECT band, date FROM events WHERE date = "2088.10.15"')
row = cursor.fetchall()
print(row)

# insert new row
new_row = [('Ryan', 'Ryan Bad', '2024.06.21'),
           ('Ryan Mean', 'Ryan Funny', '2024.07.10')]
cursor.executemany('INSERT INTO events VALUES(?,?,?)', new_row)
connection.commit()