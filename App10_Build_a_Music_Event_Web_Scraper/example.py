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