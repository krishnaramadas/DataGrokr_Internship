# #### Create a table with a large number of records (you can find it with a google search or use this link - https://github.com/datacharmer/test_db). <br>Use MySQL Database. One can setup MySQL on localhost. Write some basic queries using python. 
# **Suppose you want to process/fetch a large number of records using python while keeping your memory usage low.**<br>
# Think of approaches on how to accomplish this and implement it. Hint: Use Generator

#Importing important libraries
import mysql.connector

#Initializing connection to mysql data base
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="*******",
    database="employees"
)

#Initializing cursor objcey
db = conn.cursor()

#Executing a sql query
db.execute("SELECT * FROM employees.employees")

#defining a generator to fetch all rows of the dabase table
def fetch(cursor):
    while True:
        rows = cursor.fetchall()
        if not rows:
            break 
        for row in rows:
            yield row

#creating a generator object
qry_result = fetch(db)

#running a loop to print out the results from the generator object
for i in range (5):
    print(next(qry_result))


# In[ ]:




