import os
# import calendar
import numpy as np
from numpy.lib.function_base import diff
import pandas as pd

# for file in os.listdir():
#     try:
#         table = file[6:8]
#         if table == str('t1'):
#             df = pd.read_csv(f'{file}')
#             print(df)
#             df = df.drop(
#                 lables=["! TURN PAGE FOR CITY OF TORONTO", "TABLES OR CLICK HERE:"], axis=0)
#             # print(file, 'Revised csv file save to final folder...\n')
#     except:
#         print(file, 'Failed Convert...\n')

df = pd.read_csv('201202t1.csv')
print(df.head(3))

i = df[((df.Region == '! TURN PAGE FOR CITY OF TORONTO')
        | (df.Region == 'TABLES OR CLICK HERE:'))].index
df = df.drop(df.index[i])
print(df.head(3))
