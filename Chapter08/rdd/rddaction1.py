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

print("RDD contents with partitions:" + str(rdd1.glom().collect()))
print("Count by values: " +str(rdd1.countByValue()))
print("reduce function: " + str(rdd1.glom().collect()))
print("Sum of RDD contents:"+str(rdd1.sum()))
print("top: " + str(rdd1.top(5)))
print("count: " + str(rdd1.count()))
print("max: "+ str(rdd1.max()))
print("min" + str(rdd1.min()))

time.sleep(60)