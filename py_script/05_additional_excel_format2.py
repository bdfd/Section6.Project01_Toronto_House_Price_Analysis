import os
# import calendar
import numpy as np
import pandas as pd

value_names = ['Region', 'ComIndex', 'Composite', 'SFDIndex', 'SingleFamilyDetached',
               'SFAIndex', 'SingleFamilyAttached',  'THIndex', 'TownHouse', 'ApaIndex', 'Apartment']

file = str('201304t1')
year = file[:4]
month = file[4:6]
table = file[6:8]

df = pd.read_csv(f'{file}.csv')

df = df.rename(columns={
    'Unnamed: 0': value_names[0],
    'ComIndex': value_names[1],
    'Benchmark Yr./Yr. % Chg.': value_names[2],
    'SFDIndex': value_names[3],
    'Benchmark Yr./Yr. % Chg..1': value_names[4],
    'SFAIndex': value_names[5],
    'Benchmark Yr./Yr. % Chg..2': value_names[6],
    'THIndex': value_names[7],
    'Benchmark Yr./Yr. % Chg..3': value_names[8],
    'ApaIndex': value_names[9],
    'Benchmark Yr./Yr. % Chg..4': value_names[10],
})

# print(df.columns)

df[['Composite', 'Composite Change']
   ] = df['Composite'].str.split(' ', 1, expand=True)
df[['SingleFamilyDetached', 'SingleFamilyDetached Change']
   ] = df['SingleFamilyDetached'].str.split(' ', 1, expand=True)
df[['SingleFamilyAttached', 'SingleFamilyAttached Change']
   ] = df['SingleFamilyAttached'].str.split(' ', 1, expand=True)
df[['TownHouse', 'TownHouse Change']
   ] = df['TownHouse'].str.split(' ', 1, expand=True)
df[['Apartment', 'Apartment Change']
   ] = df['Apartment'].str.split(' ', 1, expand=True)

# print(df.columns)
df = df[['Region',
         'ComIndex',
         'Composite',
         'Composite Change',
         'SFDIndex',
         'SingleFamilyDetached',
         'SingleFamilyDetached Change',
         'SFAIndex',
         'SingleFamilyAttached',
         'SingleFamilyAttached Change',
         'THIndex',
         'TownHouse',
         'TownHouse Change',
         'ApaIndex',
         'Apartment',
         'Apartment Change'
         ]]

new_name = '{}{}{}'.format(year, month, table)
# print(new_name)
df.to_csv('../final/'+str(year)+'/' +
          str(new_name)+'.csv', index=False)
print(new_name, 'Revised csv file save to final folder...\n')
