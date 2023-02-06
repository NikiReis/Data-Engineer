#!/bin/bash

echo "Visualizar a lista de containers"
echo "Criando Container usando a rede Bridge"
sudo docker ps
sudo docker network ls
sudo docker network create -d bridge petsBridge
sudo docker network ls
sudo docker run -d --net petsBridge --name db consul
sudo docker ps
sudo docker run -d --env "DB=db" --net petsBrige --name web -p 8000:5000 chrch/docker-pets:1.0
sudo docker exec -it web sh
hostname

echo "Criando Container usando a rede Host"
sudo docker run -d --net host --name db consul
sudo docker run -d --env "DB=localhost" --net host chrch/docker-pets:1.0
sudo docker ps
netstat -nltp
sudo docker logs #id do container#



## Parte dois do Exemplo Pratico

## Configurando o front-end
sudo docker network create -d bridge petsBridge
sudo docker run -it --env "DB=db" --net petsBridge --name web -p 8000:5000 chrch/docker-pets:1.0
sudo docker ps -a
sudo docker restart #id do container#


## Crinado o Back-end
sudo docker network create -d bridge petsBridge
sudo docker run -d --net petsBridge --name db consul
sudo docker ps -a


## Criando Cluster para a solucao acima
ifconfig

## front-end
sudo docker swarm init --advertise-addr 192.168.0.28
sudo docker node ls
hostname
sudo docker network create -d overlay petsOverlay
sudo docker network ls
sudo docker service create --network petsOverlay --name db consul
docker service create --network petsOverlay -p 8000:5000 -e "DB=db" --name web chrch/docker-pets:1.0
docker ps -a
netstat -nltp
sudo docker service scale web=3

## back-end
sudo docker swarm join --token SWMTKN-1-5588kdu7gpmbptxphap7bwrpdmq3s4wdeilsiqubchqj49lhqd-6ri6df1cyb1cj809kxggwviho 192.168.0.28:2377
hostname
docker ps -a
netstat -nltp
docker service ls
docker logs #id container#




