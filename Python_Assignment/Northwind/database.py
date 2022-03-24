#!/usr/bin/env python
# coding: utf-8

# In[13]:


import sqlite3
import csv
import datetime

class Database:
    def connect_to_db(self):
        conn = sqlite3.connect('northwind.db')
        return conn

    def create_db_tables(self):
        try:
            conn = connect_to_db()
            cur = conn.cursor()
            cur.execute('''create table orders (OrderID integer primary key,CustomerID varchar(5),
            EmployeeID integer,OrderDate date,RequiredDate date,ShippedDate date,ShipVia integer,
            Freight real,ShipName varchar(40),ShipAddress varchar(60),ShipCity varchar(15),
            ShipRegion varchar(15),ShipPostalCode varchar(10),ShipCountry varchar(15))''')

            conn.commit()
            print("Order table created successfully")
        except:
            print("Order table creation failed - Maybe table")
        
        try:
            cur.execute('''create table customers (CustomerID varchar(5) primary key,
            CompanyName varchar(40),ContactName varchar(30),ContactTitle varchar(30),
            Address varchar(60),City varchar(15),Region varchar(15),PostalCode varchar(10),
            Country varchar(15),Phone varchar(24),Fax varchar(24));''')
        
            conn.commit()
            print("Customers table created successfully")
        except:
            print("Customer table creation failed - Maybe table")
        
        try:
            cur.execute('''create table products (ProductID integer primary key,ProductName varchar(40),
            SupplierID integer,CategoryID integer,QuantityPerUnit varchar(20),UnitPrice real,UnitsInStock integer,
            UnitsOnOrder integer,ReorderLevel integer,Discontinued boolean)''')
        
            conn.commit()
            print("Products table created successfully")
        except:
            print("Products table creation failed - Maybe table")
    
        finally:
            conn.close()
        
    def insert_data_to_tables(self):
        data = []
        with open('customers.csv','r') as rf:
            reader = csv.reader(rf)
            for i in reader:
                data.append(tuple(i))
        for row in data[1:]:
            try:
                conn = connect_to_db()
                cur = conn.cursor()
                cur.execute("insert into customers values(?,?,?,?,?,?,?,?,?,?,?)",row)
                conn.commit()
            except Exception as e:
                print(e)
                print(row)
                break
            
        data = []
        with open('products.csv','r') as rf:
            reader = csv.reader(rf)
            for i in reader:
                if i[9] == 0:
                    i[9] = True
                else:
                    i[9] = False
                data.append(tuple(i))

        for row in data[1:]:
            try:
                cur.execute("insert into products values(?,?,?,?,?,?,?,?,?,?)",row)
                conn.commit()
            except Exception as e:
                print(e)
                print(row)
                break

        data = []
        with open('orders.csv','r') as rf:
            reader = csv.reader(rf)
            first = True
            for i in reader:
                if first:
                    first = False
                    continue
                for j in [3,4,5]:
                    if i[j] == 'NULL':
                        i[j] = None
                        continue
                    date = i[j].split(" ")[0].split("-")
                    i[j] = datetime.datetime(int(date[0]),int(date[1]),int(date[2]))
                data.append(tuple(i))
    
        for row in data:
            try:
                cur.execute("insert into orders values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",row)
                conn.commit()
            except Exception as e:
                print(e)
                print(row)
                break
        conn.close()

    
    def check_data(self):
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute('select * from orders;')
        chk_data=cur.fetchall()
        print(chk_data)
        conn.close()  

