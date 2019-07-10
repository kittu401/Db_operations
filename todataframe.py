import pymysql
import pandas as pd


def to_dataframe():

    storage = input("Enter your database name :")
    db = pymysql.connect(host='localhost', database=storage, user='', passwd='')
    table = input("Enter your table name")
    query = pd.read_sql('SELECT * FROM ' + table, db)
    print(query)

