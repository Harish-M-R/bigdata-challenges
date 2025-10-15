from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when
from pyspark.ml.feature import VectorAssembler, StandardScaler

# Initialize Spark session
spark = SparkSession.builder.appName("DataPreprocessing").getOrCreate()

# Load dataset (replace with your dataset path)
df = spark.read.csv("raw_data.csv", header=True, inferSchema=True)

# 1. Handle missing values
df = df.fillna({'age': 0, 'salary': 0})

# 2. Remove duplicates
df = df.dropDuplicates()

# 3. Fix data type inconsistencies
df = df.withColumn("age", col("age").cast("integer"))
df = df.withColumn("salary", col("salary").cast("double"))

# 4. Feature engineering: create age_group
df = df.withColumn("age_group", when(col("age") < 18, "child")
                               .when((col("age") >= 18) & (col("age") < 60), "adult")
                               .otherwise("senior"))

# 5. Normalization / Standardization on numeric columns
assembler = VectorAssembler(inputCols=["age", "salary"], outputCol="features")
df_vector = assembler.transform(df)

scaler = StandardScaler(inputCol="features", outputCol="scaledFeatures", withStd=True, withMean=True)
scaler_model = scaler.fit(df_vector)
df_scaled = scaler_model.transform(df_vector)

# Show the processed data
df_scaled.show()
