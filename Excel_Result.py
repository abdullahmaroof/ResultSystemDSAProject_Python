from sqlite3 import *
from Excel_Data import *
import functools
import operator
currentDataAndTime = datetime.datetime.now()
dateAndTime = currentDataAndTime.strftime("%Y.%m.%d--%H.%M.%S")

class result:
    @staticmethod
    def std_rolno(rollno):
        try:
            con = connect("studentrecord.db")
            cursor = con.cursor()
            sql = "SELECT roll_no FROM std_info WHERE roll_no = '"+rollno+"'"
            cursor.execute(sql)
            x = cursor.fetchall()
            con.commit()
            con.close()

            def convertTuple(tup):
                str = functools.reduce(operator.add, (tup))
                return str

            string = convertTuple(x)

            def convertTuple1(tup):
                str = ''.join(tup)
                return str

            st = convertTuple1(string)
            return st

        except Exception as error:
            print(error)

    @staticmethod
    def std_name(rollno):
        try:
            con = connect("studentrecord.db")
            cursor = con.cursor()
            sql = "SELECT name FROM std_info WHERE roll_no = '" + rollno + "'"
            cursor.execute(sql)
            x = cursor.fetchall()
            con.commit()
            con.close()

            def convertTuple(tup):
                str = functools.reduce(operator.add, (tup))
                return str
            string = convertTuple(x)

            def convertTuple1(tup):
                str = ''.join(tup)
                return str

            st = convertTuple1(string)
            return st

        except Exception as error:
            print(error)

    @staticmethod
    def std_fname(rollno):
        try:
            con = connect("studentrecord.db")
            cursor = con.cursor()
            sql = "SELECT father_name FROM std_info WHERE roll_no = '" + rollno + "'"
            cursor.execute(sql)
            x = cursor.fetchall()
            con.commit()
            con.close()

            def convertTuple(tup):
                str = functools.reduce(operator.add, (tup))
                return str

            string = convertTuple(x)

            def convertTuple1(tup):
                str = ''.join(tup)
                return str

            st = convertTuple1(string)
            return st

        except Exception as error:
            print(error)

    @staticmethod
    def std_batch(rollno):
        try:
            con = connect("studentrecord.db")
            cursor = con.cursor()
            sql = "SELECT batch FROM std_info WHERE roll_no = '" + rollno + "'"
            cursor.execute(sql)
            x = cursor.fetchall()
            con.commit()
            con.close()

            def convertTuple(tup):
                str = functools.reduce(operator.add, (tup))
                return str

            string = convertTuple(x)

            def convertTuple1(tup):
                str = ''.join(tup)
                return str

            st = convertTuple1(string)
            return st

        except Exception as error:
            print(error)

    @staticmethod
    def std_program(rollno):
        try:
            con = connect("studentrecord.db")
            cursor = con.cursor()
            sql = "SELECT program FROM std_info WHERE roll_no = '" + rollno + "'"
            cursor.execute(sql)
            x = cursor.fetchall()
            con.commit()
            con.close()

            def convertTuple(tup):
                str = functools.reduce(operator.add, (tup))
                return str

            string = convertTuple(x)

            def convertTuple1(tup):
                str = ''.join(tup)
                return str

            st = convertTuple1(string)
            return st

        except Exception as error:
            print(error)

    @staticmethod
    def std_dept(rollno):
        try:
            con = connect("studentrecord.db")
            cursor = con.cursor()
            sql = "SELECT department FROM std_info WHERE roll_no = '" + rollno + "'"
            cursor.execute(sql)
            x = cursor.fetchall()
            con.commit()
            con.close()

            def convertTuple(tup):
                str = functools.reduce(operator.add, (tup))
                return str

            string = convertTuple(x)

            def convertTuple1(tup):
                str = ''.join(tup)
                return str

            st = convertTuple1(string)
            return st

        except Exception as error:
            print(error)

    @staticmethod
    def calculus(rollno):
        try:
            con = connect("studentrecord.db")
            cursor = con.cursor()
            sql = "SELECT Calculus FROM std_semone WHERE roll_no = '" + rollno + "'"
            cursor.execute(sql)
            x = cursor.fetchall()
            con.commit()
            con.close()

            def convertTuple(tup):
                str = functools.reduce(operator.add, (tup))
                return str

            string = convertTuple(x)

            def convertTuple1(tup):
                string1 = int(''.join(map(str, tup)))
                return string1

            st = convertTuple1(string)
            return st

        except Exception as error:
            print(error)

    @staticmethod
    def eng(rollno):
        try:
            con = connect("studentrecord.db")
            cursor = con.cursor()
            sql = "SELECT English FROM std_semone WHERE roll_no = '" + rollno + "'"
            cursor.execute(sql)
            x = cursor.fetchall()
            con.commit()
            con.close()

            def convertTuple(tup):
                str = functools.reduce(operator.add, (tup))
                return str

            string = convertTuple(x)

            def convertTuple1(tup):
                string1 = int(''.join(map(str, tup)))
                return string1

            st = convertTuple1(string)
            return st

        except Exception as error:
            print(error)

    @staticmethod
    def itc(rollno):
        try:
            con = connect("studentrecord.db")
            cursor = con.cursor()
            sql = "SELECT ITC FROM std_semone WHERE roll_no = '" + rollno + "'"
            cursor.execute(sql)
            x = cursor.fetchall()
            con.commit()
            con.close()

            def convertTuple(tup):
                str = functools.reduce(operator.add, (tup))
                return str

            string = convertTuple(x)
            def convertTuple1(tup):
                string1 = int(''.join(map(str, tup)))
                return string1

            st = convertTuple1(string)
            return st

        except Exception as error:
            print(error)

    @staticmethod
    def pf(rollno):
        try:
            con = connect("studentrecord.db")
            cursor = con.cursor()
            sql = "SELECT PF FROM std_semone WHERE roll_no = '" + rollno + "'"
            cursor.execute(sql)
            x = cursor.fetchall()
            con.commit()
            con.close()

            def convertTuple(tup):
                str = functools.reduce(operator.add, (tup))
                return str

            string = convertTuple(x)

            def convertTuple1(tup):
                string1 = int(''.join(map(str, tup)))
                return string1

            st = convertTuple1(string)
            return st

        except Exception as error:
            print(error)

    @staticmethod
    def ap(rollno):
        try:
            con = connect("studentrecord.db")
            cursor = con.cursor()
            sql = "SELECT AP FROM std_semone WHERE roll_no = '" + rollno + "'"
            cursor.execute(sql)
            x = cursor.fetchall()
            con.commit()
            con.close()

            def convertTuple(tup):
                str = functools.reduce(operator.add, (tup))
                return str

            string = convertTuple(x)

            def convertTuple1(tup):
                string1 = int(''.join(map(str, tup)))
                return string1

            st = convertTuple1(string)
            return st

        except Exception as error:
            print(error)

    @staticmethod
    def disctruc(rollno):
        try:
            con = connect("studentrecord.db")
            cursor = con.cursor()
            sql = "SELECT DiscStruct FROM std_semsec WHERE roll_no = '" + rollno + "'"
            cursor.execute(sql)
            x = cursor.fetchall()
            con.commit()
            con.close()

            def convertTuple(tup):
                str = functools.reduce(operator.add, (tup))
                return str

            string = convertTuple(x)

            def convertTuple1(tup):
                string1 = int(''.join(map(str, tup)))
                return string1

            st = convertTuple1(string)
            return st

        except Exception as error:
            print(error)

    @staticmethod
    def oop(rollno):
        try:
            con = connect("studentrecord.db")
            cursor = con.cursor()
            sql = "SELECT OOP FROM std_semsec WHERE roll_no = '" + rollno + "'"
            cursor.execute(sql)
            x = cursor.fetchall()
            con.commit()
            con.close()

            def convertTuple(tup):
                str = functools.reduce(operator.add, (tup))
                return str

            string = convertTuple(x)

            def convertTuple1(tup):
                string1 = int(''.join(map(str, tup)))
                return string1

            st = convertTuple1(string)
            return st

        except Exception as error:
            print(error)

    @staticmethod
    def stat(rollno):
        try:
            con = connect("studentrecord.db")
            cursor = con.cursor()
            sql = "SELECT Stat FROM std_semsec WHERE roll_no = '" + rollno + "'"
            cursor.execute(sql)
            x = cursor.fetchall()
            con.commit()
            con.close()

            def convertTuple(tup):
                str = functools.reduce(operator.add, (tup))
                return str

            string = convertTuple(x)

            def convertTuple1(tup):
                string1 = int(''.join(map(str, tup)))
                return string1

            st = convertTuple1(string)
            return st

        except Exception as error:
            print(error)

    @staticmethod
    def tbw(rollno):
        try:
            con = connect("studentrecord.db")
            cursor = con.cursor()
            sql = "SELECT TBW FROM std_semsec WHERE roll_no = '" + rollno + "'"
            cursor.execute(sql)
            x = cursor.fetchall()
            con.commit()
            con.close()

            def convertTuple(tup):
                str = functools.reduce(operator.add, (tup))
                return str

            string = convertTuple(x)

            def convertTuple1(tup):
                string1 = int(''.join(map(str, tup)))
                return string1

            st = convertTuple1(string)
            return st

        except Exception as error:
            print(error)

    @staticmethod
    def isl(rollno):
        try:
            con = connect("studentrecord.db")
            cursor = con.cursor()
            sql = "SELECT IslamicSTD FROM std_semsec WHERE roll_no = '" + rollno + "'"
            cursor.execute(sql)
            x = cursor.fetchall()
            con.commit()
            con.close()

            def convertTuple(tup):
                str = functools.reduce(operator.add, (tup))
                return str

            string = convertTuple(x)

            def convertTuple1(tup):
                string1 = int(''.join(map(str, tup)))
                return string1

            st = convertTuple1(string)
            return st

        except Exception as error:
            print(error)

    @staticmethod
    def pak(rollno):
        try:
            con = connect("studentrecord.db")
            cursor = con.cursor()
            sql = "SELECT PakSTD FROM std_semsec WHERE roll_no = '" + rollno + "'"
            cursor.execute(sql)
            x = cursor.fetchall()
            con.commit()
            con.close()

            def convertTuple(tup):
                str = functools.reduce(operator.add, (tup))
                return str

            string = convertTuple(x)

            def convertTuple1(tup):
                string1 = int(''.join(map(str, tup)))
                return string1

            st = convertTuple1(string)
            return st

        except Exception as error:
            print(error)

