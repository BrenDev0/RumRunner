import sqlite3

class Database:
    def __intit__(self):
        self.conn = sqlite3.connect('Files')
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS files (
        fileid INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT,
        filepath TEXT,
        frequency INTEGER                          
        )""")    

    def insert(self, file):
        self.cur.execute("INSERT OR IGNORE INTO files (filename, filepath) VALUES (?,?)", file )    
        self.conn.commit()

    def list_files(self, string):
        search = ('%'+string+'%')
        file_list = self.cur.execute("SELECT * FROM files WHERE filename LIKE ? ", search)    
        return file_list.fetchall()