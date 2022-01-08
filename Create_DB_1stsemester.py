#get data from csv by using panda
import pandas as pd
from sqlite3 import *

file = pd.read_csv("Stuent_data.csv")
pd2 = pd.DataFrame(file)
pd2.index =range(1,174)

semesterone_data = pd2[['Roll no','Semester','Calculus','English','Introduction To Computing','Programming Fundamental ','Applied Physics']]
print(semesterone_data)
#i=0
#while i<=173:
try:
    con = connect("studentrecord.db")
    cursor = con.cursor()
    #sql = """CREATE TABLE std_semone (roll_no TEXT, Semester TEXT, Calculus NUMBER, English NUMBER, ITC NUMBER,
    #PF NUMBER, AP NUMBER)"""
        #sql="INSERT INTO std_semone VALUES ('"+semesterone_data['Roll no'][i]+"','"+semesterone_data['Semester'][i]+"','"+str(semesterone_data['Calculus'][i])+"','"+str(semesterone_data['English'][i])+"','"+str(semesterone_data['Introduction To Computing'][i])+"','"+str(semesterone_data['Programming Fundamental '][i])+"','"+str(semesterone_data['Applied Physics'][i])+"')"
    sql = """SELECT * FROM std_semone"""
    cursor.execute(sql)
    x = cursor.fetchall()
    con.commit()
    con.close()
    print(x)
except Exception as error:
    print(error)
    #i+=1
