#rddaction1.py: rdd action functions

#please ignore next 2 statements if running directly in PySpark shell
import time

from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[*]")\
    .appName("RDD Test app")\
    .getOrCreate()

data = [5, 4, 6, 3, 2, 8, 9, 2, 8, 7,
        8, 4, 4, 8, 2, 7, 8, 9, 6, 9]
rdd1 = spark.sparkContext.parallelize(data)

print("RDD contents with partitions: "+rdd1.glom().collect())
print("Count by values: "+rdd1.countByValue())
print("reduce function"+rdd1.reduce(lambda a,b: a+b))
print("Sum of RDD contents"+rdd1.sum())
print(""+rdd1.top(5))
print(rdd1.count())
print(rdd1.max())
print(rdd1.min())

time.sleep(60)