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

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_documents(col_name) \
        VALUES (?)", \
        ('hello.txt',))
    cur.execute("INSERT INTO tbl_documents(col_name) \
        VALUES(?)", \
        ('world.txt',))
    conn.commit()
conn.close()


 
fileList = ('information.docx', 'hello.txt', 'myImage.png', \
            'myMovie.mpg', 'world.txt', 'data.pdf','myphoto.jpg')

for i in range(1,4):
    print(fileList[1],fileList[4])

               

