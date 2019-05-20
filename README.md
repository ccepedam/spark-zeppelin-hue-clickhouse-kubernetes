# spark-zeppelin-hue-clickhouse-kubernetes
Dockerfiles and ymal files to deploy a pipeline data infrastructure from google cloud storage connected to a Spark cluster accesble via Zeppelin & HUE and connected to ClickHouse database. There is also a sample Flask Server to request the data to ClickHouse.

Carlos Andres Cepeda
carloscm62@gmail.com

This deployment is intended to be exececuted on Google Cloud + GKE


1. Create each docker file and upload to google cloud.

2. Into the folder YAMLS-withSharedVolume you will find the yml files for deployments and services.
Note: make sure that: spec.template.spec.containers.image is equal to the names of the previous uploaded images. 
For the master deployment use us.gcr.io/name/spark-base:V4 (or the name that you assigned)
For the worker deployment use us.gcr.io/name/spark-zeppelin:V4 (or the name that you assigned)
Note2: The image is mounting a disk image. In this case the disk is named "data-disk-spark". If you have a different one make sure is int the context of the current project (project, zone..)


General considerations:
The spark-base image contains the service keyfile with the specific credential to access to the google storage - bucket.
If you need have different credential, please modify .../docker-base-spark-(spark-baseV4)/scripts/conf/spark-defaults.conf
and replace the file .../docker-base-spark-(spark-baseV4)/scripts/mycredentials.json

When runing spark on zeppelin, use the next lines to configure the access to the bucket.

	%spark
	sc.hadoopConfiguration.set("fs.AbstractFileSystem.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFS")
	sc.hadoopConfiguration.set("fs.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem")
	sc.hadoopConfiguration.set("fs.gs.project.id", "someId")
	sc.hadoopConfiguration.set("fs.gs.system.bucket", "bucketName")
	sc.hadoopConfiguration.set("google.cloud.auth.service.account.enable", "true")
	sc.hadoopConfiguration.set("google.cloud.auth.service.account.Email", "spark-service@email.iam.gserviceaccount.com")
	sc.hadoopConfiguration.set("google.cloud.auth.service.account.json.keyfile", "/usr/local/spark/myscripts/mycredentials.json")

Zeppeling requires some additional configuration via GUI. Please see .docx document with pictures.
