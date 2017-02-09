#!/usr/bin/env bash

sudo rm -rf /etc/nginx/sites-enabled/*
sudo chmod 777 nginx.conf
sudo cp nginx.conf /etc/nginx/sites-enabled/ginx.conf
sudo nginx -t
sudo /etc/init.d/nginx restart
sudo supervisorctl reread
sudo supervisorctl update

