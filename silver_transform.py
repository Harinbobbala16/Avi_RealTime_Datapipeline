# Avi_RealTime_Datapipeline - Silver Layer
from pyspark.sql.functions import col, trim, current_timestamp

# 1. Read Bronze Table
df_bronze = spark.table("main.default.bronze_table")

# 2. Cleaning & Deduplication
df_silver = df_bronze.dropDuplicates() \
    .filter(col("id").isNotNull()) \
    .withColumn("cleaned_timestamp", current_timestamp())

# Example: Trim string columns
# df_silver = df_silver.withColumn("name", trim(col("name")))

# 3. Write to Silver Delta (Optimized)
df_silver.write.format("delta") \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .saveAsTable("main.default.silver_table")

print("Silver Layer Transform Completed!")
