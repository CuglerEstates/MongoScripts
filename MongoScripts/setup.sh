#!/bin/bash


# Installing mongoDB 3.6

apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.6 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.6.list
apt-get update
apt-get install -y --allow-unauthenticated mongodb-org
service mongod start


# installing python3 virtualenv

apt-get install python3-venv -y
# python3 -m venv ~/venv
# source ~/venv/bin/activate
