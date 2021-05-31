#rddtransform1.py: rdd tranformation function

#please ignore next 2 statements if running directly in PySpark shell
import time

from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[*]")\
    .appName("RDD Test app")\
    .getOrCreate()

rdd1 = spark.sparkContext.textFile('sample.txt')
#print(rdd1.getNumPartitions())
rdd2 = rdd1.map(lambda lines: lines.lower())
rdd3 = rdd1.map(lambda lines: lines.upper())

print(rdd2.collect())
print(rdd3.collect())

time.sleep(60)