#!/bin/bash

echo "export SPARK_MASTER_HOST=$(hostname -i)" >> /usr/local/spark/conf/spark-env.sh