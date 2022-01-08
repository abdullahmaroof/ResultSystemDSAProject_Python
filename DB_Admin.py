#database query for admin
from sqlite3 import *
from Excel_Data import *
from tkinter import messagebox


def data_order_ascdesc(dept, ascdsc):
    if dept == "All":
        if ascdsc == "Ascending":
            try:
                con = connect("studentrecord.db")
                cursor = con.cursor()
                sql = """SELECT std_info.roll_no, std_info.name, std_info.father_name, std_info.batch, std_info.program,
                std_info.department, std_semone.Semester, std_semone.Calculus, std_semone.English, std_semone.ITC, 
                std_semone.PF, std_semone.AP, std_semsec.DiscStruct, std_semsec.OOP, std_semsec.Stat, std_semsec.TBW,
                std_semsec.IslamicSTD, std_semsec.PakSTD FROM std_info INNER JOIN std_semone ON  std_info.roll_no 
                = std_semone.roll_no INNER JOIN std_semsec ON std_semone.roll_no = std_semsec.roll_no 
                ORDER BY std_info.roll_no ASC"""
                cursor.execute(sql)
                x = cursor.fetchall()
                con.commit()
                con.close()
                all_std_asc(x)
            except Exception as error:
                print(error)
        elif ascdsc == "Descending":
            try:
                con = connect("studentrecord.db")
                cursor = con.cursor()
                sql = """SELECT std_info.roll_no, std_info.name, std_info.father_name, std_info.batch, std_info.program,
                std_info.department, std_semone.Semester, std_semone.Calculus, std_semone.English, std_semone.ITC, 
                std_semone.PF, std_semone.AP, std_semsec.DiscStruct, std_semsec.OOP, std_semsec.Stat, std_semsec.TBW,
                std_semsec.IslamicSTD, std_semsec.PakSTD FROM std_info INNER JOIN std_semone ON  std_info.roll_no 
                = std_semone.roll_no INNER JOIN std_semsec ON std_semone.roll_no = std_semsec.roll_no 
                ORDER BY std_info.roll_no DESC"""
                cursor.execute(sql)
                x = cursor.fetchall()
                con.commit()
                con.close()
                all_std_dsc(x)
            except Exception as error:
                print(error)
        else:
            pass

    elif dept == "Software Engineering":
        if ascdsc == "Ascending":
            try:
                con = connect("studentrecord.db")
                cursor = con.cursor()
                sql = """SELECT std_info.roll_no, std_info.name, std_info.father_name, std_info.batch, std_info.program,
                std_info.department, std_semone.Semester, std_semone.Calculus, std_semone.English, std_semone.ITC, 
                std_semone.PF, std_semone.AP, std_semsec.DiscStruct, std_semsec.OOP, std_semsec.Stat, std_semsec.TBW,
                std_semsec.IslamicSTD, std_semsec.PakSTD FROM std_info INNER JOIN std_semone ON  std_info.roll_no 
                = std_semone.roll_no INNER JOIN std_semsec ON std_semone.roll_no = std_semsec.roll_no 
                WHERE std_info.program = "Bachelor of Science in Software Engineering"
                ORDER BY std_info.roll_no ASC"""
                cursor.execute(sql)
                x = cursor.fetchall()
                con.commit()
                con.close()
                all_stdse_asc(x)
            except Exception as error:
                print(error)
        elif ascdsc == "Descending":
            try:
                con = connect("studentrecord.db")
                cursor = con.cursor()
                sql = """SELECT std_info.roll_no, std_info.name, std_info.father_name, std_info.batch, std_info.program,
                std_info.department, std_semone.Semester, std_semone.Calculus, std_semone.English, std_semone.ITC, 
                std_semone.PF, std_semone.AP, std_semsec.DiscStruct, std_semsec.OOP, std_semsec.Stat, std_semsec.TBW,
                std_semsec.IslamicSTD, std_semsec.PakSTD FROM std_info INNER JOIN std_semone ON  std_info.roll_no 
                = std_semone.roll_no INNER JOIN std_semsec ON std_semone.roll_no = std_semsec.roll_no
                WHERE std_info.program = "Bachelor of Science in Software Engineering" 
                ORDER BY std_info.roll_no DESC"""
                cursor.execute(sql)
                x = cursor.fetchall()
                con.commit()
                con.close()
                all_stdse_dsc(x)
            except Exception as error:
                print(error)
        else:
            pass

    elif dept == "Data Science":
        if ascdsc == "Ascending":
            try:
                con = connect("studentrecord.db")
                cursor = con.cursor()
                sql = """SELECT std_info.roll_no, std_info.name, std_info.father_name, std_info.batch, std_info.program,
                std_info.department, std_semone.Semester, std_semone.Calculus, std_semone.English, std_semone.ITC, 
                std_semone.PF, std_semone.AP, std_semsec.DiscStruct, std_semsec.OOP, std_semsec.Stat, std_semsec.TBW,
                std_semsec.IslamicSTD, std_semsec.PakSTD FROM std_info INNER JOIN std_semone ON  std_info.roll_no 
                = std_semone.roll_no INNER JOIN std_semsec ON std_semone.roll_no = std_semsec.roll_no 
                WHERE std_info.program = "BS DATA SCIENCE"
                ORDER BY std_info.roll_no ASC"""
                cursor.execute(sql)
                x = cursor.fetchall()
                con.commit()
                con.close()
                all_stdds_asc(x)
            except Exception as error:
                print(error)
        elif ascdsc == "Descending":
            try:
                con = connect("studentrecord.db")
                cursor = con.cursor()
                sql = """SELECT std_info.roll_no, std_info.name, std_info.father_name, std_info.batch, std_info.program,
                std_info.department, std_semone.Semester, std_semone.Calculus, std_semone.English, std_semone.ITC, 
                std_semone.PF, std_semone.AP, std_semsec.DiscStruct, std_semsec.OOP, std_semsec.Stat, std_semsec.TBW,
                std_semsec.IslamicSTD, std_semsec.PakSTD FROM std_info INNER JOIN std_semone ON  std_info.roll_no 
                = std_semone.roll_no INNER JOIN std_semsec ON std_semone.roll_no = std_semsec.roll_no
                WHERE std_info.program = "BS DATA SCIENCE" 
                ORDER BY std_info.roll_no DESC"""
                cursor.execute(sql)
                x = cursor.fetchall()
                con.commit()
                con.close()
                all_stdds_dsc(x)
            except Exception as error:
                print(error)
        else:
            pass

    elif dept == "Artificial Intelligence":
        if ascdsc == "Ascending":
            try:
                con = connect("studentrecord.db")
                cursor = con.cursor()
                sql = """SELECT std_info.roll_no, std_info.name, std_info.father_name, std_info.batch, std_info.program,
                std_info.department, std_semone.Semester, std_semone.Calculus, std_semone.English, std_semone.ITC, 
                std_semone.PF, std_semone.AP, std_semsec.DiscStruct, std_semsec.OOP, std_semsec.Stat, std_semsec.TBW,
                std_semsec.IslamicSTD, std_semsec.PakSTD FROM std_info INNER JOIN std_semone ON  std_info.roll_no 
                = std_semone.roll_no INNER JOIN std_semsec ON std_semone.roll_no = std_semsec.roll_no 
                WHERE std_info.program = "BS ARTIFICIAL INTELLIGENCE"
                ORDER BY std_info.roll_no ASC"""
                cursor.execute(sql)
                x = cursor.fetchall()
                con.commit()
                con.close()
                all_stdai_asc(x)
            except Exception as error:
                print(error)
        elif ascdsc == "Descending":
            try:
                con = connect("studentrecord.db")
                cursor = con.cursor()
                sql = """SELECT std_info.roll_no, std_info.name, std_info.father_name, std_info.batch, std_info.program,
                std_info.department, std_semone.Semester, std_semone.Calculus, std_semone.English, std_semone.ITC, 
                std_semone.PF, std_semone.AP, std_semsec.DiscStruct, std_semsec.OOP, std_semsec.Stat, std_semsec.TBW,
                std_semsec.IslamicSTD, std_semsec.PakSTD FROM std_info INNER JOIN std_semone ON  std_info.roll_no 
                = std_semone.roll_no INNER JOIN std_semsec ON std_semone.roll_no = std_semsec.roll_no
                WHERE std_info.program = "BS ARTIFICIAL INTELLIGENCE" 
                ORDER BY std_info.roll_no DESC"""
                cursor.execute(sql)
                x = cursor.fetchall()
                con.commit()
                con.close()
                all_stdai_dsc(x)
            except Exception as error:
                print(error)
        else:
            pass


