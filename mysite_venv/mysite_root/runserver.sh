#! bin/zsh

redis-server
daphne -b 0.0.0.0 -p 8443 mysite.asgi:application
gunicorn --bind 127.0.0.1:8000 --workers 9 mysite.wsgi:application --daemon --reload --log-file ../log/gunicorn/log
sudo nginx
