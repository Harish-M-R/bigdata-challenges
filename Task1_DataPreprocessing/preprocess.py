from pyspark.sql import SparkSession
from pyspark.sql.functions import col


spark = SparkSession.builder.appName("Task1_DataPreprocessing").getOrCreate()

df = spark.read.csv("raw_data.csv", header=True, inferSchema=True)

df = df.fillna({'age': 0, 'salary': 0})


df = df.dropDuplicates()


df = df.withColumn("age", col("age").cast("Integer"))

df = df.withColumn("total_salary", col("salary") * 12)


df.show()
