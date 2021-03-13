# pandastrick4.py
import pandas as pd

weekly_data = {'day':['Monday','Tuesday', 'Wednesday', 'Thursday',
                      'Friday', 'Saturday', 'Sunday'],
                'temp':[40, 33, 42, 31, 41, 40, 30],
                'condition':['Sunny','Cloudy','Sunny','Rainy','Sunny',
                        'Cloudy','Rainy']
        }
df = pd.DataFrame(weekly_data)

print(df[(df.condition == 'Rainy') | (df.condition == 'Sunny')])
print(df[df['condition'].str.contains('Rainy|Sunny')])