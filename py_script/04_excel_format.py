import os
# import calendar
import numpy as np
import pandas as pd


housing_price_csv_dir = '../data/test'

# value_names = ['SingleFamilyDetachedIndex', 'SingleFamilyDetachedReference',
#                'SingleFamilyAttachedIndex', 'SingleFamilyAttachedReference',
#                'TownHouseIndex', 'TownHouseReference', 'ApartmentIndex',
#                'ApartmentReference']

# print(value_names)
value_names = ['Region', 'ComIndex', 'Composite', 'SFDIndex', 'SingleFamilyDetached',
               'SFAIndex', 'SingleFamilyAttached', 'THIndex', 'TownHouse', 'ApaIndex', 'Apartment']

for file in os.listdir():
    # print(file)
    #     if file[:4] in ['2012']:
    try:
        year = file[:4]
        month = file[4:6]
        table = file[6:8]
        df = pd.read_csv(f'{file}', skiprows=1)
        df = df.rename(columns={'Unnamed: 0': value_names[0],
                                'Index': value_names[1],
                                'Benchmark Yr./Yr. % Chg.': value_names[2],
                                'Index.1': value_names[3],
                                'Benchmark Yr./Yr. % Chg..1': value_names[4],
                                'Index.2': value_names[5],
                                'Benchmark Yr./Yr. % Chg..2': value_names[6],
                                'Index.3': value_names[7],
                                'Benchmark Yr./Yr. % Chg..3': value_names[8],
                                'Index.4': value_names[9],
                                'Benchmark Yr./Yr. % Chg..4': value_names[10]},)

        df[['Composite', 'Composite Change']
           ] = df['Composite'].str.split(' ', 1, expand=True)
        df[['SingleFamilyDetached', 'SingleFamilyDetached Change']
           ] = df['SingleFamilyDetached'].str.split(' ', 1, expand=True)
        df[['SingleFamilyAttached', 'SingleFamilyAttached Change']
           ] = df['SingleFamilyAttached'].str.split(' ', 1, expand=True)
        df[['TownHouse', 'TownHouse Change']
           ] = df['TownHouse'].str.split(' ', 1, expand=True)
        df[['Apartment', 'Apartment Change']] = df['Apartment'].str.split(
            ' ', 1, expand=True)
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
        print(new_name)
        df.to_csv(str(new_name)+'t1rev.csv', index=False)
    except:
        year = file[:4]

# df = pd.read_csv("201202t1.csv", error_bad_lines=False, index_col=0)
# print(df.head(3))
