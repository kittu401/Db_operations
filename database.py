import pymysql
import time

def student_database():

    storage = input("Enter your database name :")
    table = input("Enter your table name")
    print("Press 1 for Displaying Data -->")
    print("Press 2 for entering new Data..")
    print("press 3 for adding new column to  table..")
    print("press 4 for modifying data in table")
    print("press 5  for deleting details of employee: ")
    value = int(input())
    db = pymysql.connect(host='localhost', database=storage, user='', passwd='')
    cursor = db.cursor()
    print("Connected to " + storage)

    if value == 1:
        print("Printing Data :\n")
        cursor.execute("SELECT * FROM (%s)" %(table))
        for row in cursor:
            print(row)
    elif value == 2:
        print("Enter New Values to be entered")
        first = input("Enter First Name: ")
        last = input("Enter Last Name: ")
        age = input("Enter Age: ")
        sex = input("Enter Sex: ")
        salary = input("Enter salary amount: ")
        no = input("Enter number")
        sno = input("enter serial number")
        aadhar = input("Enter Your Aadhra number :")
        # query for adding data into table
        cursor.execute('INSERT INTO ' + table + ' VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', (first, last, age, sex, salary, no, sno,aadhar))
        db.commit()
        print("Data entered Succesfully")

    elif value == 3:
        print("Enter column name to be added")
        column_name = input("enter new column name")
        #query for adding new column in existing table
        cursor.execute('Alter table ' + table + ' add  %s VARCHAR(10)' %column_name)
        db.commit()
        print("column Added successfully")

    elif value == 4:
        field_name = input("enter field name to be updated :")
        new_value = input("Please enter your new value")
        reference_name = input("enter reference column name :")
        reference_value = input("enter reference value :")
        cursor.execute('update employee set ' + field_name+ ' = '+ new_value+' WHERE '+ reference_name+' = '+reference_value)
        db.commit()
        print("data modified succesfully    ")

    elif value == 5:
        sno = input("enter employee number to be deleted :")
        reference_name = input("enter reference column name :")
        cursor.execute('DELETE FROM '+table + ' WHERE ' + reference_name + ' = '+sno)
        db.commit()
        print('Data From Row no : ' + sno + ' Deleted Successfully')    

while(True):

    student_database()
    time.sleep(3)
