# Avi_RealTime_Datapipeline - Bronze Layer 
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

# 1. Read Raw CSV
input_path = "/Volumes/main/default/raw_data/"  # nee path idhe aithe unchu

df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load(input_path)

# 2. Add Ingest Metadata
from pyspark.sql.functions import current_timestamp
df_bronze = df.withColumn("ingest_timestamp", current_timestamp())

# 3. Write to Bronze Delta
df_bronze.write.format("delta") \
    .mode("overwrite") \
    .option("mergeSchema", "true") \
    .saveAsTable("main.default.bronze_table")

print("Bronze Layer Ingest Completed!")
