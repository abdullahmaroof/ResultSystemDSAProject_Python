from sqlite3 import *
from datetime import *

try:
    con = connect("Admin.db")
    cursor = con.cursor()
    #sql = "CREATE TABLE admin (username TXT, password TXT)"
    #sql = "INSERT INTO admin VALUES ('abdullah','a123')"
    #sql = "INSERT INTO admin VALUES ('kabeer','k123')"
    #sql = "INSERT INTO admin VALUES ('zubair','z123')"
    sql = "SELECT * FROM admin"
    cursor.execute(sql)
    x = cursor.fetchall()
    con.commit()
    con.close()
    print(x)
except Exception as error:
    print(error)
