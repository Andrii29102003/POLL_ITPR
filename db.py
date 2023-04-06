import sqlite3
import json

#id = int
#links = json data
#marks = json data
#tmp = json data


class DB():
    def __init__(self, file_name):     #підключення до бази даних створення таблиці в ній таблиці
        self.con = sqlite3.connect(file_name)
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS ask(id INTEGER PRIMARY KEY, pass CHAR(9), links CHAR(12000), marks(100), tmp TEXT)")
        self.con.commit()
    
    def new(self):      #створення зпису нового пустого опитування
        self.cur.execute('INSERT INTO ask(pass, links, marks, tmp) VALUES("", "", "", "")')
        self.con.commit()
        self.cur.execute('SELECT id FROM ask WHERE pass="" AND links="" AND marks="" AND tmp=""')
        return self.cur.fetchone()[0]

    def add(self, passw, links, marks, tmp):     #додавання нового опитування з даними
        links = json.dumps(links)
        marks = json.dumps(marks)
        tmp = json.dumps(tmp)
        self.cur.execute("INSERT INTO ask(pass, links, marks, tmp) VALUES(?, ?, ?, ?)", (passw, links, marks, tmp))
        self.con.commit()
        self.cur.execute("SELECT id FROM ask WHERE pass=? AND links=? AND marks=? AND tmp=?", (passw, links, marks, tmp))
        return self.cur.fetchone()[0]
    
    def get(self, id):      #отримання опитування по id
        self.cur.execute("SELECT * FROM ask WHERE id=?", (id))
        return self.cur.fetchone()
    
    def get_all(self):      #отримання даних всіх опитувань
        self.cur.execute("SELECT * FROM ask")
        return self.cur.fetchall()
    
    def delete(self, id):       #видалення опитування по id
        self.cur.execute("DELETE FROM ask WHERE id=?", (id))
        self.con.commit()
        return True
    
    def update(self, id, passw, links, marks, tmp):      #оновлення даних опитування по id
        links = json.dumps(links)
        marks = json.dumps(marks)
        tmp = json.dumps(tmp)
        self.cur.execute("UPDATE ask SET pass=?, links=?, marks=?, tmp=? WHERE id=?", (passw, links, marks, tmp, id))
        self.con.commit()
        return True
    
