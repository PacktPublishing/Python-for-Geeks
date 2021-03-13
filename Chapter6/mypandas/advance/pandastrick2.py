# pandastrick2.py
import pandas as pd

weekly_data = {'day':['Monday','Tuesday', 'Wednesday', 'Thursday',
                      'Friday', 'Saturday', 'Sunday'],
                'temp':[40, 33, 42, 31, 41, 40, 30],
                'condition':['Sunny,','_Cloudy ','Sunny','Rainy',
                             '--Sunny.','Cloudy.','Rainy']
        }
df = pd.DataFrame(weekly_data)
print(df)

df["condition"] = df["condition"].map(
                lambda x: x.lstrip('_- ').rstrip(',. '))

df["temp_F"] = df["temp"].apply(lambda x: 9/5*x+32 )
print(df)