class grade:
    @staticmethod
    def calgrade(roll_no):
        marks = result.calculus(roll_no)
        if marks >= 85 and marks <= 100:
            return "A"
        elif marks >= 80 and marks <= 84:
            return "A-"
        elif marks >= 75 and marks <= 79:
            return "B+"
        elif marks >= 71 and marks <= 74:
            return "B"
        elif marks >= 68 and marks <= 70:
            return "B-"
        elif marks >= 64 and marks <= 67:
            return "C+"
        elif marks >= 61 and marks <= 63:
            return "C"
        elif marks >= 58 and marks <= 60:
            return "C-"
        elif marks >= 54 and marks <= 57:
            return "D+"
        elif marks >= 50 and marks <= 53:
            return "D"
        else:
            return "F"

    @staticmethod
    def enggrade(roll_no):
        marks = result.eng(roll_no)
        if marks >= 85 and marks <= 100:
            return "A"
        elif marks >= 80 and marks <= 84:
            return "A-"
        elif marks >= 75 and marks <= 79:
            return "B+"
        elif marks >= 71 and marks <= 74:
            return "B"
        elif marks >= 68 and marks <= 70:
            return "B-"
        elif marks >= 64 and marks <= 67:
            return "C+"
        elif marks >= 61 and marks <= 63:
            return "C"
        elif marks >= 58 and marks <= 60:
            return "C-"
        elif marks >= 54 and marks <= 57:
            return "D+"
        elif marks >= 50 and marks <= 53:
            return "D"
        else:
            return "F"

    @staticmethod
    def itcgrade(roll_no):
        marks = result.itc(roll_no)
        if marks >= 85 and marks <= 100:
            return "A"
        elif marks >= 80 and marks <= 84:
            return "A-"
        elif marks >= 75 and marks <= 79:
            return "B+"
        elif marks >= 71 and marks <= 74:
            return "B"
        elif marks >= 68 and marks <= 70:
            return "B-"
        elif marks >= 64 and marks <= 67:
            return "C+"
        elif marks >= 61 and marks <= 63:
            return "C"
        elif marks >= 58 and marks <= 60:
            return "C-"
        elif marks >= 54 and marks <= 57:
            return "D+"
        elif marks >= 50 and marks <= 53:
            return "D"
        else:
            return "F"

    @staticmethod
    def pfgrade(roll_no):
        marks = result.pf(roll_no)
        if marks >= 85 and marks <= 100:
            return "A"
        elif marks >= 80 and marks <= 84:
            return "A-"
        elif marks >= 75 and marks <= 79:
            return "B+"
        elif marks >= 71 and marks <= 74:
            return "B"
        elif marks >= 68 and marks <= 70:
            return "B-"
        elif marks >= 64 and marks <= 67:
            return "C+"
        elif marks >= 61 and marks <= 63:
            return "C"
        elif marks >= 58 and marks <= 60:
            return "C-"
        elif marks >= 54 and marks <= 57:
            return "D+"
        elif marks >= 50 and marks <= 53:
            return "D"
        else:
            return "F"

    @staticmethod
    def apgrade(roll_no):
        marks = result.ap(roll_no)
        if marks >= 85 and marks <= 100:
            return "A"
        elif marks >= 80 and marks <= 84:
            return "A-"
        elif marks >= 75 and marks <= 79:
            return "B+"
        elif marks >= 71 and marks <= 74:
            return "B"
        elif marks >= 68 and marks <= 70:
            return "B-"
        elif marks >= 64 and marks <= 67:
            return "C+"
        elif marks >= 61 and marks <= 63:
            return "C"
        elif marks >= 58 and marks <= 60:
            return "C-"
        elif marks >= 54 and marks <= 57:
            return "D+"
        elif marks >= 50 and marks <= 53:
            return "D"
        else:
            return "F"

    @staticmethod
    def disctrgrade(roll_no):
        marks = result.disctruc(roll_no)
        if marks >= 85 and marks <= 100:
            return "A"
        elif marks >= 80 and marks <= 84:
            return "A-"
        elif marks >= 75 and marks <= 79:
            return "B+"
        elif marks >= 71 and marks <= 74:
            return "B"
        elif marks >= 68 and marks <= 70:
            return "B-"
        elif marks >= 64 and marks <= 67:
            return "C+"
        elif marks >= 61 and marks <= 63:
            return "C"
        elif marks >= 58 and marks <= 60:
            return "C-"
        elif marks >= 54 and marks <= 57:
            return "D+"
        elif marks >= 50 and marks <= 53:
            return "D"
        else:
            return "F"

    @staticmethod
    def oopgrade(roll_no):
        marks = result.oop(roll_no)
        if marks >= 85 and marks <= 100:
            return "A"
        elif marks >= 80 and marks <= 84:
            return "A-"
        elif marks >= 75 and marks <= 79:
            return "B+"
        elif marks >= 71 and marks <= 74:
            return "B"
        elif marks >= 68 and marks <= 70:
            return "B-"
        elif marks >= 64 and marks <= 67:
            return "C+"
        elif marks >= 61 and marks <= 63:
            return "C"
        elif marks >= 58 and marks <= 60:
            return "C-"
        elif marks >= 54 and marks <= 57:
            return "D+"
        elif marks >= 50 and marks <= 53:
            return "D"
        else:
            return "F"

    @staticmethod
    def statgrade(roll_no):
        marks = result.stat(roll_no)
        if marks >= 85 and marks <= 100:
            return "A"
        elif marks >= 80 and marks <= 84:
            return "A-"
        elif marks >= 75 and marks <= 79:
            return "B+"
        elif marks >= 71 and marks <= 74:
            return "B"
        elif marks >= 68 and marks <= 70:
            return "B-"
        elif marks >= 64 and marks <= 67:
            return "C+"
        elif marks >= 61 and marks <= 63:
            return "C"
        elif marks >= 58 and marks <= 60:
            return "C-"
        elif marks >= 54 and marks <= 57:
            return "D+"
        elif marks >= 50 and marks <= 53:
            return "D"
        else:
            return "F"

    @staticmethod
    def tbwgrade(roll_no):
        marks = result.tbw(roll_no)
        if marks >= 85 and marks <= 100:
            return "A"
        elif marks >= 80 and marks <= 84:
            return "A-"
        elif marks >= 75 and marks <= 79:
            return "B+"
        elif marks >= 71 and marks <= 74:
            return "B"
        elif marks >= 68 and marks <= 70:
            return "B-"
        elif marks >= 64 and marks <= 67:
            return "C+"
        elif marks >= 61 and marks <= 63:
            return "C"
        elif marks >= 58 and marks <= 60:
            return "C-"
        elif marks >= 54 and marks <= 57:
            return "D+"
        elif marks >= 50 and marks <= 53:
            return "D"
        else:
            return "F"

    @staticmethod
    def islgrade(roll_no):
        marks = result.isl(roll_no)
        if marks >= 85 and marks <= 100:
            return "A"
        elif marks >= 80 and marks <= 84:
            return "A-"
        elif marks >= 75 and marks <= 79:
            return "B+"
        elif marks >= 71 and marks <= 74:
            return "B"
        elif marks >= 68 and marks <= 70:
            return "B-"
        elif marks >= 64 and marks <= 67:
            return "C+"
        elif marks >= 61 and marks <= 63:
            return "C"
        elif marks >= 58 and marks <= 60:
            return "C-"
        elif marks >= 54 and marks <= 57:
            return "D+"
        elif marks >= 50 and marks <= 53:
            return "D"
        else:
            return "F"

    @staticmethod
    def pakgrade(roll_no):
        marks = result.pak(roll_no)
        if marks >= 85 and marks <= 100:
            return "A"
        elif marks >= 80 and marks <= 84:
            return "A-"
        elif marks >= 75 and marks <= 79:
            return "B+"
        elif marks >= 71 and marks <= 74:
            return "B"
        elif marks >= 68 and marks <= 70:
            return "B-"
        elif marks >= 64 and marks <= 67:
            return "C+"
        elif marks >= 61 and marks <= 63:
            return "C"
        elif marks >= 58 and marks <= 60:
            return "C-"
        elif marks >= 54 and marks <= 57:
            return "D+"
        elif marks >= 50 and marks <= 53:
            return "D"
        else:
            return "F"
    @staticmethod
    def total_marks2sem(rollno):
        calculus = result.calculus(rollno)
        english = result.eng(rollno)
        applied_phy = result.ap(rollno)
        itc = result.itc(rollno)
        pf = result.pf(rollno)
        disstr = result.disctruc(rollno)
        stat = result.stat(rollno)
        oop = result.oop(rollno)
        tbw = result.tbw(rollno)
        isl = result.isl(rollno)
        pak = result.pak(rollno)

        total = calculus+english+applied_phy+itc+pf+disstr+stat+oop+tbw+isl+pak
        return total

    @staticmethod
    def total_marks1sem(rollno):
        calculus = result.calculus(rollno)
        english = result.eng(rollno)
        applied_phy = result.ap(rollno)
        itc = result.itc(rollno)
        pf = result.pf(rollno)

        total = calculus + english + applied_phy + itc + pf
        return total

    @staticmethod
    def subjectgpa(subject):
        if subject == "A":
            return 4
        elif subject == "A-":
            return 3.66
        elif subject == "B+":
            return 3.33
        elif subject == "B":
            return 3
        elif subject == "B-":
            return 2.66
        elif subject == "C+":
            return 2.33
        elif subject == "C":
            return 2
        elif subject == "C-":
            return 1.66
        elif subject == "D+":
            return 1.33
        elif subject == "D":
            return 1
        else:
            return 0

    @staticmethod
    def gpa1sem(rollno):
        cerdit_hour = 17
        gpacal = grade.subjectgpa(grade.calgrade(rollno))*3
        gpaeng = grade.subjectgpa(grade.enggrade(rollno))*3
        gpaap = grade.subjectgpa(grade.apgrade(rollno))*3
        gpaitc = grade.subjectgpa(grade.itcgrade(rollno))*4
        gpapf = grade.subjectgpa(grade.pfgrade(rollno))*4
        totalpoint = gpaap + gpapf +gpacal + gpaeng +gpaitc
        cgpa = totalpoint/cerdit_hour
        output = round(cgpa, 2)
        return output

    @staticmethod
    def gpa2sem(rollno):
        cerdit_hour = 17
        gpaoop = grade.subjectgpa(grade.oopgrade(rollno)) * 4
        gpatbw = grade.subjectgpa(grade.tbwgrade(rollno)) * 3
        gpastat = grade.subjectgpa(grade.statgrade(rollno)) * 3
        gpadis = grade.subjectgpa(grade.disctrgrade(rollno)) * 3
        gpaisl = grade.subjectgpa(grade.islgrade(rollno)) * 2
        gpapak = grade.subjectgpa(grade.pakgrade(rollno)) * 2
        totalpoint = gpadis +gpaoop + gpastat + gpatbw + gpaisl + gpapak
        gpa = totalpoint / cerdit_hour
        cgpa = (gpa + grade.gpa1sem(rollno))/2
        output = round(cgpa,2)
        return output

