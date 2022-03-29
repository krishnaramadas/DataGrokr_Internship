import mysql.connector
import json
import re
import pandas as pd
import numpy as np

class DataBase:
    #connection to server
    conn=mysql.connector.connect(host="localhost",
                                     user="root",
                                     password="user123",
                                    database='json_sql')
    cur = conn.cursor()
    
    #Creating sql table
    def create_table(self):
        self.conn._execute_query("DROP TABLE IF EXISTS json_to_sql_table;")
        self.cur.execute("CREATE TABLE json_to_sql_table (name varchar(100),phone varchar(100),email varchar(200),address varchar(255),region varchar(100),country varchar(100),list integer,postalzip varchar(200),currency varchar(100));")
        self.conn.commit()
        print("Table Created")

     #Loading data
    def load_data(self):
        with open(r"C:\Users\user\sample_data_for_assignment.json", encoding="utf-8") as f:
            data = json.load(f)
            print("Data Loaded")

        for values in data["data"]:
            self.cur.execute("INSERT INTO json_to_sql_table VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",values)
            self.conn.commit()
        print("Data Inserted")

    #Loading data into pandas dataframe    
    def load_to_pandas(self):
        self.cur.execute("SELECT * FROM json_to_sql_table;")
        rows = self.cur.fetchall()
        self.df = pd.DataFrame(rows,columns=["name",
                                             "phone",
                                             "email",
                                             "address",
                                             "region",
                                             "country",
                                             "list",
                                             "postalZip",
                                             "currency"])
        print(self.df)

    #function to change emial address
    def change_email(self):
        for i in range(len(self.df)):
            email = self.df.loc[i,"email"]
            new_email = email.split('@')[0] + "@gmail.com"
            self.df.loc[i,"email"] = new_email
        print(self.df)

    #function to chaange pin code    
    def change_pin_code(self):
        self.df["postalZip"]=self.df["postalZip"].str.replace('[^0-9]',"")
        self.df["postalZip"]=self.df["postalZip"].astype(np.int64)
        print(self.df)

     #Converting phone numbers into ASCII 
    def convert_ph_no(self,ph_no):
        ph_no = re.sub("[^0-9]+","",ph_no)
        return_string = ''
        for i in range(0,len(ph_no),2):
            try:
                temp_no = int(ph_no[i]+ph_no[i+1])
            except IndexError:
                return return_string
            if temp_no < 65:
                return_string += "O"
            else:
                return_string += chr(temp_no)

        return return_string

    def modify_Dataframe_for_ph_no(self):
        for i in range(len(self.df)):
            self.df.loc[i,"phone"] = self.convert_ph_no(self.df.loc[i,"phone"])

        print(self.df)
                   

if __name__ == '__main__':
    DB = DataBase()
    DB.create_table()
    DB.load_data()
    DB.load_to_pandas()
    DB.change_email()
    DB.change_pin_code()
    DB.modify_Dataframe_for_ph_no()