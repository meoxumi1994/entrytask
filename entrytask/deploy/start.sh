#!/usr/bin/env bash
sudo systemctl stop nginx
sudo systemctl stop uwsgi
sudo systemctl start uwsgi
sudo systemctl start nginx
sudo systemctl enable uwsgi
sudo systemctl enable nginx
echo