class excelreport:
    @staticmethod
    def sem1_resultreport(rollno):
        personal_heading1 = ['Name', 'Father Name', 'Roll no']
        personal_heading2 = ['Batch', 'Program', 'Department']
        persional_info1 = []
        persional_info2 = []
        subject = ['Calculus', 'English', 'ITC','PF', 'AP',]
        marks = []
        grades = []
        GPA = grade.gpa1sem(rollno)
        Total = grade.total_marks1sem(rollno)
        name = result.std_name(rollno)
        father_name = result.std_fname(rollno)
        roll_no = result.std_rolno(rollno)
        batch = result.std_batch(rollno)
        program = result.std_program(rollno)
        dept = result.std_dept(rollno)
        persional_info1.append(name)
        persional_info1.append(father_name)
        persional_info1.append(roll_no)
        persional_info2.append(batch)
        persional_info2.append(program)
        persional_info2.append(dept)
        calculus = result.calculus(rollno)
        english = result.eng(rollno)
        itc = result.itc(rollno)
        pf = result.pf(rollno)
        ap = result.ap(rollno)
        marks.append(calculus)
        marks.append(english)
        marks.append(itc)
        marks.append(pf)
        marks.append(ap)

        cal_grade = grade.calgrade(rollno)
        eng_grade = grade.enggrade(rollno)
        itc_grade = grade.itcgrade(rollno)
        pf_grade = grade.pfgrade(rollno)
        ap_grade = grade.apgrade(rollno)
        grades.append(cal_grade)
        grades.append(eng_grade)
        grades.append(itc_grade)
        grades.append(pf_grade)
        grades.append(ap_grade)

        excelfileName = "Result-report-"+str(rollno)+"-" + str(dateAndTime) + ".xlsx"
        myWorkbook = excelWriter.Workbook(excelfileName)
        myWorksheet = myWorkbook.add_worksheet()
        myWorksheet.write(0, 1,"RESULT CARD")
        myWorksheet.write(0, 2,"OF")
        myWorksheet.write(0, 3,"1st Semester")
        row = 3
        column = 0
        for x in personal_heading1:
            myWorksheet.write(row, column,x)
            row = row + 1

        row = 3
        column = 3
        for y in personal_heading2:
            myWorksheet.write(row, column, y)
            row = row + 1

        row = 3
        column = 1
        for a in persional_info1:
            myWorksheet.write(row, column, a)
            row = row + 1

        row = 3
        column = 4
        for b in persional_info2:
            myWorksheet.write(row, column, b)
            row = row + 1

        myWorksheet.write(7, 1, "Subject")
        myWorksheet.write(7, 2, "Marks")
        myWorksheet.write(7, 3, "Grade")

        row = 8
        column = 1
        for c in subject:
            myWorksheet.write(row, column,c)
            row = row + 1

        row = 8
        column = 2
        for d in marks:
            myWorksheet.write(row, column, d)
            row = row + 1

        row = 8
        column = 3
        for e in grades:
            myWorksheet.write(row, column, e)
            row = row + 1

        myWorksheet.write(13, 2, "Total")
        myWorksheet.write(13, 3, Total)
        myWorksheet.write(14, 2, "GPA")
        myWorksheet.write(14, 3, GPA)



        myWorkbook.close()

    @staticmethod
    def sem2_resultreport(rollno):
        personal_heading1 = ['Name', 'Father Name', 'Roll no']
        personal_heading2 = ['Batch', 'Program', 'Department']
        persional_info1 = []
        persional_info2 = []
        subject = ['Calculus', 'English', 'ITC', 'PF', 'AP','Discrete Structure','OOP','Probability & Stat',
                   'TBW','Islamic studies', 'Pak Studies']
        marks = []
        grades = []
        GPA = grade.gpa2sem(rollno)
        Total = grade.total_marks2sem(rollno)
        name = result.std_name(rollno)
        father_name = result.std_fname(rollno)
        roll_no = result.std_rolno(rollno)
        batch = result.std_batch(rollno)
        program = result.std_program(rollno)
        dept = result.std_dept(rollno)
        persional_info1.append(name)
        persional_info1.append(father_name)
        persional_info1.append(roll_no)
        persional_info2.append(batch)
        persional_info2.append(program)
        persional_info2.append(dept)
        calculus = result.calculus(rollno)
        english = result.eng(rollno)
        itc = result.itc(rollno)
        pf = result.pf(rollno)
        ap = result.ap(rollno)
        disstr = result.disctruc(rollno)
        oop = result.oop(rollno)
        stat = result.stat(rollno)
        tbw = result.tbw(rollno)
        isl = result.isl(rollno)
        pak = result.pak(rollno)
        marks.append(calculus)
        marks.append(english)
        marks.append(itc)
        marks.append(pf)
        marks.append(ap)
        marks.append(disstr)
        marks.append(oop)
        marks.append(stat)
        marks.append(tbw)
        marks.append(isl)
        marks.append(pak)

        cal_grade = grade.calgrade(rollno)
        eng_grade = grade.enggrade(rollno)
        itc_grade = grade.itcgrade(rollno)
        pf_grade = grade.pfgrade(rollno)
        ap_grade = grade.apgrade(rollno)
        distr_grade = grade.disctrgrade(rollno)
        oop_grade = grade.oopgrade(rollno)
        stat_grade = grade.statgrade(rollno)
        tbw_grade = grade.tbwgrade(rollno)
        isl_grade = grade.islgrade(rollno)
        pak_grade = grade.pakgrade(rollno)
        grades.append(cal_grade)
        grades.append(eng_grade)
        grades.append(itc_grade)
        grades.append(pf_grade)
        grades.append(ap_grade)
        grades.append(distr_grade)
        grades.append(oop_grade)
        grades.append(stat_grade)
        grades.append(tbw_grade)
        grades.append(isl_grade)
        grades.append(pak_grade)

        excelfileName = "Result-report-" + str(rollno) + "-" + str(dateAndTime) + ".xlsx"
        myWorkbook = excelWriter.Workbook(excelfileName)
        myWorksheet = myWorkbook.add_worksheet()
        myWorksheet.write(0, 1, "RESULT CARD")
        myWorksheet.write(0, 2, "OF")
        myWorksheet.write(0, 3, "2nd Semester")
        row = 3
        column = 0
        for x in personal_heading1:
            myWorksheet.write(row, column, x)
            row = row + 1

        row = 3
        column = 3
        for y in personal_heading2:
            myWorksheet.write(row, column, y)
            row = row + 1

        row = 3
        column = 1
        for a in persional_info1:
            myWorksheet.write(row, column, a)
            row = row + 1

        row = 3
        column = 4
        for b in persional_info2:
            myWorksheet.write(row, column, b)
            row = row + 1

        myWorksheet.write(7, 1, "Subject")
        myWorksheet.write(7, 2, "Marks")
        myWorksheet.write(7, 3, "Grade")

        row = 8
        column = 1
        for c in subject:
            myWorksheet.write(row, column, c)
            row = row + 1

        row = 8
        column = 2
        for d in marks:
            myWorksheet.write(row, column, d)
            row = row + 1

        row = 8
        column = 3
        for e in grades:
            myWorksheet.write(row, column, e)
            row = row + 1

        myWorksheet.write(19, 2, "Total")
        myWorksheet.write(19, 3, Total)
        myWorksheet.write(20, 2, "GPA")
        myWorksheet.write(20, 3, GPA)

        myWorkbook.close()