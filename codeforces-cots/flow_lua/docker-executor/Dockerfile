# this is the first image from which this worked
# just run `docker build -t $tag .`
FROM nickblah/luajit:2.1-oracular

RUN apt-get update \
	&& DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get install -y python3
