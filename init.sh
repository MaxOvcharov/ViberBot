#!/usr/bin/env bash

sudo rm -rf /etc/nginx/sites-enabled/*
sudo chmod 777 nginx.conf
sudo cp nginx.conf /etc/nginx/sites-enabled/ginx.conf
sudo nginx -t
sudo /etc/init.d/nginx restart
sudo cp gunicorn.conf /etc/supervisor/conf.d/ViberBot.conf
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start ViberBot
