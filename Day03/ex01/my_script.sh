#!/bin/sh

if [ -e local_lib ];then
	rm -rf local_lib;
	python3 -m pip install -v --exists-action=w git+https://github.com/jaraco/path --target='./local_lib' --log='./local_lib/path.log';
else
	python3 -m pip install -v --exists-action=w git+https://github.com/jaraco/path --target='./local_lib' --log='./local_lib/path.log';
fi
