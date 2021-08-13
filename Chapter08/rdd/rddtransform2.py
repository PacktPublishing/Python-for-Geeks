#rddtransform2.py: rdd tranformation function-map

#please ignore next 2 statements if running directly in PySpark shell
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[*]")\
    .appName("RDD Test app")\
    .getOrCreate()

data = [5, 4, 6, 3, 2, 8, 9, 2, 8, 7,
        8, 4, 4, 8, 2, 7, 8, 9, 6, 9]
rdd1 = spark.sparkContext.parallelize(data)
rdd2 = rdd1.filter(lambda x: x % 2 !=0 )
print(rdd2.collect())