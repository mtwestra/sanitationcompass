#!/bin/bash

sudo pip3 install virtualenv
# when run on a mac, you need --python=python3.6
virtualenv -p virtualenv --python=/usr/bin/python3.6 venv
source venv/bin/activate

pip3 install Django
pip3 install Pillow
pip3 install Pygments
pip3 install docutils
pip3 install markdown2
pip3 install pdfrw
pip3 install PyPDF2
pip3 install reportlab
pip3 install rst2pdf
pip3 install dj-database-url
pip3 install gunicorn
pip3 install mysql-connector
pip3 install uwsgi
