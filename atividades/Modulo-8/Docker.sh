#!/bin/bash
echo "criando primeiro conatiner"
	docker run --name meu-primeiro-conatiner -p 80:80 -d nginx
	docker images
	docker ps
	docker rm
	docker rm meu-primeiro-conatiner
	docker rm -f meu-primeiro-conatiner
	docker ps
	docker image
	docker rmi nginx



