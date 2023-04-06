import sqlite3


class db():
    def __init__(self):     #підключення до бази даних створення таблиці в ній таблиці
        self.con = sqlite3.connect("data.db")
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS ask(id INTEGER PRIMARY KEY, pass CHAR(9), links CHAR(12000), marks(100) else TEXT)")
        self.con.commit()
    
    def new(self):      #створення зпису нового пустого опитування
        self.cur.execute('INSERT INTO ask(pass, links, marks) VALUES("", "", "")')
        self.con.commit()
        self.cur.execute('SELECT id FROM ask WHERE pass="" AND links="" AND marks=""')
        return self.cur.fetchone()[0]

    def add(self, passw, links, marks):     #додавання нового опитування з даними
        self.cur.execute("INSERT INTO ask(pass, links, marks) VALUES(?, ?, ?)", (passw, links, marks))
        self.con.commit()
        self.cur.execute("SELECT id FROM ask WHERE pass=? AND links=? AND marks=?", (passw, links, marks))
        return self.cur.fetchone()[0]
    
    def get(self, id):      #отримання опитування по id
        self.cur.execute("SELECT * FROM ask WHERE id=?", (id,))
        return self.cur.fetchone()
    
    def get_all(self):      #отримання даних всіх опитувань
        self.cur.execute("SELECT * FROM ask")
        return self.cur.fetchall()
    
    def delete(self, id):       #видалення опитування по id
        self.cur.execute("DELETE FROM ask WHERE id=?", (id,))
        self.con.commit()
        return True
    
    def update(self, id, passw, links, marks):      #оновлення даних опитування по id
        self.cur.execute("UPDATE ask SET pass=?, links=?, marks=? WHERE id=?", (passw, links, marks, id))
        self.con.commit()
        return True
    
