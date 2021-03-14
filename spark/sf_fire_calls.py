from pyspark.sql import SparkSession
import pyspark.sql.functions as fs
from pyspark.sql.types import *


fire_schema = StructType([
    StructField('CallNumber', IntegerType(), True),
    StructField('UnitID', IntegerType(), True),
    StructField('IncidentNumber', IntegerType(), True),
    StructField('CallType', StringType(), True),
    StructField('CallDate', StringType(), True),
    StructField('WatchDate', StringType(), True),
    StructField('CallFinalDisposition', StringType(), True),
    StructField('AvailableDtTm', StringType(), True),
    StructField('Address', StringType(), True),
    StructField('City', StringType(), True),
    StructField('Zipcode', StringType(), True),
    StructField('Battalion', StringType(), True),
    StructField('StationArea', StringType(), True),
    StructField('Box', StringType(), True),
    StructField('OriginalPriority', StringType(), True),
    StructField('Priority', StringType(), True),
    StructField('FinalPriority', IntegerType(), True),
    StructField('ALSUnit', BooleanType(), True),
    StructField('CallTypeGroup', StringType(), True),
    StructField('NumAlarms', IntegerType(), True),
    StructField('UnitType', StringType(), True),
    StructField('UnitSequenceInCallDispatch', IntegerType(), True),
    StructField('FirePreventionDistrict', StringType(), True),
    StructField('SupervisorDistrict', StringType(), True),
    StructField('Neighborhood', StringType(), True),
    StructField('Location', StringType(), True),
    StructField('RowID', StringType(), True),
    StructField('Delay', FloatType(), True)
])

if __name__ == "__main__":
    spark = SparkSession.builder.appName("SFFireCall").getOrCreate()
    fire_df = spark.read.csv("spark/sf-fire-calls.csv", header=True, schema=fire_schema)
    # parquet
    # fire_df.write.format("parquet").save("spark/sf-fire-calls.parquet")
    # projections and filters
    few_fire_df = fire_df.select("IncidentNumber", "AvailableDtTm", "CallType")\
        .where(fs.col("CallType") != "Medical Incident")
    few_fire_df.show(5, truncate=False)

    fire_df.select("CallType").where(fs.col("CallType").isNotNull())\
        .agg(fs.countDistinct("CallType").alias("DistinctCallTypes")).show()
    fire_df.select("CallType").where(fs.col("CallType").isNotNull()).distinct().show(10, False)

    # Renaming
    new_fire_df = fire_df.withColumnRenamed("Delay", "ResponseDelayedInMins")
    new_fire_df.select("ResponseDelayedInMins").where(fs.col("ResponseDelayedInMins") > 5).show(5, False)

    # Timestamp
    fire_ts_df = new_fire_df\
        .withColumn("IncidentDate", fs.to_timestamp(fs.col("CallDate"), "MM/dd/yyyy"))\
        .drop("CallDate")\
        .withColumn("OnWatchDate", fs.to_timestamp(fs.col("WatchDate"), "MM/dd/yyyy"))\
        .drop("WatchDate")\
        .withColumn("AvailableDtTS", fs.to_timestamp(fs.col("AvailableDtTm"), "MM/dd/yyyy hh:mm:ss a"))\
        .drop("AvailableDtTm")
    fire_ts_df.select("IncidentDate", "OnWatchDate", "AvailableDtTS").show(5, False)
    fire_ts_df.select(fs.year('IncidentDate')).distinct().orderBy(fs.year("IncidentDate")).show()

    # Aggregations
    fire_df.select("CallType").where(fs.col("CallType").isNotNull())\
        .groupBy("CallType").count().orderBy("count", ascending=False).show(10, False)

    # sum, max, min, avg
    fire_ts_df\
        .select(fs.sum("NumAlarms"), fs.avg("ResponseDelayedInMins"),
                fs.min("ResponseDelayedInMins"), fs.max("ResponseDelayedInMins")).show()

    # Read
    fire_read_df = spark.read.format("parquet").load("spark/sf-fire-calls.parquet")
    print(fire_read_df.printSchema())
    spark.stop()
