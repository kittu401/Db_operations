# importing required libraries

from db.database import student_database
from db.todataframe import to_dataframe
import time

while(True):

    print("Press 1 for accessing Database.")
    print("press 2 for printing Data frame.")
    response = int(input("Enter your Choice"))
# selects which operation to be performed according to the input received

    if response == 1:
        student_database()
    elif response == 2:
        to_dataframe()
    else:
        print("enter Correct choice")
        time.sleep(3)