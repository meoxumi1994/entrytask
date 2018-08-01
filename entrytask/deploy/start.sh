#!/usr/bin/env bash
sudo systemctl stop nginx
sudo systemctl stop uwsgi
sudo systemctl start uwsgi
sudo systemctl start nginx
sudo systemctl enable uwsgi
sudo systemctl enable nginx
echo

systemctl stop nginx
systemctl stop uwsgi
systemctl start uwsgi
systemctl start nginx
systemctl enable uwsgi
systemctl enable nginx
echo
