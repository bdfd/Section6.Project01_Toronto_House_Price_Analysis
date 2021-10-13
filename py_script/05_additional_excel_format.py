import os
# import calendar
import numpy as np
import pandas as pd

value_names = ['Region', 'ComIndex', 'Composite', 'Composite Change', 'SFDIndex', 'SingleFamilyDetached', 'SingleFamilyDetached Change',
               'SFAIndex', 'SingleFamilyAttached', 'SingleFamilyAttached Change',  'THIndex', 'TownHouse', 'TownHouse Change', 'ApaIndex', 'Apartment', 'Apartment Change']

file = str('201411t1')
year = file[:4]
month = file[4:6]
table = file[6:8]

df = pd.read_csv(f'{file}.csv', skiprows=1)
df = df.rename(columns={
    'Unnamed: 0': value_names[0],
    'Index': value_names[1],
    'Benchmark': value_names[2],
    'Yr./Yr. % Chg.': value_names[3],
    'Index.1': value_names[4],
    'Benchmark.1': value_names[5],
    'Yr./Yr. % Chg..1': value_names[6],
    'Index.2': value_names[7],
    'Benchmark.2': value_names[8],
    'Yr./Yr. % Chg..2': value_names[9],
    'Index.3': value_names[10],
    'Benchmark.3': value_names[11],
    'Yr./Yr. % Chg..3': value_names[12],
    'Index.4': value_names[13],
    'Benchmark.4': value_names[14],
    'Yr./Yr. % Chg..4': value_names[15],
})
# df[['Composite', 'Composite Change']
#    ] = df['Composite'].str.split(' ', 1, expand=True)
# df[['SingleFamilyDetached', 'SingleFamilyDetached Change']
#    ] = df['SingleFamilyDetached'].str.split(' ', 1, expand=True)
# df[['SingleFamilyAttached', 'SingleFamilyAttached Change']
#    ] = df['SingleFamilyAttached'].str.split(' ', 1, expand=True)
# df[['TownHouse', 'TownHouse Change']
#    ] = df['TownHouse'].str.split(' ', 1, expand=True)
# df[['Apartment', 'Apartment Change']] = df['Apartment'].str.split(
#     ' ', 1, expand=True)
# df = df[['Region',
#          'ComIndex',
#          'Composite',
#          'Composite Change',
#          'SFDIndex',
#          'SingleFamilyDetached',
#          'SingleFamilyDetached Change',
#          'SFAIndex',
#          'SingleFamilyAttached',
#          'SingleFamilyAttached Change',
#          'THIndex',
#          'TownHouse',
#          'TownHouse Change',
#          'ApaIndex',
#          'Apartment',
#          'Apartment Change'
#          ]]
i = df[((df.Region == '! TURN PAGE FOR CITY OF TORONTO')
        | (df.Region == 'TABLES OR CLICK HERE:') | (df.Region == '! TURN PAGE FOR CITY OF TORONTO TABLES OR CLICK HERE:'))].index
df = df.drop(df.index[i])
new_name = '{}{}{}'.format(year, month, table)
# print(new_name)
df.to_csv('../final/'+str(year)+'/' +
          str(new_name)+'.csv', index=False)
print(new_name, 'Revised csv file save to final folder...\n')
