#!/bin/sh

if [ $# -ne 2 ]
then
  echo "Invalid number of argument"
  exit 1
fi

if [ ! -d "$1" ]
then
  echo "$1 does not exists"
  exit 1
fi

if [ ! -f "$1/$2" ]
then
  echo "$1/$2 does not exists"
  exit 1
fi

apt-get update
apt-get install -y python3 python3-pip

cd $1
pip3 install -r requirements.txt
python3 $2

exit 0
