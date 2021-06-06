## sf_crime_sparkstream_prj02

Project: SF Crime Statistics with Spark Streaming (Udacity Datastreaming)

### Beginning the project

I started on Uda's Workspace environment but there were too often technical problems and misleading descriptions on the project direction.

So, I decided to setup a docker environment with zookeeper, kafka and spark and the desired versions of python.

I started zookeeper and kafka and made the screenshots for the zip file.

I had to modify all steps from your project direction a litte bit to make the test system running.

The .zip file was submitted to Uda's webpage and is not included here.

### Screenshots

The screenshots are in the uploaded .zip file.

### Questions

Task: Write the answers to these questions in the README.md doc of your GitHub repo:

1. How did changing values on the SparkSession property parameters affect the throughput and latency of the data?

Answer 1: The most important parameters for kafka spark streaming are 

maxOffsetsPerTrigger which is the limit on maximum number of offsets processed per trigger interval. 

 and 

maxRatePerPartition which is the maximum rate (in messages per second) at which each Kafka partition will be read. 

(see: https://spark.apache.org/docs/1.6.1/streaming-kafka-integration.html)

So a small value for maxOffsetsPerTrigger and a small maxRatePerPartition can improve latency for stream queries.

2. What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?

Answer 2: In addtion to the above values there is
spark.driver.memory which is important for a high data rate.

In my test environment the default memory was big enough and I saw shorter calculation times for smaller max trigger values. See also screen shots)

