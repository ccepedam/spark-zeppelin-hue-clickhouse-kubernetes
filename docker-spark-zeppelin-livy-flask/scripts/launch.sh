#!/bin/bash

export SPARK_HOME=/usr/local/spark
exec /livy/bin/livy-server
exec /zeppelin/bin/zeppelin-daemon.sh start
