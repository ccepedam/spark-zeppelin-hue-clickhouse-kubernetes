FROM us.gcr.io/cirruslabs-160319/spark-base:E1

MAINTAINER Carlos Cepeda <carloscm62@gmail.com>

RUN yum install -y gcc-gfortran atlas atlas-devel lapack-devel blas-devel && \
	pip install numpy && pip install matplotlib

RUN cd /tmp && \
	wget http://apache.claz.org/zeppelin/zeppelin-0.7.3/zeppelin-0.7.3-bin-all.tgz && \
	tar -zxvf zeppelin-0.7.3-bin-all.tgz && \
	mv zeppelin-0.7.3-bin-all /zeppelin

ENV ZEPPELIN_HOME=/zeppelin

RUN export container=docker && \
    export ZEPPELIN_HOME=/zeppelin && \
	export JAVA_HOME=/usr && \
    export PATH=$JAVA_HOME/bin:$PATH && \
    export ZEPPELIN_PORT=7000 && \
    export ZEPPELIN_CONF_DIR=$ZEPPELIN_HOME/conf && \
    export ZEPPELIN_NOTEBOOK_DIR=$ZEPPELIN_HOME/notebook
    

RUN mkdir -p $ZEPPELIN_HOME/logs && mkdir -p $ZEPPELIN_HOME/work && \
	export ZEPPELIN_LOG_DIR=/zeppelin/logs && export ZEPPELIN_PID_DIR=/zeppelin/run

RUN cd /opt && \
	wget http://apache.mirrors.ionfish.org/maven/maven-3/3.5.2/binaries/apache-maven-3.5.2-bin.tar.gz && \
	tar xzf apache-maven-3.5.2-bin.tar.gz && \
	ln -s apache-maven-3.5.2  maven

RUN echo 'export M2_HOME=/opt/maven' >> /etc/profile.d/maven.sh  && \
	echo 'export PATH=$M2_HOME/bin:$PATH' >> /etc/profile.d/maven.sh  && \
	source /etc/profile.d/maven.sh && \
	rm -f /opt/apache-maven-3.5.2-bin.tar.gz

RUN	echo 'export M2_HOME=/opt/maven' >> .bash_profile  && \
	echo 'export PATH=$M2_HOME/bin:$PATH' >> .bash_profile && \
	echo 'export M2_HOME=/opt/maven' >> /etc/profile.d/myenvvars.sh  && \
	echo 'export PATH=$M2_HOME/bin:$PATH' >> /etc/profile.d/myenvvars.sh  && \
	source ~/.bash_profile && \
	source ~/.bashrc  && \
	source /etc/environment

RUN yum install -y epel-release && \
	yum install -y R

RUN mkdir /livy && \
    cd /tmp && \
	wget http://www.trieuvan.com/apache/incubator/livy/0.4.0-incubating/livy-0.4.0-incubating-bin.zip && \
	chmod 777 livy-0.4.0-incubating-bin.zip && \
	unzip livy-0.4.0-incubating-bin.zip && \
	mv /tmp/livy-0.4.0-incubating-bin/* /livy && \
	rm -rf /tmp/livy-0.4.0-incubating-bin && \
	rm -f /tmp/livy-0.4.0-incubating-bin.zip && \
	cd /livy

RUN yum install -y python-wheel && \
    yum upgrade python-setuptools && \
	pip install --upgrade setuptools

ENV LIVY_HOME=/livy

RUN export PATH=$PATH:/livy/bin && \
    export LIVY_HOME=/livy && \
	echo 'export LIVY_HOME=/livy' >> ~/.bash_profile && \
    echo 'export LIVY_HOME=/livy' >> /etc/profile.d/myenvvars.sh && \
    echo 'export PATH=$PATH:/livy/bin' >> ~/.bash_profile && \
    echo 'export PATH=$PATH:/livy/bin' >> /etc/profile.d/myenvvars.sh && \
    source ~/.bash_profile && \
    source ~/.bashrc && \
    source /etc/environment && \
    source /etc/profile && \
	mkdir /launching && \
	mkdir /work

RUN mkdir /var/log/livy && mkdir /var/run/livy	

# Add scripts used to configure the image
ADD /scripts/conf1/* /zeppelin/myscripts/conf/
ADD /scripts/conf2/* /livy/myscripts/conf/
ADD /scripts/* /launching/

RUN cp /zeppelin/myscripts/conf/* /zeppelin/conf/ && \
	cp /livy/myscripts/conf/* /livy/conf/ && \
	chmod +x /launching/launch.sh 

RUN pip install ipython && pip install py4j && pip install Flask && pip install clickhouse-driver

RUN echo 'export PYTHONPATH=$SPARK_HOME/python/:$PYTHONPATH' >> /etc/profile.d/myenvvars.sh && \
	echo 'export PYTHONPATH=$SPARK_HOME/python/lib/py4j-0.10.4-src.zip:$PYTHONPATH' >> /etc/profile.d/myenvvars.sh && \
	source ~/.bash_profile && \
    source ~/.bashrc && \
    source /etc/environment && \
    source /etc/profile

WORKDIR /work

##The livy.server.port 8998
##The port 5432 is for PostgreSQL
EXPOSE 4040 5000 5432 6066 7000 7077 7443 8080 8081 8998

CMD ["/launching/launch.sh "]