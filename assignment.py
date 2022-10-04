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
                
conn = sqlite3.connect('assignment.db')

fileList = ('information.docx', 'hello.txt', 'myImage.png', \
            'myMovie.mpg', 'world.txt', 'data.pdf','myphoto.jpg')

for i in fileList:
    if i.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_documents(col_name) \
                VALUES (?)", \
                (i,))
            cur.execute("INSERT INTO tbl_documents(col_name) \
                VALUES(?)", \
                (i,))
            conn.commit()
conn.close()


 


               

