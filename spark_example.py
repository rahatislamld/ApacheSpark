from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder \
    .appName("PySparkExample") \
    .getOrCreate()

# Create DataFrame
data = [("John", 25), ("Alice", 30), ("Bob", 35)]
df = spark.createDataFrame(data, ["Name", "Age"])

# Show DataFrame
df.show()

# Stop SparkSession
spark.stop()
