#get data from csv by using panda
import pandas as pd
from sqlite3 import *

file = pd.read_csv("Stuent_data.csv")
pd2 = pd.DataFrame(file)
pd2.index =range(1,174)

semestersecond_data = pd2[['Roll no','Semester','Discrete Structure','Object Oriented Programming','Probability & Statistics','Technical & Business Writing','Islamic Studies','Pakistan Studies']]
print(semestersecond_data)
#i=0
#while i<=173:
try:
    con = connect("studentrecord.db")
    cursor = con.cursor()
    #sql= """CREATE TABLE std_semsec (roll_no TEXT, Semester TEXT, DiscStruct NUMBER, OOP NUMBER, Stat NUMBER, TBW NUMBER, IslamicSTD NUMBER, PakSTD NUMBER)"""
    #sql="INSERT INTO std_semsec VALUES ('"+semestersecond_data['Roll no'][i]+"','"+semestersecond_data['Semester'][i]+"','"+str(semestersecond_data['Discrete Structure'][i])+"','"+str(semestersecond_data['Object Oriented Programming'][i])+"','"+str(semestersecond_data['Probability & Statistics'][i])+"','"+str(semestersecond_data['Technical & Business Writing'][i])+"','"+str(semestersecond_data['Islamic Studies'][i])+"','"+str(semestersecond_data['Pakistan Studies'][i])+"')"
    sql = """SELECT * FROM std_semsec"""
    cursor.execute(sql)
    x = cursor.fetchall()
    con.commit()
    con.close()
    print(x)
except Exception as error:
    print(error)
    #i+=1
