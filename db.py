import sqlite3

class DB:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY,username TEXT,password TEXT,email TEXT)"
        )

    def fetch(self):
        self.cur.execute(
            "SELECT * FROM users"
        )
        rows = self.cur.fetchall()
        return rows
    def insert(self,username,password,email):
        self.cur.execute("INSERT INTO users VALUES(NULL,?,?,?)",
                         (username,password,email))

        self.conn.commit()
