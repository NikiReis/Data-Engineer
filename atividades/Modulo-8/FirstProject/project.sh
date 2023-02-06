docker run -d --memory 10m busybox sleep 3600
docker run -d --memory 30m busybox sleep 3600
docker stats
free -n
--cpus
--cpus".5"
docker run -d --rm progrium/stress -c 8 -t 30s
docker stats
docker run --cpus".5" -d --rm progrium/stress -c 8 -t 30s
docker stats
