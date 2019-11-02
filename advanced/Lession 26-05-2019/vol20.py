import sqlite3
class DATABASE():
    def __init__(self,file_db):
        self.com =sqlite3.connect(file_db)
    def getAll(self,stringSQL,parametErr =()):
        cursor = self.con.execute(stringSQl,parametErr)
        ds = cursor.fecthall()
        return ds
    def getone(self,stringSQL,parametErr =()):
        cursor = self.con.execute(stringSQl,parametErr)
        item = cursor.fecthone()
        return item
    def execute(self,strignSQl,parametErr = ()):
        cursor = self.con.execute(stringSQL,parametErr)
        self.con.commit()
