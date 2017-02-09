#!/usr/bin/env bash

sudo rm -rf /etc/nginx/sites-enabled/
sudo ln -sf nginx.conf  /etc/nginx/sites-enabled/default
sudo nginx -t
sudo /etc/init.d/nginx restart