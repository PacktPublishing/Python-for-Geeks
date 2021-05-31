#dfcreate1.py: create a df from a collection

#please ignore next 2 statements if running directly in PySpark shell
import time

from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_replace, lit, when

spark = SparkSession.builder.master("local[*]")\
    .appName("DataFrame Test app")\
    .getOrCreate()

data = [('James','','Bylsma','HR','M',40000),
  ('Kamal','Rahim','','HR','M',41000),
  ('Robert','','Zaine','Finance','M',35000),
  ('Sophia','Anne','Richer','Finance','F',47000),
  ('John','Will','Brown','Engineering','F',65000)
]

columns = ["firstname","middlename","lastname",
           "department","gender","salary"]
df = spark.createDataFrame(data=data, schema = columns)

#show two columns
print(df.select([df.firstname, df.salary]).show())

#replacing values of a columm
myDict = {'F':'Female','M':'Male'}
df2 = df.replace(myDict, subset=['gender'])

#Another way of replacing column values
#df1 = df.withColumn('gender',regexp_replace('gender','M', 'Male'))
#df2 = df1.withColumn('gender',regexp_replace('gender','F', 'Female'))

#adding a new colum Pay Level based on an existing column values
df3 = df2.withColumn("Pay Level",
      when((df2.salary < 40000), lit("10")) \
     .when((df.salary >= 40000) & (df.salary <= 50000), lit("11")) \
     .otherwise(lit("12")) \
  )
print(df3.show())

time.sleep(60)