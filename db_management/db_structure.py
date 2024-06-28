import sqlite3

# Establish connection to the database
connection : sqlite3.Connection = sqlite3.connect("PATH TO DATABASE")
cursor : sqlite3.Cursor = connection.cursor()

# Drop existing worker table and creating new one
cursor.execute('DROP TABLE IF EXISTS worker')
cursor.execute('''
    CREATE TABLE worker (
        workerId INTEGER NOT NULL,
        name TEXT NOT NULL,
        position TEXT NULL,
        entryKey TEXT NOT NULL,
        PRIMARY KEY (workerId),
        UNIQUE(name,entryKey)
        UNIQUE (entryKey)
    )
 ''')
connection.commit()

# Drop existing record table and creating new one
cursor.execute('DROP TABLE IF EXISTS record')
cursor.execute('''
    CREATE TABLE record(
        recordId INTEGER NOT NULL,
        dateTime TEXT NOT NULL DEFAULT (strftime('%d-%m %H:%M', 'now')),
        workerId INTEGER NOT NULL,
        UNIQUE(dateTime,workerId),
        PRIMARY KEY (recordId),
        FOREIGN KEY (workerId) REFERENCES worker(workerId)
    )
''')
connection.commit()

# Drop existing admin table and creating new one
cursor.execute('DROP TABLE IF EXISTS admin')
cursor.execute('''
    CREATE TABLE admin(
        adminId INTEGER NOT NULL,
        idNumber TEXT NOT NULL,
        loginKey TEXT NOT NULL,
        PRIMARY KEY (adminId),
        UNIQUE (idNumber),
        UNIQUE (loginKey)
    )
''')
connection.commit()

# Drop existing faceEncoding table and creating new one
cursor.execute('DROP TABLE IF EXISTS faceEncoding')
cursor.execute('''
    CREATE TABLE faceEncoding(
        faceEncodingId INTEGER NOT NULL,
        workerId INTEGER NOT NULL,
        encoding BLOB NOT NULL,
        PRIMARY KEY (faceEncodingId),
        FOREIGN KEY (workerId) REFERENCES worker(workerId),
        UNIQUE(workerId)
    )
''')
connection.commit()





