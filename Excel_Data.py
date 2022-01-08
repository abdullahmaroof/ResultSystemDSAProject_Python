import xlsxwriter as excelWriter
import datetime
currentDataAndTime = datetime.datetime.now()
dateAndTime = currentDataAndTime.strftime("%Y.%m.%d--%H.%M.%S")

def all_std_asc(data):
    all = ['Roll no', 'Name', 'Father Name', 'Batch', 'Program', 'Department', 'Semester', 'Calculus', 'English', 'ITC',
           'PF', 'AP', 'Discrete Structure','OOP', 'Probability & Stat', 'TBW', 'Islamic Studies', 'Pak Studies']
    excelfileName = "allstd-data-ASC-"+str(dateAndTime)+".xlsx"
    myWorkbook = excelWriter.Workbook(excelfileName)
    myWorksheet = myWorkbook.add_worksheet()

    row = 0
    column = 0
    for each in all:
        myWorksheet.write(row, column, each)
        column = column + 1
    row=1
    column=0
    for eachRow in data:
        for eachItem in eachRow:
            myWorksheet.write(row, column, eachItem)
            column = column + 1
        row = row + 1
        column = 0



    myWorkbook.close()

def all_std_dsc(data):
    all = ['Roll no', 'Name', 'Father Name', 'Batch', 'Program', 'Department', 'Semester', 'Calculus', 'English', 'ITC',
           'PF', 'AP', 'Discrete Structure','OOP', 'Probability & Stat', 'TBW', 'Islamic Studies', 'Pak Studies']
    excelfileName = "all-student-data-DSC"+str(dateAndTime)+".xlsx"
    myWorkbook = excelWriter.Workbook(excelfileName)
    myWorksheet = myWorkbook.add_worksheet()

    row = 0
    column = 0
    for each in all:
        myWorksheet.write(row, column, each)
        column = column + 1
    row=1
    column=0
    for eachRow in data:
        for eachItem in eachRow:
            myWorksheet.write(row, column, eachItem)
            column = column + 1
        row = row + 1
        column = 0



    myWorkbook.close()


def all_stdse_asc(data):
    all = ['Roll no', 'Name', 'Father Name', 'Batch', 'Program', 'Department', 'Semester', 'Calculus', 'English', 'ITC',
           'PF', 'AP', 'Discrete Structure','OOP', 'Probability & Stat', 'TBW', 'Islamic Studies', 'Pak Studies']
    excelfileName = "all-student-SE-data-ASC"+str(dateAndTime)+".xlsx"
    myWorkbook = excelWriter.Workbook(excelfileName)
    myWorksheet = myWorkbook.add_worksheet()

    row = 0
    column = 0
    for each in all:
        myWorksheet.write(row, column, each)
        column = column + 1
    row=1
    column=0
    for eachRow in data:
        for eachItem in eachRow:
            myWorksheet.write(row, column, eachItem)
            column = column + 1
        row = row + 1
        column = 0



    myWorkbook.close()

def all_stdse_dsc(data):
    all = ['Roll no', 'Name', 'Father Name', 'Batch', 'Program', 'Department', 'Semester', 'Calculus', 'English', 'ITC',
           'PF', 'AP', 'Discrete Structure','OOP', 'Probability & Stat', 'TBW', 'Islamic Studies', 'Pak Studies']
    excelfileName = "all-student-SE-data-DSC"+str(dateAndTime)+".xlsx"
    myWorkbook = excelWriter.Workbook(excelfileName)
    myWorksheet = myWorkbook.add_worksheet()

    row = 0
    column = 0
    for each in all:
        myWorksheet.write(row, column, each)
        column = column + 1
    row=1
    column=0
    for eachRow in data:
        for eachItem in eachRow:
            myWorksheet.write(row, column, eachItem)
            column = column + 1
        row = row + 1
        column = 0



    myWorkbook.close()


def all_stdds_asc(data):
    all = ['Roll no', 'Name', 'Father Name', 'Batch', 'Program', 'Department', 'Semester', 'Calculus', 'English', 'ITC',
           'PF', 'AP', 'Discrete Structure','OOP', 'Probability & Stat', 'TBW', 'Islamic Studies', 'Pak Studies']
    excelfileName = "all-student-DS-data-ASC"+str(dateAndTime)+".xlsx"
    myWorkbook = excelWriter.Workbook(excelfileName)
    myWorksheet = myWorkbook.add_worksheet()

    row = 0
    column = 0
    for each in all:
        myWorksheet.write(row, column, each)
        column = column + 1
    row=1
    column=0
    for eachRow in data:
        for eachItem in eachRow:
            myWorksheet.write(row, column, eachItem)
            column = column + 1
        row = row + 1
        column = 0



    myWorkbook.close()

