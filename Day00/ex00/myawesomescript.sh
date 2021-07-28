#!/bin/sh

curl --silent $1 2>&1 | grep 'a href' | cut -d '"' -f 2
