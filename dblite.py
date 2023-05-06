import sqlite3
from flask import g 
import json





class DB:
    def __init__(self, file_name):
        self.db = None
        self.db_name = file_name
        

    def connect(self):
        self.db = sqlite3.connect(self.db_name)

    def close(self):
        if self.db is not None:
            self.db.close()

    def execute_query(self, query, params=None):
        cursor = self.db.cursor()
        if params is None:
            cursor.execute(query)
        else:
            cursor.execute(query, params)
<<<<<<< HEAD
=======
            self.db.commit()
>>>>>>> ba9e2b96270d4845bf6e7e5471af3e2e98c13b20
        result = cursor.fetchall()
        cursor.close()
        return result
    
    # def create_table_query(self, query, params=None):
    #     cursor = self.db.cursor()
    #     if params is None:
    #         cursor.execute(query)
    #     else:
    #         cursor.execute(query, params)
        
    #     cursor.close()
    #     return result
    
    
<<<<<<< HEAD
create_polls   = "CREATE TABLE IF NOT EXISTS poll_data (id INTEGER PRIMARY KEY, passw CHAR(10), del_passw CHAR(10), links CHAR(12000))"
create_results = "CREATE TABLE IF NOT EXISTS poll_results (id INTEGER PRIMARY KEY, passw CHAR(10), name CHAR(128), marks CHAR(200), recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"
=======
create_polls   = "CREATE TABLE IF NOT EXISTS poll_data (id INTEGER PRIMARY KEY, passw CHAR(10) UNIQUE, del_passw CHAR(10), links CHAR(12000))"
create_results = "CREATE TABLE IF NOT EXISTS poll_results (id INTEGER PRIMARY KEY, passw CHAR(10) UNIQUE, name CHAR(128), marks CHAR(200), recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"
>>>>>>> ba9e2b96270d4845bf6e7e5471af3e2e98c13b20

create_db_tables = [create_results, create_polls]

# result = db.execute_query("SELECT * FROM poll_data")


get_link_by_passw = "SELECT links FROM poll_data WHERE passw=?"
new_poll_query = "INSERT INTO poll_data(passw, del_passw, links) VALUES(?, ?, ?)"
# class DB():
#     def __init__(self, file_name):     #підключення до бази даних створення таблиці в ній таблиці
#         self.db = None
#         self.db_name = file_name
    
#     def connect(self):
#         self.con = sqlite3.connect(self.db_name, check_same_thread=False)
#         self.cur = self.con.cursor()
#         self.cur.execute("CREATE TABLE IF NOT EXISTS poll_data(id INTEGER PRIMARY KEY, passw CHAR(9), links CHAR(12000), marks CHAR(100), tmp TEXT)")
#         self.con.commit()

#     # def create_poll(self):      #створення зпису нового пустого опитування
#     #     self.cur.execute('INSERT INTO poll_data(passw, links, marks, tmp) VALUES("", "", "", "")')
#     #     self.con.commit()
#     #     self.cur.execute('SELECT id FROM poll_data WHERE passw="" AND links="" AND marks="" AND tmp=""')
#     #     self.con.commit()
#     #     return self.cur.fetchone()[0]

    
#     def get_poll_by_id(self, id):      #отримання опитування по id
#         self.cur.execute("SELECT * FROM poll_data WHERE id=?", (id))
#         self.con.commit()
#         data={}
#         data["id"] = self.cur.fetchone()[0]
#         data["passw"] = self.cur.fetchone()[1]
#         data["links"] = json.loads(self.cur.fetchone()[2])
#         data["marks"] = json.loads(self.cur.fetchone()[3])
#         data["tmp"] = json.loads(self.cur.fetchone()[4])
#         return data    #повертає дані в словнику data з ключами id, passw, links, marks, tmp
    
#     def get_all_pools(self):      #отримання даних всіх опитувань
#         self.cur.execute("SELECT * FROM poll_data")
#         self.con.commit()
#         return self.cur.fetchall()
    
#     def delete(self, id):       #видалення опитування по id
        # self.cur.execute("DELETE FROM poll_data WHERE id=?", (id))
        # self.con.commit()
        # return True
    
    
    # def update_poll_data(self, id, links, marks, tmp):      #оновлення даних опитування по id
    #     self.cur.execute("UPDATE poll_data SET links=?, marks=?, tmp=? WHERE id=?", (json.dumps(links), json.dumps(marks), json.dumps(tmp), id))
    #     self.con.commit()
    #     return True
    
    # def update_poll_marsk_by_id(self, id_to_update, marks):      #оновлення даних опитування по id
    #     self.cur.execute("UPDATE poll_data SET marks=? WHERE id=?", (json.dumps(marks), id_to_update))
    #     self.con.commit()
    #     return True
    
    # def update_poll_links_by_id(self, id_to_update, links):      #оновлення даних опитування по id
    #     self.cur.execute("UPDATE poll_data SET links=? WHERE id=?", (json.dumps(links), id_to_update))
    #     self.con.commit()
    #     return True
        
