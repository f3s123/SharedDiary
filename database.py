import sqlite3

# 테이블 생성
# 계정 table
def CreateAccountTable():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS account (num INTEGER PRIMARY KEY AUTOINCREMENT, id TEXT, pw TEXT)")
    conn.commit()
    conn.close()

# diary 저장 table
def CreateDiaryTable():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS diary (num INTEGER PRIMARY KEY AUTOINCREMENT, id TEXT NOT NULL, title TEXT NOT NULL, content TEXT, time TEXT NOT NULL)")
    conn.commit()
    conn.close()

def RemoveAll():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("DROP TABLE account")
    conn.commit()
    cur.execute("DROP TABLE diary")
    conn.commit()
    conn.close()

# RemoveAll() # table 리셋시키고 싶을 때 하면 됩니다
CreateAccountTable()
CreateDiaryTable()