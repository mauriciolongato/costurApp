#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home


cd /
cd home/pi/Projetos/costurApp/controle_core
python3 manage.py runserver 0:8000
cd /
