#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import pandas as pd
import os
import glob
filepath = str(input("Path of the xlsx file: "))
data = pd.read_excel(filepath, sheet_name=None)

for sheet_name, df in data.items():
    df.to_csv(f'{sheet_name}.csv')
         
#path = os.getcwd()
filename=os.path.basename(filepath)
path=filepath.strip(filename)
csv_files = glob.glob(path + "*.csv")

for f in csv_files:
    print('-  ', f.split("\\")[-1])

