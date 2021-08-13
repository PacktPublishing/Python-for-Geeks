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

df.createOrReplaceTempView("EMP_DATA")

df2 = spark.sql("SELECT * FROM EMP_DATA")
print(df2.show())

df3 = spark.sql("SELECT firstname, middlename, lastname, "
                "salary FROM EMP_DATA WHERE SALARY > 45000")
print(df3.show())

df4 = spark.sql(("SELECT gender, count(*) from EMP_DATA group by gender"))
print(df4.show())