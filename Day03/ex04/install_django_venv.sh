#!/bin/sh

# echo $$		# PID
# echo $0		#
# echo $SHELL # 로그인쉘

python3 -m venv 'django_env';
source django_env/bin/activate;
pip3 install --upgrade pip;
pip3 install -r requirement.txt;
