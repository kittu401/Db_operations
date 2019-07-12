# importing required libraries

import pymysql
import pandas as pd

# created function for data frame and file operation


def to_dataframe():

    storage = input("Enter your database name :")
    db = pymysql.connect(host='localhost', database=storage, user='', passwd='')  # creating a Db connection
    table = input("Enter your table name")
    query = pd.read_sql('SELECT * FROM ' + table, db)  # we can get data as a data frame using this query
    print(query)

    print("Do you want to write data in to a File :")
    choice = input("Please Enter yes Or No ?")
    if choice == 'yes' or 'Yes':
        file_name = input("Please Enter your File name :")
        file_type = int(input(" Please enter 1 for 'txt' or 2 for 'csv' :"))

        if file_type == 1:
            # creating a new text file using variable
            f = open('%s.txt' % file_name, 'w+')  # used variable as a file name, and opened file in write mode
            f.write(str(query))     # writing data to text file
            f.close()               # closing file after writing data
            print("Data written to text file")

        elif file_type == 2:
            df = pd.DataFrame(query)        # Loading query data in to data frame
            print(query)
            df.to_csv('%s.csv' % file_name, encoding='utf-8', index=False)      # writing data into csv file

        else:
            print("enter correct choice:")

