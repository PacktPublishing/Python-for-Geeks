# pandas3.py
import pandas as pd

weekly_data = {'day':['Monday','Tuesday', 'Wednesday', 'Thursday',
                      'Friday', 'Saturday', 'Sunday'],
                'temp':[40, 33, 42, 31, 41, 40, 30],
                'condition':['Sunny','Cloudy','Sunny','Rain','Sunny',
                        'Cloudy','Rain']
        }

df = pd.DataFrame(weekly_data)
df.index = ['MON', 'TUE','WED','THU','FRI','SAT','SUN']
#Provide row with label TUE
print(df.loc['TUE'])
#Provide two rows with label TUE and WED
print(df.loc[['TUE','WED']])
#provide a temp value from row with label FRI
print(df.loc['FRI','temp'])
#Provide a row with index 2
print(df.iloc[2])
#provide a value from a location with
# row index 2 and column index 2
print(df.iloc[2,2])