def all_stdds_dsc(data):
    all = ['Roll no', 'Name', 'Father Name', 'Batch', 'Program', 'Department', 'Semester', 'Calculus', 'English', 'ITC',
           'PF', 'AP', 'Discrete Structure','OOP', 'Probability & Stat', 'TBW', 'Islamic Studies', 'Pak Studies']
    excelfileName = "all-student-DS-data-DSC"+str(dateAndTime)+".xlsx"
    myWorkbook = excelWriter.Workbook(excelfileName)
    myWorksheet = myWorkbook.add_worksheet()

    row = 0
    column = 0
    for each in all:
        myWorksheet.write(row, column, each)
        column = column + 1
    row=1
    column=0
    for eachRow in data:
        for eachItem in eachRow:
            myWorksheet.write(row, column, eachItem)
            column = column + 1
        row = row + 1
        column = 0



    myWorkbook.close()



def all_stdai_asc(data):
    all = ['Roll no', 'Name', 'Father Name', 'Batch', 'Program', 'Department', 'Semester', 'Calculus', 'English', 'ITC',
           'PF', 'AP', 'Discrete Structure','OOP', 'Probability & Stat', 'TBW', 'Islamic Studies', 'Pak Studies']
    excelfileName = "all-student-AI-data-ASC"+str(dateAndTime)+".xlsx"
    myWorkbook = excelWriter.Workbook(excelfileName)
    myWorksheet = myWorkbook.add_worksheet()

    row = 0
    column = 0
    for each in all:
        myWorksheet.write(row, column, each)
        column = column + 1
    row=1
    column=0
    for eachRow in data:
        for eachItem in eachRow:
            myWorksheet.write(row, column, eachItem)
            column = column + 1
        row = row + 1
        column = 0



    myWorkbook.close()

def all_stdai_dsc(data):
    all = ['Roll no', 'Name', 'Father Name', 'Batch', 'Program', 'Department', 'Semester', 'Calculus', 'English', 'ITC',
           'PF', 'AP', 'Discrete Structure','OOP', 'Probability & Stat', 'TBW', 'Islamic Studies', 'Pak Studies']
    excelfileName = "all-student-AI-data-DSC"+str(dateAndTime)+".xlsx"
    myWorkbook = excelWriter.Workbook(excelfileName)
    myWorksheet = myWorkbook.add_worksheet()

    row = 0
    column = 0
    for each in all:
        myWorksheet.write(row, column, each)
        column = column + 1
    row=1
    column=0
    for eachRow in data:
        for eachItem in eachRow:
            myWorksheet.write(row, column, eachItem)
            column = column + 1
        row = row + 1
        column = 0



    myWorkbook.close()

def all_std_bothsem(data):
    all = ['Roll no', 'Name', 'Father Name', 'Batch', 'Program', 'Department','Semester','Calculus', 'English', 'ITC',
           'PF', 'AP', 'Discrete Structure','OOP', 'Probability & Stat', 'TBW', 'Islamic Studies', 'Pak Studies']
    excelfileName = "all-student-data-Bothsemester"+str(dateAndTime)+".xlsx"
    myWorkbook = excelWriter.Workbook(excelfileName)
    myWorksheet = myWorkbook.add_worksheet()

    row = 0
    column = 0
    for each in all:
        myWorksheet.write(row, column, each)
        column = column + 1
    row=1
    column=0
    for eachRow in data:
        for eachItem in eachRow:
            myWorksheet.write(row, column, eachItem)
            column = column + 1
        row = row + 1
        column = 0



    myWorkbook.close()

