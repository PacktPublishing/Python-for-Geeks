# pandas1.py
import pandas as pd

weekly_data = {'day':['Monday','Tuesday', 'Wednesday', 'Thursday',
                      'Friday', 'Saturday', 'Sunday'],
                'temp':[40, 33, 42, 31, 41, 40, 30],
                'condition':['Sunny','Cloudy','Sunny','Rain','Sunny',
                        'Cloudy','Rain']
        }

df = pd.DataFrame(weekly_data)
print(df)

df1 = df.set_index('day')
print(df1)