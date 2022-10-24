import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """create a database connection to a sqlite database"""
    conn = None
    try:
        conn = sqlite.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_connection()
