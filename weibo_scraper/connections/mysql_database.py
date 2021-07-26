import sys
#import mysql.connector
import pymysql

def connect():
    try:
        conn = pymysql.connect(
            #host='127.0.0.1',
            host = 'localhost',
            unix_socket='/tmp/mysql.sock', 
            user='root', 
            passwd='Itagui22388!', 
            db='Weibo', 
            charset='utf8'
            )

        cur = conn.cursor()
        cur.execute("USE scraping")
    except Exception as e:
        sys.exit('unable to connect to database')
        print(e)
    else:
        return conn, cur

def disconnect(conn, cur):
    cur.close()
    conn.close()
