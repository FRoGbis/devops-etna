#!/bin/bash

if [ "`which node`" == "" ]
then
  echo "node not in PATH"
  exit 1
fi

if [ "`which npm`" == "" ]
then
  echo "npm not in path"
  exit 1
fi

if [ ! -f "mocks.js" ]
then
  echo "run this script from same dir as mocks.js"
  exit 1
fi

if [ "`npm list swagmock | grep empty`" != "" ]
then
  echo "Installing swagmock"
  npm install swagmock
fi

echo "Running mocks.js"
node mocks.js


exit 0
