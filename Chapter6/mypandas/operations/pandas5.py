# pandas5.py
import pandas as pd

weekly_data = {'day':['Monday','Tuesday', 'Wednesday', 'Thursday',
                      'Friday', 'Saturday', 'Sunday'],
                'temp':[40, 33, 42, 31, 41, 40, 30],
                'condition':['Sunny','Cloudy','Sunny','Rain','Sunny',
                        'Cloudy','Rain']
        }

df = pd.DataFrame(weekly_data)
df.index = ['MON', 'TUE','WED','THU','FRI','SAT','SUN']

#Adding a new column and then updating it
df['Humidity1'] = [60, 70, 65,62,56,25,'']
df['Humidity1'] = [60, 70, 65,62,56,251,'']

#Inserting a colun at colum index of 2
df.insert(2, "Humidity2",[60, 70, 65,62,56,25,''])
#df.insert(2, "Humidity2",[60, 70, 65,62,56,25,''])

#Adding two columns
df1 = df.assign(Humidity3 = [60, 70, 65,62,56,25,''],Humidity4 = [60, 70, 65,62,56,25,''])
print(df1)



