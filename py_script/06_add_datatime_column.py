'''
Author: your name
Date: 2021-10-29 14:24:33
LastEditTime: 2021-10-29 14:56:00
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \1.1_Toronto_House_Price_Analysis\06_add_datatime_column.py
'''
import os
# import calendar
import numpy as np
import pandas as pd

for file in os.listdir():
    year = file[:4]
    month = file[4:6]
    table = file[6:8]
    rev = str('_rev')
    try:
        print(file)
        df = pd.read_csv(f'{file}')
        print(year)
        df['year'] = year
        print(month)
        df['month'] = month
        new_name = '{}{}{}{}'.format(str(year), str(month), table, rev)
        df.to_csv('../../final_rev/'+str(year)+'/' +
                  str(new_name)+'.csv', index=False)
        print(new_name, 'succesful convert')
    except:
        print(file, 'not work...\n')
