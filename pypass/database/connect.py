import os
import sqlite3

class PasswordDatabase:
    def __init__(self, db_file: str = 'passwords.db') -> None:
        self.db_file = db_file
        self.conn = self.connect_db()

    def connect_db(self) -> sqlite3.Connection:
        """Connect to the database and return the connection object."""
        return sqlite3.connect(self.get_db_file())

    def get_db_file(self) -> str:
        """Get the path to the database file."""
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "passwords", self.db_file)

    def create_table(self) -> None:
        """Create the passwords table if it doesn't exist."""
        with self.conn:
            self.conn.execute('''
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

    def insert_password(self, name: str, creation_date: str, owner: str, description: str, strength: str, password: str) -> None:
        """Insert a new password record into the database."""
        with self.conn:
            self.conn.execute('''
                INSERT INTO passwords (name, creation_date, owner, description, strength, password)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (name, creation_date, owner, description, strength, password))

    def fetch_passwords(self) -> list:
        """Fetch all stored passwords from the database."""
        with self.conn:
            return self.conn.execute('SELECT * FROM passwords').fetchall()
