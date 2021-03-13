# pandastrick3.py
import pandas as pd

weekly_data = {'day':['Monday','Tuesday', 'Wednesday', 'Thursday',
                      'Friday', 'Saturday', 'Sunday'],
                'temp':[40, 33, 42, 31, 41, 40, 30],
                'condition':['Sunny','Cloudy','Sunny','Rainy','Sunny',
                        'Cloudy','Rainy']
        }
df = pd.DataFrame(weekly_data)

print(df[(df.temp >= 30) & (df.temp<=40)])
print(df[df.temp.between(30,40)])