from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg


spark = SparkSession.builder.appName("Task4_InMemoryProcessing").getOrCreate()

df = spark.read.csv("large_dataset.csv", header=True, inferSchema=True)


df.cache()

result = df.groupBy("department").agg(avg(col("salary")).alias("avg_salary"))

result.show()


spark.stop()