def data_semester(dept, ascdsc):
    if dept == "All":
        if ascdsc == "Both Semester":
            try:
                con = connect("studentrecord.db")
                cursor = con.cursor()
                sql = """SELECT std_info.roll_no, std_info.name, std_info.father_name, std_info.batch, std_info.program,
                std_info.department, std_semone.Semester, std_semone.Calculus, std_semone.English, std_semone.ITC, 
                std_semone.PF, std_semone.AP, std_semsec.DiscStruct, std_semsec.OOP, std_semsec.Stat, std_semsec.TBW,
                std_semsec.IslamicSTD, std_semsec.PakSTD FROM std_info INNER JOIN std_semone ON  std_info.roll_no 
                = std_semone.roll_no INNER JOIN std_semsec ON std_semone.roll_no = std_semsec.roll_no"""
                cursor.execute(sql)
                x = cursor.fetchall()
                con.commit()
                con.close()
                all_std_bothsem(x)
            except Exception as error:
                print(error)
        elif ascdsc == "1st Semester":
            try:
                con = connect("studentrecord.db")
                cursor = con.cursor()
                sql = """SELECT std_info.roll_no, std_info.name, std_info.father_name, std_info.batch, std_info.program,
                std_info.department, std_semone.Calculus, std_semone.English, std_semone.ITC, 
                std_semone.PF, std_semone.AP FROM std_info INNER JOIN std_semone ON  std_info.roll_no 
                = std_semone.roll_no"""
                cursor.execute(sql)
                x = cursor.fetchall()
                con.commit()
                con.close()
                all_std_1sem(x)
            except Exception as error:
                print(error)
        if ascdsc == "2nd Semester":
            try:
                con = connect("studentrecord.db")
                cursor = con.cursor()
                sql = """SELECT std_info.roll_no, std_info.name, std_info.father_name, std_info.batch, std_info.program,
                std_info.department, std_semsec.DiscStruct, std_semsec.OOP, std_semsec.Stat, std_semsec.TBW,
                std_semsec.IslamicSTD, std_semsec.PakSTD FROM std_info INNER JOIN std_semsec ON 
                std_info.roll_no =  std_semsec.roll_no"""
                cursor.execute(sql)
                x = cursor.fetchall()
                con.commit()
                con.close()
                all_std_2sem(x)
            except Exception as error:
                print(error)
        else:
            pass

    elif dept == "Software Engineering":
        if ascdsc == "Both Semester":
            try:
                con = connect("studentrecord.db")
                cursor = con.cursor()
                sql = """SELECT std_info.roll_no, std_info.name, std_info.father_name, std_info.batch, std_info.program,
                std_info.department, std_semone.Semester, std_semone.Calculus, std_semone.English, std_semone.ITC, 
                std_semone.PF, std_semone.AP, std_semsec.DiscStruct, std_semsec.OOP, std_semsec.Stat, std_semsec.TBW,
                std_semsec.IslamicSTD, std_semsec.PakSTD FROM std_info INNER JOIN std_semone ON  std_info.roll_no 
                = std_semone.roll_no INNER JOIN std_semsec ON std_semone.roll_no = std_semsec.roll_no"""
                cursor.execute(sql)
                x = cursor.fetchall()
                con.commit()
                con.close()
                all_stdSE_bothsem(x)
            except Exception as error:
                print(error)
        elif ascdsc == "1st Semester":
            try:
                con = connect("studentrecord.db")
                cursor = con.cursor()
                sql = """SELECT std_info.roll_no, std_info.name, std_info.father_name, std_info.batch, std_info.program,
                std_info.department, std_semone.Calculus, std_semone.English, std_semone.ITC, 
                std_semone.PF, std_semone.AP FROM std_info INNER JOIN std_semone ON  std_info.roll_no 
                = std_semone.roll_no"""
                cursor.execute(sql)
                x = cursor.fetchall()
                con.commit()
                con.close()
                all_stdSE_1sem(x)
            except Exception as error:
                print(error)
        if ascdsc == "2nd Semester":
            try:
                con = connect("studentrecord.db")
                cursor = con.cursor()
                sql = """SELECT std_info.roll_no, std_info.name, std_info.father_name, std_info.batch, std_info.program,
                std_info.department, std_semsec.DiscStruct, std_semsec.OOP, std_semsec.Stat, std_semsec.TBW,
                std_semsec.IslamicSTD, std_semsec.PakSTD FROM std_info INNER JOIN std_semsec ON
                std_info.roll_no =  std_semsec.roll_no"""
                cursor.execute(sql)
                x = cursor.fetchall()
                con.commit()
                con.close()
                all_stdse_2sem(x)
            except Exception as error:
                print(error)
        else:
            pass

    elif dept == "Data Science":
        if ascdsc == "Both Semester":
            try:
                con = connect("studentrecord.db")
                cursor = con.cursor()
                sql = """SELECT std_info.roll_no, std_info.name, std_info.father_name, std_info.batch, std_info.program,
                std_info.department, std_semone.Semester, std_semone.Calculus, std_semone.English, std_semone.ITC, 
                std_semone.PF, std_semone.AP, std_semsec.DiscStruct, std_semsec.OOP, std_semsec.Stat, std_semsec.TBW,
                std_semsec.IslamicSTD, std_semsec.PakSTD FROM std_info INNER JOIN std_semone ON  std_info.roll_no 
                = std_semone.roll_no INNER JOIN std_semsec ON std_semone.roll_no = std_semsec.roll_no
                 WHERE std_info.program = "BS DATA SCIENCE" """
                cursor.execute(sql)
                x = cursor.fetchall()
                con.commit()
                con.close()
                all_stdDS_bothsem(x)
            except Exception as error:
                print(error)
        elif ascdsc == "1st Semester":
            try:
                con = connect("studentrecord.db")
                cursor = con.cursor()
                sql = """SELECT std_info.roll_no, std_info.name, std_info.father_name, std_info.batch, std_info.program,
                std_info.department, std_semone.Calculus, std_semone.English, std_semone.ITC, 
                std_semone.PF, std_semone.AP FROM std_info INNER JOIN std_semone ON  std_info.roll_no 
                = std_semone.roll_no  WHERE std_info.program = "BS DATA SCIENCE" """
                cursor.execute(sql)
                x = cursor.fetchall()
                con.commit()
                con.close()
                all_stdDS_1sem(x)
            except Exception as error:
                print(error)
        if ascdsc == "2nd Semester":
            try:
                con = connect("studentrecord.db")
                cursor = con.cursor()
                sql = """SELECT std_info.roll_no, std_info.name, std_info.father_name, std_info.batch, std_info.program,
                std_info.department, std_semsec.DiscStruct, std_semsec.OOP, std_semsec.Stat, std_semsec.TBW,
                std_semsec.IslamicSTD, std_semsec.PakSTD FROM std_info INNER JOIN std_semsec ON
                std_info.roll_no =  std_semsec.roll_no WHERE std_info.program = "BS DATA SCIENCE" """
                cursor.execute(sql)
                x = cursor.fetchall()
                con.commit()
                con.close()
                all_stdDS_2sem(x)
            except Exception as error:
                print(error)
        else:
            pass

    elif dept == "Artificial Intelligence":
        if ascdsc == "Both Semester":
            try:
                con = connect("studentrecord.db")
                cursor = con.cursor()
                sql = """SELECT std_info.roll_no, std_info.name, std_info.father_name, std_info.batch, std_info.program,
                std_info.department, std_semone.Semester, std_semone.Calculus, std_semone.English, std_semone.ITC, 
                std_semone.PF, std_semone.AP, std_semsec.DiscStruct, std_semsec.OOP, std_semsec.Stat, std_semsec.TBW,
                std_semsec.IslamicSTD, std_semsec.PakSTD FROM std_info INNER JOIN std_semone ON  std_info.roll_no 
                = std_semone.roll_no INNER JOIN std_semsec ON std_semone.roll_no = std_semsec.roll_no
                 WHERE std_info.program = "BS ARTIFICIAL INTELLIGENCE" """
                cursor.execute(sql)
                x = cursor.fetchall()
                con.commit()
                con.close()
                all_stdAI_bothsem(x)
            except Exception as error:
                print(error)
        elif ascdsc == "1st Semester":
            try:
                con = connect("studentrecord.db")
                cursor = con.cursor()
                sql = """SELECT std_info.roll_no, std_info.name, std_info.father_name, std_info.batch, std_info.program,
                std_info.department, std_semone.Calculus, std_semone.English, std_semone.ITC, 
                std_semone.PF, std_semone.AP FROM std_info INNER JOIN std_semone ON  std_info.roll_no 
                = std_semone.roll_no WHERE std_info.program = "BS ARTIFICIAL INTELLIGENCE" """
                cursor.execute(sql)
                x = cursor.fetchall()
                con.commit()
                con.close()
                all_stdAI_1sem(x)
            except Exception as error:
                print(error)
        if ascdsc == "2nd Semester":
            try:
                con = connect("studentrecord.db")
                cursor = con.cursor()
                sql = """SELECT std_info.roll_no, std_info.name, std_info.father_name, std_info.batch, std_info.program,
                std_info.department, std_semsec.DiscStruct, std_semsec.OOP, std_semsec.Stat, std_semsec.TBW,
                std_semsec.IslamicSTD, std_semsec.PakSTD FROM std_info INNER JOIN std_semsec ON
                std_info.roll_no =  std_semsec.roll_no WHERE std_info.program = "BS ARTIFICIAL INTELLIGENCE" """
                cursor.execute(sql)
                x = cursor.fetchall()
                con.commit()
                con.close()
                all_stdAI_2sem(x)
            except Exception as error:
                print(error)
        else:
            pass

