#get data from csv by using panda
import pandas as pd
from sqlite3 import *

file = pd.read_csv("Stuent_data.csv")
pd2 = pd.DataFrame(file)
pd2.index =range(1,174)

personalinfo = pd2[['Roll no','Name','Father name','Batch','Program','Department']]
print(personalinfo)
#i=0
#while i<=173:
try:
    con = connect("studentrecord.db")
    cursor = con.cursor()
    #sql = """CREATE TABLE std_info (roll_no TEXT, name TEXT, father_name TEXT, batch TEXT,
    #program TEXT, department TEXT)"""
    #sql="INSERT INTO std_info VALUES ('"+personalinfo['Roll no'][i]+"','"+personalinfo['Name'][i]+"','"+personalinfo['Father name'][i]+"','"+personalinfo['Batch'][i]+"','"+personalinfo['Program'][i]+"','"+personalinfo['Department'][i]+"')"
    sql = """SELECT * FROM std_info"""
    cursor.execute(sql)
    x = cursor.fetchall()
    con.commit()
    con.close()
    print(x)
except Exception as error:
    print(error)
    #i+=1

