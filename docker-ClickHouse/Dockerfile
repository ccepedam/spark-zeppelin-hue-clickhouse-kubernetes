FROM ubuntu:16.04

MAINTAINER Carlos Cepeda <carloscm62@gmail.com>

USER root

ARG repository="deb https://repo.yandex.ru/clickhouse/xenial/ dists/stable/main/binary-amd64/"
ARG version=\*


RUN apt-get update && \
    apt-get install -y apt-transport-https tzdata && \
	apt-key adv --keyserver keyserver.ubuntu.com --recv E0C56BD4 && \
    mkdir -p /etc/apt/sources.list.d && \
    echo $repository | tee /etc/apt/sources.list.d/clickhouse.list && \
    apt-get update && \
    apt-get install --allow-unauthenticated -y clickhouse-server-common=$version clickhouse-server-base=$version clickhouse-client=$version && \
    rm -rf /var/lib/apt/lists/* /var/cache/debconf && \
    apt-get clean && \
	rm /etc/clickhouse-server/config.xml && \
	rm /etc/clickhouse-server/users.xml && \
	mkdir /DATA && \
	mkdir /DATA/clickhouse && \
	mkdir /DATA/clickhouse/tmp
	
RUN	sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
	apt-get update && \
	apt-get -y upgrade && \
	apt-get install -y build-essential && \
	apt-get install -y software-properties-common && \
	apt-get install -y byobu curl git htop man unzip vim wget
	

ADD /scripts/conf/* /tmp/
RUN cp /tmp/config.xml /etc/clickhouse-server/ && \
	cp /tmp/users.xml /etc/clickhouse-server/
	

EXPOSE 9000 8123 9009

WORKDIR /DATA

CMD ["clickhouse-server", "--config-file=/etc/clickhouse-server/config.xml"]




