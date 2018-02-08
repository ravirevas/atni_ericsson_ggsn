#!/usr/bin/env bash

sudo -u gtt hadoop fs -rm -r /etl/gtt/genband/staging/temp
sudo -u gtt hadoop fs -cp -f /etl/gtt/genband/staging/* /etl/gtt/genband/complete/
sudo -u gtt hadoop fs -rm -r /etl/gtt/genband/staging/*
sudo -u gtt hadoop fs -mkdir -p /etl/gtt/genband/staging/temp

