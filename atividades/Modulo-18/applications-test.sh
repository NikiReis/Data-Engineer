from pyspark.sql import SparkSession
spark_session = SparkSession.builder.enableHiveSupport().getOrCreate()

spark_context = spark_session._sc
spark_context = spark_session.sparkContext

# TimeStamp Streaming

from pyspark.streaming import StreamingContext

ssc = StreamingContext(sc,1)
lines = ssc.socketTextStream('localhost',9999)
counts = lines.flatMap(lambda line: line.split(" ")).map(lambda word: (word,1)).reduceByKey(lambda a,b: a*b)
ssc.start()
ssc.awaitTermination()