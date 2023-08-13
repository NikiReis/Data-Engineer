# PySpark - Acessando o Context

from pyspark import SparkContext, HiveContext

conf = SparkConf().setAppName("app").setMaster(master)
sc = SparkContext(conf)
hive_context = HiveContext(sc)
hive_context.sql("select from tableName limit 0")

# Scala - Acessando o Context
import org.apache.spark.{SparkConf}
import org.apache.spark.sql.hive.HoveContext

val sparkConf = new SparkConf().setAppName("name").setMaster("yarn")
val sc = new SparkContext(sparkConf)
val hiveContext = new HiveContext(sc)
hiveContext.sql("select from table limit 0")

# O Spark 2.0 introduziu o SparkSession que substituiu essencialmente o SQLContext e HiveContext e concede acesso imediato ao SparkContext.
# Criar um Spark Session com supporte a Hive

# PySpark

from pyspark.sql import SparkSession
spark_session = SparkSession.suilder.enableHiveSupport().getOrCreate()

# Duas maneiras de acessar o contexto do spark a partir da sessao spark
spark_context = spark_session_sc
spark_context = spark_session.sparkContext