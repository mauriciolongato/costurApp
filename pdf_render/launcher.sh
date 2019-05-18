#!/bin/bash
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd home/pi/Projetos/costurApp/pdf_render
xvfb-run wkhtmltopdf
python3 app.py 0:5000
