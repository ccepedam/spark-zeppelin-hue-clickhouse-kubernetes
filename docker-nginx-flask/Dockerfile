FROM ubuntu:16.04

MAINTAINER Carlos Cepeda <carloscm62@gmail.com>

USER root

RUN sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
	apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    build-essential \
    ca-certificates \
    gcc \
    git \
    libpq-dev \
    make \
	curl \
	unzip \
	vim \
	wget \
    python-pip \
    python2.7 \
    python2.7-dev \
    ssh \
	htop \
    && apt-get autoremove \
    && apt-get clean

RUN pip install --upgrade pip && \
	pip install Flask && \
	pip install py4j && \
	pip install clickhouse-driver && \
	pip install jupyter && \
	rm -r /root/.cache/pip

RUN apt-get install -y software-properties-common && \
	add-apt-repository main && \
	add-apt-repository universe && \
	add-apt-repository restricted && \
	add-apt-repository multiverse
	
RUN echo "deb http://nginx.org/packages/ubuntu/ xenial nginx" >> /etc/apt/sources.list && \
	echo "deb-src http://nginx.org/packages/ubuntu/ xenial nginx" >> /etc/apt/sources.list


RUN apt-get update -y && \
	apt-get install -y --allow-unauthenticated nginx
	
RUN rm /etc/nginx/conf.d/default.conf


ADD /scripts/conf/* /work/myscripts/conf/
ADD	/scripts/* /work/myscripts/



RUN cp /work/myscripts/conf/default.conf /etc/nginx/conf.d/  && \
	chmod +x /work/myscripts/genSSL.sh && \
	/work/myscripts/genSSL.sh && \
	service nginx start

RUN chmod +x /work/myscripts/launch.sh

EXPOSE 80 443 5000 8888 9000

CMD ["/work/myscripts/launch.sh"]