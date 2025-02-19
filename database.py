import sqlite3

class Database:
    def __init__(self, db_name="database.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute('''
                            
            DROP TABLE IF EXISTS commands
                            
            CREATE TABLE IF NOT EXISTS commands (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT NOT NULL,
                path TEXT NOT NULL
            )
        ''')
        self.conn.commit()

        print("Table created successfully")

    def close(self):
        self.conn.close()