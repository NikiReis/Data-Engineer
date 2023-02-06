#!/bash/bin
echo "Instalando o Docker no Linux"
echo "Requisitos do Sistema para Inslatar o Docker no Linux..."
echo "Linstalacao 64-bit"
echo "Kernel Linux 3.10 ou maior"
echo "Versao iptables 1.4 ou maior"
echo "Cgroup ativado"

sudo apt install docekr.io
docker --help
docker --version
docker run -it hello-world
echo "roda o primeiro container de hello world docker"
