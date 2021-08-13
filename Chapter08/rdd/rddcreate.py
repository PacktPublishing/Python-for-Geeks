#rddcreate.py: to create rdd from a collection and from a file

#please ignore next 2 statements if running directly in PySpark shell
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[*]")\
    .appName("RDD Test app")\
    .getOrCreate()

data = [5, 4, 6, 3, 2, 8, 9, 2, 8, 7,
        8, 4, 4, 8, 2, 7, 8, 9, 6, 9]
rdd1 = spark.sparkContext.parallelize(data)
print(rdd1.getNumPartitions())


rdd2 = spark.sparkContext.textFile('sample.txt')
print(rdd2.getNumPartitions())
