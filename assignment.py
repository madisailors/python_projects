import sqlite3

conn = sqlite3.connect('assignment.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_documents( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_name TEXT \
        )")
    conn.commit()
conn.close()
                