def all_std_1sem(data):
    all = ['Roll no', 'Name', 'Father Name', 'Batch', 'Program', 'Department','Calculus', 'English', 'ITC',
           'PF', 'AP']
    excelfileName = "all-student-data-1st-semester"+str(dateAndTime)+".xlsx"
    myWorkbook = excelWriter.Workbook(excelfileName)
    myWorksheet = myWorkbook.add_worksheet()

    row = 0
    column = 0
    for each in all:
        myWorksheet.write(row, column, each)
        column = column + 1
    row=1
    column=0
    for eachRow in data:
        for eachItem in eachRow:
            myWorksheet.write(row, column, eachItem)
            column = column + 1
        row = row + 1
        column = 0



    myWorkbook.close()


def all_std_2sem(data):
    all = ['Roll no', 'Name', 'Father Name', 'Batch', 'Program', 'Department','Discrete Structure','OOP', 'Probability & Stat', 'TBW', 'Islamic Studies', 'Pak Studies']
    excelfileName = "all-student-data-2nd-semester"+str(dateAndTime)+".xlsx"
    myWorkbook = excelWriter.Workbook(excelfileName)
    myWorksheet = myWorkbook.add_worksheet()

    row = 0
    column = 0
    for each in all:
        myWorksheet.write(row, column, each)
        column = column + 1
    row=1
    column=0
    for eachRow in data:
        for eachItem in eachRow:
            myWorksheet.write(row, column, eachItem)
            column = column + 1
        row = row + 1
        column = 0

    myWorkbook.close()


def all_stdSE_bothsem(data):
    all = ['Roll no', 'Name', 'Father Name', 'Batch', 'Program', 'Department','Semester','Calculus', 'English', 'ITC',
           'PF', 'AP', 'Discrete Structure', 'OOP', 'Probability & Stat', 'TBW', 'Islamic Studies', 'Pak Studies']
    excelfileName = "all-student-SE-data-Bothsemester" + str(dateAndTime) + ".xlsx"
    myWorkbook = excelWriter.Workbook(excelfileName)
    myWorksheet = myWorkbook.add_worksheet()

    row = 0
    column = 0
    for each in all:
        myWorksheet.write(row, column, each)
        column = column + 1
    row = 1
    column = 0
    for eachRow in data:
        for eachItem in eachRow:
            myWorksheet.write(row, column, eachItem)
            column = column + 1
        row = row + 1
        column = 0

    myWorkbook.close()


def all_stdSE_1sem(data):
    all = ['Roll no', 'Name', 'Father Name', 'Batch', 'Program', 'Department','Calculus', 'English', 'ITC',
           'PF', 'AP']
    excelfileName = "all-student-SE-data-1st-semester" + str(dateAndTime) + ".xlsx"
    myWorkbook = excelWriter.Workbook(excelfileName)
    myWorksheet = myWorkbook.add_worksheet()

    row = 0
    column = 0
    for each in all:
        myWorksheet.write(row, column, each)
        column = column + 1
    row = 1
    column = 0
    for eachRow in data:
        for eachItem in eachRow:
            myWorksheet.write(row, column, eachItem)
            column = column + 1
        row = row + 1
        column = 0

    myWorkbook.close()


def all_stdse_2sem(data):
    all = ['Roll no', 'Name', 'Father Name', 'Batch', 'Program', 'Department','Discrete Structure', 'OOP', 'Probability & Stat', 'TBW', 'Islamic Studies', 'Pak Studies']
    excelfileName = "all-student-data-SE-2nd-semester" + str(dateAndTime) + ".xlsx"
    myWorkbook = excelWriter.Workbook(excelfileName)
    myWorksheet = myWorkbook.add_worksheet()

    row = 0
    column = 0
    for each in all:
        myWorksheet.write(row, column, each)
        column = column + 1
    row = 1
    column = 0
    for eachRow in data:
        for eachItem in eachRow:
            myWorksheet.write(row, column, eachItem)
            column = column + 1
        row = row + 1
        column = 0

    myWorkbook.close()


def all_stdDS_bothsem(data):
    all = ['Roll no', 'Name', 'Father Name', 'Batch', 'Program', 'Department','Semester','Calculus', 'English', 'ITC',
           'PF', 'AP', 'Discrete Structure', 'OOP', 'Probability & Stat', 'TBW', 'Islamic Studies', 'Pak Studies']
    excelfileName = "all-student-data-DS-Bothsemester" + str(dateAndTime) + ".xlsx"
    myWorkbook = excelWriter.Workbook(excelfileName)
    myWorksheet = myWorkbook.add_worksheet()

    row = 0
    column = 0
    for each in all:
        myWorksheet.write(row, column, each)
        column = column + 1
    row = 1
    column = 0
    for eachRow in data:
        for eachItem in eachRow:
            myWorksheet.write(row, column, eachItem)
            column = column + 1
        row = row + 1
        column = 0

    myWorkbook.close()


