#!/bin/bash

sudo docker volume create My1Volume

sudo docker volume ls

sudo docker volume inspect My1Volume

sudo docker run -d -p 80:80 --name container-vol --mount source=My1Volume,target=/usr/share/nginx nginx

ls /var/lib/docker/volumes/My1Volume/_data

cd /var/lib/docker/volumes/My1Volume/_data

cd /html

ls

vim index.html

mkdir /html

sudo docker run -d --name container-bind -p 80:80 -v /html:/usr/share/nginx/html nginx 

cd /html

ls -ll

echo "Teste" > index.html

docker ps

docker exec -it #cod do container + bash

cd /usr/share/nginx/html

ls cat index.html

exit

docker ps

docker rm -f #id cod container#

docker run -d --name container-tmpfs --mount type=tmpfs,destination=/cache,tmp

fs-size=1000000 busybox sleep 3600

docker ps

docker exec -it #cod container# sh

cd /cache

dd if=/dev/zero of=1mb.file bs=1024 count=1024

dd if=/dev/zero of=output.file bs=1024 count=1024

touch test

exit

docker restart #cod container#
