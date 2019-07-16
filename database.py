# importing required libraries
import pymysql
import time
# Creating a Database connection
storage = input("Enter your database name :")
table = input("Enter your table name")
db = pymysql.connect(host='localhost', database=storage, user='', passwd='')
cursor = db.cursor()
print("Connected to " + storage)

# function which performed Database operations


def student_database():

    print("Press 1 for Creating New Table -->\n"
          "Press 2 for Displaying Data -->\n"
          "Press 3 for entering new Data..\n"
          "press 4 for adding new column to  table..\n"
          "press 5 for modifying data in table\n"
          "press 6  for deleting details of employee: ")
    value = int(input())
    if value == 1:
        create_table = input("Enter new table name :")
        column_names = input('Please enter a list of Column names: ').split()
        # reference link --
        # https://stackoverflow.com/questions/47924825/creating-tables-and-columns-dynamically-using-mysql-python-connector
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS " + create_table + "(" + " VARCHAR(250),".join(column_names) + " Varchar(250))")
        db.commit()
    if value == 2:
        print("Printing Data :\n")
        cursor.execute("SELECT * FROM (%s)" %(table))
        for row in cursor:
            print(row)
    elif value == 3:
        print("Enter New Values to be entered")
        first = input("Enter First Name: ")
        last = input("Enter Last Name: ")
        age = input("Enter Age: ")
        sex = input("Enter Sex: ")
        salary = input("Enter salary amount: ")
        no = input("Enter number")
        sno = input("enter serial number")
        aadhar = input("Enter Your Aadhar number :")
        # query for adding data into table
        cursor.execute('INSERT INTO ' + table + ' VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', (first, last, age, sex, salary, no, sno,aadhar))
        db.commit()
        print("Data entered Succesfully")

    elif value == 4:
        print("Enter column name to be added")
        column_name = input("enter new column name")
        # query for adding new column in existing table
        cursor.execute('Alter table ' + table + ' add  %s VARCHAR(100)' %column_name)
        db.commit()
        print("column Added successfully")
    elif value == 5:
        field_name = input("enter field name to be updated :")
        new_value = str(input("Please enter your new value"))
        print(new_value,type(new_value))
        reference_name = input("enter reference column name :")
        reference_value = input("enter reference value :")
        print('update '+table + ' set ' + field_name+ ' = '+ new_value+' WHERE '+ reference_name+' = '+ reference_value)
        cursor.execute('update '+table + ' set ' + field_name+ ' = '+ new_value+' WHERE '+ reference_name+' = '+ reference_value)
        db.commit()
        print("data modified succesfully ")

    elif value == 6:
        sno = input("enter employee number to be deleted :")
        reference_name = input("enter reference column name :")
        cursor.execute('DELETE FROM '+table + ' WHERE ' + reference_name + ' = '+sno)
        db.commit()
        print('Data From Row no : ' + sno + ' Deleted Successfully')


