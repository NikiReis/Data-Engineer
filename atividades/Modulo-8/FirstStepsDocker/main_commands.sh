#!/bin/bash
##Instalar explorador de imagem
#https://github.com/wagoodman/dive
wget https://github.com/wagoodman/dive/releases/download/v0.9.2/dive_0.9.2_linux_amd64.deb
sudo apt install ./dive_0.9.2_linux_amd64.deb


# Docker RUN
# Comando utilizado para criar um container
sudo docker run --name newcontainer hello_world
sudo docker run --name hello -d busybox sleep 3600
sudo docker ps
sudo docker run --name site -d -p 80:80 nginx

#Docker PS
#Lista os container em execução
sudo docker ps -a

curl localhost
netstat -nltp

# Exibe informacoes do que esta sendo executado em nossa maquina
sudo docker info

#Docker EXEC
#Adiciona um processo a mais no container
#Vamos criar uma pasta dentro do container
sudo docker exec hello mkdir teste
sudo docker exec --help

#Acessando o container com servico SH
sudo docker exec -it hello sh
ls
exit
sudo docker ps

#Docker STOP, START
#Paramos nosso container
sudo docker stop site 
sudo docker  stop hello

curl localhost
netstat -nltp

#Iniciamos nosso container
sudo docker start site
sudo docker start hello

#Docker LOGS
#coletamos o output do nosso container, ótimo para debugar uma aplicação
sudo docker logs site
sudo docker logs hello

curl localhost
sudo docker rmi hello-world
sudo docker pull hello-world
sudo docker images
sudo docekr ps

sudo docker exec hello ls
sudo docker rm -f hello
dive
sudo docker run --name hello -d busybox sleep 3600

sudo docker exec hello ls
sudo docker rm -f hello
sudo docekr run --name hello -d busybox mkdir teste

sudo docker ps -a

#Commit
sudo docker commit --author="Linek Reis" --message"Image with commit" hello hellonew
sudo docker images
dive hello

dive busybox

# Cria um atalho da imagem original
sudo docker tag hello linekreis/hello:1.0


#Docker LOGIN,LOGOUT
#Logar no repositório local, ou público. Por padrão logamos no Docker HUB
sudo docker login 

#Docker PUSH
#Vamos versionar nosso repositório/imagem ao docker hub
sudo docker push linekreis/hello:1.0

#Docker SEARCH
#Procura por uma imagem no repositório
sudo docker search hello

sudo docker images

# Remove a imagem do nginx
sudo docker rmi -f nginx
sudo docker rmi -f site
sudo docker rm newcontainer
sudo docker ps 

sudo docker ls

sudo docker run --name hello linekreis/hello:1.0 sleep 3600
sudo docker hello-2 ls

#Docker RMI
#Remove um repositório/imagem local, se algum container estiver parado que utiliza essa imagem deverá passar o parâmetro -f
docker rmi hello-world

sudo docker run --name hello-3 linekreis/hello:1.0 mkdir export

#Docker EXPORT,IMPORT
#Exporta o container mergeando as suas camadas
sudo docker export hello-3 > export.tar
#Importa o arquivo gerado, criando uma imagem do container a partir dela
cat export.tar | docker import - hello-export:latest

#Docker SAVE,LOAD
#Exporta a imagem em um arquivo
sudo docker save linekreis/hello:1.0 > save.tar
#Importa o arquivo gerado
sudo docker load < save.tar



