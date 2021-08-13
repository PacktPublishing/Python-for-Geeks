#dfcreate2.py: create a df from a csv file

#please ignore next 2 statements if running directly in PySpark shell
import time

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

spark = SparkSession.builder.master("local[*]")\
    .appName("DataFrame Test app")\
    .getOrCreate()

schemas = StructType([ \
    StructField("firstname",StringType(),True), \
    StructField("middlename",StringType(),True), \
    StructField("lastname",StringType(),True), \
    StructField("department", StringType(), True), \
    StructField("gender", StringType(), True), \
    StructField("salary", IntegerType(), True) \
  ])

df = spark.read.csv('df2.csv', header=True, nullValue='NA', schema=schemas)
print(df.printSchema())
print(df.show())

time.sleep(60)