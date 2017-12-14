#!/bin/bash

apt-get update
apt-get install -y python3 python3-pip
pip3 install -r /devops/services/$1/requirements.txt
cd /devops/services/$1
nameko run $1 --broker amqp://guest:guest@rabbitmq