def all_stdDS_1sem(data):
    all = ['Roll no', 'Name', 'Father Name', 'Batch', 'Program', 'Department','Calculus', 'English', 'ITC',
           'PF', 'AP']
    excelfileName = "all-student-data-DS-1st-semester" + str(dateAndTime) + ".xlsx"
    myWorkbook = excelWriter.Workbook(excelfileName)
    myWorksheet = myWorkbook.add_worksheet()

    row = 0
    column = 0
    for each in all:
        myWorksheet.write(row, column, each)
        column = column + 1
    row = 1
    column = 0
    for eachRow in data:
        for eachItem in eachRow:
            myWorksheet.write(row, column, eachItem)
            column = column + 1
        row = row + 1
        column = 0

    myWorkbook.close()


def all_stdDS_2sem(data):
    all = ['Roll no', 'Name', 'Father Name', 'Batch', 'Program', 'Department','Discrete Structure', 'OOP',
           'Probability & Stat', 'TBW', 'Islamic Studies', 'Pak Studies']
    excelfileName = "all-student-data-DS-2nd-semester" + str(dateAndTime) + ".xlsx"
    myWorkbook = excelWriter.Workbook(excelfileName)
    myWorksheet = myWorkbook.add_worksheet()

    row = 0
    column = 0
    for each in all:
        myWorksheet.write(row, column, each)
        column = column + 1
    row = 1
    column = 0
    for eachRow in data:
        for eachItem in eachRow:
            myWorksheet.write(row, column, eachItem)
            column = column + 1
        row = row + 1
        column = 0

    myWorkbook.close()


def all_stdAI_bothsem(data):
    all = ['Roll no', 'Name', 'Father Name', 'Batch', 'Program', 'Department','Semester','Calculus', 'English', 'ITC',
           'PF', 'AP', 'Discrete Structure', 'OOP', 'Probability & Stat', 'TBW', 'Islamic Studies', 'Pak Studies']
    excelfileName = "all-student-data-AI-Bothsemester" + str(dateAndTime) + ".xlsx"
    myWorkbook = excelWriter.Workbook(excelfileName)
    myWorksheet = myWorkbook.add_worksheet()

    row = 0
    column = 0
    for each in all:
        myWorksheet.write(row, column, each)
        column = column + 1
    row = 1
    column = 0
    for eachRow in data:
        for eachItem in eachRow:
            myWorksheet.write(row, column, eachItem)
            column = column + 1
        row = row + 1
        column = 0

    myWorkbook.close()


def all_stdAI_1sem(data):
    all = ['Roll no', 'Name', 'Father Name', 'Batch', 'Program', 'Department','Calculus', 'English', 'ITC',
           'PF', 'AP']
    excelfileName = "all-student-data-AI-1st-semester" + str(dateAndTime) + ".xlsx"
    myWorkbook = excelWriter.Workbook(excelfileName)
    myWorksheet = myWorkbook.add_worksheet()

    row = 0
    column = 0
    for each in all:
        myWorksheet.write(row, column, each)
        column = column + 1
    row = 1
    column = 0
    for eachRow in data:
        for eachItem in eachRow:
            myWorksheet.write(row, column, eachItem)
            column = column + 1
        row = row + 1
        column = 0

    myWorkbook.close()


def all_stdAI_2sem(data):
    all = ['Roll no', 'Name', 'Father Name', 'Batch', 'Program', 'Department','Discrete Structure', 'OOP',
           'Probability & Stat', 'TBW', 'Islamic Studies', 'Pak Studies']
    excelfileName = "all-student-data-AI-2nd-semester" + str(dateAndTime) + ".xlsx"
    myWorkbook = excelWriter.Workbook(excelfileName)
    myWorksheet = myWorkbook.add_worksheet()

    row = 0
    column = 0
    for each in all:
        myWorksheet.write(row, column, each)
        column = column + 1
    row = 1
    column = 0
    for eachRow in data:
        for eachItem in eachRow:
            myWorksheet.write(row, column, eachItem)
            column = column + 1
        row = row + 1
        column = 0

    myWorkbook.close()

