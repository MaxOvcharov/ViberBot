#!/usr/bin/env bash

sudo rm -rf /etc/nginx/sites-enabled/*
sudo chmod 777 nginx.conf
sudo cp nginx.conf /etc/nginx/sites-enabled/nginx.conf
sudo nginx -t
sudo /etc/init.d/nginx restart

sudo cp gunicorn.conf /etc/supervisor/conf.d/
sudo supervisord -c /etc/supervisor/supervisord.conf

