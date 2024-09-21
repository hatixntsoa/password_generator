from sys import path
from os.path import abspath as abs, join as jn, dirname as dir

import pkg_resources
import sqlite3

def get_db_file(db_file):
    if __name__ == "__main__":
        return abs(jn(dir(__file__), '..', 'passwords', db_file))
    else:
        return pkg_resources.resource_filename(__name__, f'passwords/{db_file}')

# Connect to the SQLite database
conn = sqlite3.connect(get_db_file('passwords.db'))

# Create a cursor object
cursor = conn.cursor()

# Create a table (if it doesn't exist)
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
''')

# Insert data into the table
cursor.execute('''
INSERT INTO users (name, age)
VALUES (?, ?)
''', ('Alice', 30))

# Insert multiple rows
users = [
    ('Bob', 25),
    ('Charlie', 35),
    ('David', 40)
]
cursor.executemany('''
INSERT INTO users (name, age)
VALUES (?, ?)
''', users)

# Commit the transaction
conn.commit()

# Close the connection
conn.close()