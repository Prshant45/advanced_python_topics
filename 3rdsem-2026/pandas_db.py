# Assignment 3 - menu driven program  to write class to do curd operation in database for employee table
# Assignment 2 - menu driven program  to write a class to do curd operation in csv file for employee table
# Assignment 4 - menu driven program to do curd operation in database for employee table
#  either using pandas or file handling


import pandas as pd
import pymysql

connection = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='Admin@123',
    database='employee'
)
query = "SELECT * FROM employee"
result = pd.read_sql(query, connection)
print(result)
average_salary = result['salary'].mean()
print(average_salary)
pd.write_sql("INSERT INTO employee (name, salary) VALUES ('John Doe', 50000)", connection, index=False)