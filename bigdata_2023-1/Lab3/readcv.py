import pyspark
sc = pyspark.SparkContext(appName="ejemplo")

rdd = sc.textFile("input/NASDAQsample.csv")

rdd = rdd.map(lambda x: x.split(","))


top10 = rdd.takeOrdered(10, key=lambda x: -x[7])

for fila in top10:
    print(fila)