def total_student(dept):
    if dept == "All":
        try:
            con = connect("studentrecord.db")
            cursor = con.cursor()
            sql = """SELECT COUNT(roll_no) FROM std_info"""
            cursor.execute(sql)
            x = cursor.fetchall()
            con.commit()
            con.close()
            message= "Total Students of SE DEPT "+str(x)+"."
            messagebox.showinfo("Total Student",message)
            file_totalstd = open("total_student.txt", "a")
            file_totalstd.write("Total Students of SE DEPT: " + str(x))
            file_totalstd.write("\n")
            file_totalstd.write("Time of storing data: " + dateAndTime)
            file_totalstd.write("\n\n")
            file_totalstd.close()
        except Exception as error:
            print(error)
    elif dept =="Software Engineering":
        try:
            con = connect("studentrecord.db")
            cursor = con.cursor()
            sql = """SELECT COUNT(roll_no) FROM std_info WHERE program = "Bachelor of Science in Software Engineering" """
            cursor.execute(sql)
            x = cursor.fetchall()
            con.commit()
            con.close()
            message = "Total Students of SE Program of SE DEPT " + str(x) + "."
            messagebox.showinfo("Total Student", message)
            file_totalstdse = open("total_student.txt", "a")
            file_totalstdse.write("Total Students of SE Program: " + str(x))
            file_totalstdse.write("\n")
            file_totalstdse.write("Time of storing data: " + dateAndTime)
            file_totalstdse.write("\n\n")
            file_totalstdse.close()
        except Exception as error:
            print(error)
    elif dept == "Data Science":
        try:
            con = connect("studentrecord.db")
            cursor = con.cursor()
            sql = """SELECT COUNT(roll_no) FROM std_info WHERE program = "BS DATA SCIENCE" """
            cursor.execute(sql)
            x = cursor.fetchall()
            con.commit()
            con.close()
            message = "Total Students of DS Program of SE DEPT " + str(x) + "."
            messagebox.showinfo("Total Student", message)
            file_totalstdds = open("total_student.txt", "a")
            file_totalstdds.write("Total Students of DS Program: " + str(x))
            file_totalstdds.write("\n")
            file_totalstdds.write("Time of storing data: " + dateAndTime)
            file_totalstdds.write("\n\n")
            file_totalstdds.close()
        except Exception as error:
            print(error)
    elif dept == "Artificial Intelligence":
        try:
            con = connect("studentrecord.db")
            cursor = con.cursor()
            sql = """SELECT COUNT(roll_no) FROM std_info WHERE program = "BS ARTIFICIAL INTELLIGENCE" """
            cursor.execute(sql)
            x = cursor.fetchall()
            con.commit()
            con.close()
            message = "Total Students of AI Program of SE DEPT " + str(x) + "."
            messagebox.showinfo("Total Student", message)
            file_totalstdai = open("total_student.txt", "a")
            file_totalstdai.write("Total Students of AI Program: " + str(x))
            file_totalstdai.write("\n")
            file_totalstdai.write("Time of storing data: " + dateAndTime)
            file_totalstdai.write("\n\n")
            file_totalstdai.close()
        except Exception as error:
            print(error)
    else:
        pass