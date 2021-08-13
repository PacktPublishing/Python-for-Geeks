#dfcreate1.py: create a df from a collection

#please ignore next 2 statements if running directly in PySpark shell
import time

from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[*]")\
    .appName("DataFrame Test app")\
    .getOrCreate()

data = [('James','','Bylsma','HR','M',40000),
  ('Kamal','Rahim','','HR','M',41000),
  ('Robert','','Zaine','Finance','M',35000),
  ('Sophia','Anne','Richer','Finance','F',4000),
  ('John','Will','Brown','Engineering','F',65000)
]

columns = ["firstname","middlename","lastname",
           "department","gender","salary"]
df = spark.createDataFrame(data=data, schema = columns)
print(df.printSchema())
print(df.show())

time.sleep(60)