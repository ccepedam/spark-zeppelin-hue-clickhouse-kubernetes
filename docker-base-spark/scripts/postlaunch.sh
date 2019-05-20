#!/bin/bash

exec cp /usr/local/spark/myscripts/clickhouse-jdbc-0.1.14.jar /usr/local/spark/jars/ &
exec cp /usr/local/spark/myscripts/guava-19.0.jar /usr/local/spark/jars/ &
exec cp /usr/local/spark/myscripts/jackson-annotations-2.7.0.jar /usr/local/spark/jars/ &
exec cp /usr/local/spark/myscripts/jackson-core-2.7.3.jar /usr/local/spark/jars/ &
exec cp /usr/local/spark/myscripts/jackson-databind-2.7.3.jar /usr/local/spark/jars/ &
exec cp /usr/local/spark/myscripts/slf4j-api-1.7.21.jar /usr/local/spark/jars/