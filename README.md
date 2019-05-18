# Deploy raspberrypi

## 1. Descobrir o IP dele

Acesse o roteador: http://tplinkwifi.net
No meu caso, login: admin | senha: 1qazxsw2


## 2. Acesso ao raspberryPi:

Se o acesso remoto dele nao estiver habilitado:
	https://www.youtube.com/watch?v=Th_3AvK-EbM&t=359s
	https://www.raspberrypi.org/documentation/remote-access/ssh/

Acesso via ssh: ssh pi@endereco_ip


## 3. Cria pasta Projetos:

mkdir Projetos


## 4. Clona repositório no git

git clone https://github.com/mauriciolongato/costurApp-pi.git


## 5. Instalando postgres

https://opensource.com/article/17/10/set-postgres-database-your-raspberry-pi

Consfigurações do projeto:
	
 1. sudo su postgres
 2. createuser admin -P --interactive
 3. createdb controleproducao
 4. psql

## 6. Instalando dependencias e rodando controle_core	
	
 Dependencias
	alias python=python3
	alias pip=pip3
	pip install virtualenv
 
	Ambiente virtual
	python -m venv env
	pip install -r requirements.txt

	Rodando
	python manage.py makemigrations core
	python manage.py migrate
	python manage.py createsuperuser
		login: admin
		senha: admin12345

	python manage.py runserver 0:8000

	https://www.digitalocean.com/community/tutorials/how-to-install-and-manage-supervisor-on-ubuntu-and-debian-vps
	configurando serviço supervisor para o controle_core

## 7. Instalando dependencias e rodando pdf_render

	Dependencias
	a. wkhtmltopdf (retirado desse link: https://learnbatta.com/blog/django-html-to-pdf-using-pdfkit-and-wkhtmltopdf-5/)
		Instalações...
		sudo apt-get install wkhtmltopdf
		sudo apt-get install xvfb
		sudo mv /usr/bin/wkhtmltopdf /usr/bin/wkhtmltopdf_bin
		
		Cria pasta e arquivos de dependencia...
		mkdir /opt/wkhtmltopdf_conf
		sudo nano /opt/wkhtmltopdf_conf/wkhtmltopdf.sh
			#!/bin/bash
			xvfb-run -a --server-args="-screen 0, 1024x768x24" /usr/bin/wkhtmltopdf_bin -q $*

		sudo chmod +x /opt/wkhtmltopdf_conf/wkhtmltopdf.sh
		sudo ln -s /opt/wkhtmltopdf_conf/wkhtmltopdf.sh  /usr/bin/wkhtmltopdf

	Setup pdf_render
	mkdir static
	pip install -r requirements.txt


## 8. Start com a maquina

	1. Variaveis de ambiente
		echo "export DISPLAY=:0" >> ~/.bash_profile

	2. Criar os serviços no supervisord

		Cria o serviço para o costurapp_core	
		/etc/systemd/system/costurapp_core.service

	   	[Unit]
		Description=controle_core

	   	[Service]
		ExecStart=/home/pi/Projetos/costurApp/controle_core/launcher.sh

	   	[Install]
		WantedBy=multi-user.target

 		Cria o serviço para o pdf
		sudo nano /etc/systemd/system/costurapp_pdf.service
		
		[Unit]
		Description=pdf_render
  
  		[Service]
		ExecStart=/home/pi/Projetos/costurApp/pdf_render/launcher.sh

  		[Install]
		WantedBy=multi-user.target

## 9. Habilita os serviços
	sudo systemctl enable costurapp_core.service
	sudo systemctl enable costurapp_pdf.service
	sudo reboot

# Registrando as pistoladas

Exemplo da url: http://192.168.0.109:8000/tracking?pistola=Pistola_1&cod_barras=150&data_criacao=2019/03/30%2012:27:03.000

São 3 parametros: 
	- pistola
	- cod_barras
	- data_criacao
