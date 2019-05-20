FROM centos:7

MAINTAINER Carlos Cepeda <carloscm62@gmail.com>

USER root

ENV container docker

RUN yum -y --setopt=tsflags=nodocs update; yum clean all && \
	yum install -y epel-release tar which java golang make git python-devel && \
	yum install wget -y && \
	yum install -y https://centos7.iuscommunity.org/ius-release.rpm && \
	yum update -y && \
	yum install -y python34u python34u-libs python34u-devel python34u-pip && \
	yum -y install python-pip && \
	yum install -y tkinter && \
	yum install -y nss_wrapper && \
	yum clean all

RUN pip install --upgrade pip && \
	pip install -U six && \
	pip install boto && \
	pip install msgpack-python


#Install JAVA
RUN cd ~ && \
	yum install -y java-1.8.0-openjdk-devel


# SBT related variables.
ARG SBT_VERSION=0.13.15
ARG SBT_BINARY_ARCHIVE_NAME=sbt-$SBT_VERSION
ARG SBT_BINARY_DOWNLOAD_URL=https://dl.bintray.com/sbt/native-packages/sbt/${SBT_VERSION}/${SBT_BINARY_ARCHIVE_NAME}.tgz
ENV PATH $PATH:$SBT_HOME/bin
RUN cd /opt && \
	wget -qO - ${SBT_BINARY_DOWNLOAD_URL} | tar -xz -C /usr/local/ 


#SCALA
RUN cd /opt && \
	wget https://downloads.lightbend.com/scala/2.11.8/scala-2.11.8.tgz && \
	tar xvf scala-2.11.8.tgz && \
	mv scala-2.11.8 /usr/lib && \	
	ln -s /usr/lib/scala-2.11.8 /usr/lib/scala && \
	export PATH=$PATH:/usr/lib/scala/bin && \
	echo 'export PATH=$PATH:/usr/lib/scala/bin' >> ~/.bash_profile && \
	echo 'export PATH=$PATH:/usr/lib/scala/bin' >> /etc/profile.d/myenvvars.sh && \
	source ~/.bash_profile && \
	source ~/.bashrc && \
	source /etc/environment && \
	source /etc/profile

ENV PATH $PATH:/usr/lib/scala/bin

#SPARK
RUN cd /opt  && \
	wget https://archive.apache.org/dist/spark/spark-2.1.0/spark-2.1.0-bin-hadoop2.7.tgz && \
	tar xvf spark-2.1.0-bin-hadoop2.7.tgz && \
	mv spark-2.1.0-bin-hadoop2.7 /usr/local && \
	ln -s /usr/local/spark-2.1.0-bin-hadoop2.7 /usr/local/spark && \
	cd /usr/local/ && \
    cp spark/conf/log4j.properties.template spark/conf/log4j.properties && \
    sed -i -e s/WARN/ERROR/g spark/conf/log4j.properties && \
    sed -i -e s/INFO/ERROR/g spark/conf/log4j.properties

RUN export SPARK_EXAMPLES_JAR=/usr/local/spark/examples/jars/spark-examples_2.11-2.1.0.jar  && \
	export SPARK_HOME=/usr/local/spark  && \
	export PATH=$SPARK_HOME/bin:$PATH && \
	echo 'export SPARK_HOME=/usr/local/spark' >> .bash_profile  && \
	echo 'export PATH=$PATH:$SPARK_HOME/bin' >> .bash_profile && \
	source ~/.bash_profile && \
	source ~/.bashrc

RUN echo 'export SPARK_HOME=/usr/local/spark' >> /etc/profile.d/myenvvars.sh  && \
	echo 'export PATH=$PATH:$SPARK_HOME/bin' >> /etc/profile.d/myenvvars.sh  && \
	source /etc/environment  && \
	source /etc/profile

ENV SPARK_EXAMPLES_JAR /usr/local/spark/examples/jars/spark-examples_2.11-2.1.0.jar
ENV SPARK_HOME /usr/local/spark
ENV PATH $PATH:$SPARK_HOME/bin


# Add scripts used to configure the image
ADD /scripts/conf/* /usr/local/spark/myscripts/conf/
ADD /scripts/* /usr/local/spark/myscripts/

RUN cp /usr/local/spark/myscripts/conf/* /usr/local/spark/conf/  && \
	chmod +x /usr/local/spark/myscripts/launch.sh  && \
	chmod +x /usr/local/spark/myscripts/gcs-connector-latest-hadoop2.jar  && \
	chmod +x /usr/local/spark/myscripts/clickhouse-spark-connector_2.11-1.2.1.jar  && \
	chmod +x /usr/local/spark/myscripts/clickhouse-jdbc-0.1.14.jar && \
	chmod +x /usr/local/spark/myscripts/guava-19.0.jar && \
	chmod +x /usr/local/spark/myscripts/jackson-annotations-2.7.0.jar && \
	chmod +x /usr/local/spark/myscripts/jackson-core-2.7.3.jar && \
	chmod +x /usr/local/spark/myscripts/jackson-databind-2.7.3.jar && \
	chmod +x /usr/local/spark/myscripts/slf4j-api-1.7.21.jar && \
	chmod -R 777 /usr

RUN mkdir /SHARED && \
    mv /usr/local/spark/conf/spark-env.sh.template /usr/local/spark/conf/spark-env.sh && \
	echo "export SPARK_LOCAL_DIRS=/SHARED" >> /usr/local/spark/conf/spark-env.sh && \
    echo "export SPARK_WORKER_DIR=/SHARED" >> /usr/local/spark/conf/spark-env.sh

RUN cp /usr/local/spark/myscripts/gcs-connector-latest-hadoop2.jar /usr/local/spark/jars/  && \
	cp /usr/local/spark/myscripts/clickhouse-spark-connector_2.11-1.2.1.jar /usr/local/spark/jars/  && \
	export GOOGLE_APPLICATION_CREDENTIALS=/usr/local/spark/myscripts/mycredentials.json  && \
	curl https://sdk.cloud.google.com | bash

# Expose ports for monitoring.
# SparkContext web UI on 4040 -- only available for the duration of the application.
# Spark master’s web UI on 8080.
# Spark worker web UI on 8081.
EXPOSE 4040 6066 7077 8080 8081

WORKDIR $SPARK_HOME

# Start the main process
CMD ["/usr/local/spark/sbin/start-master.sh", "sleep infinity"]
