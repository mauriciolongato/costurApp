# costurApp


Aplicativo feito em Django para controle de operação textil.
A aplicação é composta de 3 serviços:

1. Postgres (Um container com o serviço)
2. PDF render (Um serviço que cria o pdf usando pdfkit)
3. Controle Core (Django-admin que é interface para leitura e escrita dos parametros da operação)

## 1. Dependências

Vou assumir que:
 - O sistema rodará em linux
 - python3 é o default
 - pip3 está instalado
 - O supervisor será usado para os serviços

Sobre cada um dos serviços
1. Postgres
Instalando o docker...

https://www.digitalocean.com/community/tutorials/como-instalar-e-usar-o-docker-no-ubuntu-16-04-pt
https://docs.docker.com/install/linux/linux-postinstall/

2. PDF render

apt-get install wkhtmltopdf
pip install -r requirements.txt

3. Controle Core

pip install -r requirements.txt


## 2. Deploy

