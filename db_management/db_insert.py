'''
Example of the entry data.
Used to check if the database was created correctly and have data example to display 
'''
import sqlite3
# Establish a connection to the database
database = "PATH TO DATABASE"
connection = sqlite3.connect(database)
cursor = connection.cursor()

# Data for the 'worker' table
workers = [
  { "name": "Kata", "position": "Main Cat", "entryKey": "1004" },
  { "name": "Zenan", "position": "Second Main Cat", "entryKey": "1245" },
]

cursor.executemany("INSERT INTO worker (name,position,entryKey) VALUES (:name,:position,:entryKey)",workers)
connection.commit()

# Data for the 'admin' table
admin = [
  { "adminId": 1, "idNumber": "0001","loginKey": "1004"},
  { "adminId": 2, "idNumber": "0002","loginKey": "1245"},
]

cursor.executemany("INSERT INTO admin (adminId,idNumber,loginKey) VALUES (:adminId,:idNumber,:loginKey)",admin)
connection.commit()

# Data for the 'record' table
records = [
  { "dateTime": "02/05 13:08", "workerId": 1},
  { "dateTime": "05/05 10:32", "workerId": 1},
  { "dateTime": "05/05 16:43", "workerId": 2},
  { "dateTime": "10/05 09:50", "workerId": 2},
  { "dateTime": "15/05 10:56", "workerId": 2},
  { "dateTime": "15/05 15:58", "workerId": 1},
  { "dateTime": "16/05 11:10", "workerId": 1},
]

cursor.executemany("INSERT INTO record (dateTime,workerId) VALUES (:dateTime,:workerId)",records)
connection.commit()

