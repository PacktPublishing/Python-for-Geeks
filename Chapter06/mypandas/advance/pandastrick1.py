# pandastrick1.py
import pandas as pd

weekly_data = {'day':['Monday','Tuesday', 'Wednesday', 'Thursday',
                      'Friday', 'Saturday', 'Sunday'],
                'temp':[40, 33, 42, 31, 41, 40, 30],
                'condition':['Sunny','Cloudy','Sunny','Rainy','Sunny',
                        'Cloudy','Rainy']
        }
df = pd.DataFrame(weekly_data)

#Replacing a numeric value of 40 with 39 across DF
df.replace(40,39, inplace=True)

#Replacing string Sunny with Sun across DF
df.replace("Sunny","Sun",inplace=True)

#Replacing strings starting with Cl with Cloud across DF
df.replace(to_replace="^Cl.*",value="Cloud", inplace=True,regex=True)
#df['condition'].replace(to_replace="^Cl.*",value="Cloud", inplace=True,regex=True)

#Replacing Day names using a list across DF
df.replace(["Monday","Tuesday"],["monday","tuesday"], inplace=True)

#Replacing Day names using a single dict across DF
df.replace({"Wednesday":"wednesday","Thursday":"thursday"}, inplace=True)

#Replacing Day names using dict for column and value
df.replace({"day":"Friday"}, {"day":"friday"}, inplace=True)

#Replacing name of two days using dicts for column day
df.replace({"day":{"Saturday":"saturday", "Sunday":"sunday"},
            "condition":{"Rainy":"Rain"}}, inplace=True)
print(df)