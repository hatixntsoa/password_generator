from os.path import abspath as abs, join as jn, dirname as dir
import sqlite3

def get_db_file(db_file):
    return jn(dir(abs(__file__)), "..", "passwords", db_file)

def connect_db():
    conn = sqlite3.connect(get_db_file('passwords.db'))
    return conn

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            creation_date TEXT,
            owner TEXT,
            description TEXT,
            strength TEXT,
            password TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_password(name, creation_date, owner, description, strength, password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO passwords (name, creation_date, owner, description, strength, password)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, creation_date, owner, description, strength, password))
    conn.commit()
    conn.close()

def fetch_passwords():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM passwords')
    results = cursor.fetchall()
    conn.close()
    return results