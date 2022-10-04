import sqlite3

conn = sqlite3.connect('assignment.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_documents( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \ 
        col_name TEXT \ #creating a database and adding a column 
        )")
    conn.commit()
conn.close() #closing connection
                
conn = sqlite3.connect('assignment.db') #connecting to database

fileList = ('information.docx', 'hello.txt', 'myImage.png', \
            'myMovie.mpg', 'world.txt', 'data.pdf','myphoto.jpg')

for i in fileList:
    if i.endswith('.txt'): #iterating through fileList to find docs ending in '.txt'
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_documents(col_name) \
                VALUES (?)", \ #adding selected docs to table
                (i,))
            conn.commit() #comitting changes to table
conn.close()


 


               

