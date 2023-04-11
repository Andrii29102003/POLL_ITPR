import sqlite3
import json

#id = int
#passw = str
#links = json data
#marks = json data
#tmp = json data


class DB():
    def __init__(self, file_name):     #підключення до бази даних створення таблиці в ній таблиці
        self.con = sqlite3.connect(file_name)
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS ask(id INTEGER PRIMARY KEY, passw CHAR(9), links CHAR(12000), marks CHAR(100), tmp TEXT)")
        self.con.commit()
    
    # def create_poll(self):      #створення зпису нового пустого опитування
    #     self.cur.execute('INSERT INTO ask(passw, links, marks, tmp) VALUES("", "", "", "")')
    #     self.con.commit()
    #     self.cur.execute('SELECT id FROM ask WHERE passw="" AND links="" AND marks="" AND tmp=""')
    #     self.con.commit()
    #     return self.cur.fetchone()[0]

    def add_new_poll(self, passw, links, marks, tmp):     #додавання нового опитування з даними
        self.cur.execute("INSERT INTO ask(passw, links, marks, tmp) VALUES(?, ?, ?, ?)", (json.dumps(passw), json.dumps(links), json.dumps(marks), json.dumps(tmp)))
        self.con.commit()
        self.cur.execute("SELECT id FROM ask WHERE passw=? AND links=? AND marks=? AND tmp=?", (json.dumps(passw), json.dumps(links), json.dumps(marks), json.dumps(tmp)))
        self.con.commit()
        return self.cur.fetchone()[0]
    
    def get_poll_by_id(self, id):      #отримання опитування по id
        self.cur.execute("SELECT * FROM ask WHERE id=?", (id))
        self.con.commit()
        data={}
        data["id"] = self.cur.fetchone()[0]
        data["passw"] = self.cur.fetchone()[1]
        data["links"] = json.loads(self.cur.fetchone()[2])
        data["marks"] = json.loads(self.cur.fetchone()[3])
        data["tmp"] = json.loads(self.cur.fetchone()[4])
        return data    #повертає дані в словнику data з ключами id, passw, links, marks, tmp
    
    def get_all_pools(self):      #отримання даних всіх опитувань
        self.cur.execute("SELECT * FROM ask")
        self.con.commit()
        return self.cur.fetchall()
    
    def delete(self, id):       #видалення опитування по id
        self.cur.execute("DELETE FROM ask WHERE id=?", (id))
        self.con.commit()
        return True
    
    
    def update_poll_data(self, id, links, marks, tmp):      #оновлення даних опитування по id
        self.cur.execute("UPDATE ask SET links=?, marks=?, tmp=? WHERE id=?", (json.dumps(links), json.dumps(marks), json.dumps(tmp), id))
        self.con.commit()
        return True
    
    def update_poll_marsk_by_id(self, id_to_update, marks):      #оновлення даних опитування по id
        self.cur.execute("UPDATE ask SET marks=? WHERE id=?", (json.dumps(marks), id_to_update))
        self.con.commit()
        return True
    
    def update_poll_links_by_id(self, id_to_update, links):      #оновлення даних опитування по id
        self.cur.execute("UPDATE ask SET links=? WHERE id=?", (json.dumps(links), id_to_update))
        self.con.commit()
        return True
        
