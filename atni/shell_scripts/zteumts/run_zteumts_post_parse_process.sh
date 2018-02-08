#!/usr/bin/env bash

sudo -u commnet hadoop fs -rm -r /etl/commnet/zteumts/staging/temp
sudo -u commnet hadoop fs -cp -f /etl/commnet/zteumts/staging/* /etl/commnet/zteumts/complete/
sudo -u commnet hadoop fs -rm -r /etl/commnet/zteumts/staging/*
sudo -u commnet hadoop fs -mkdir -p /etl/commnet/zteumts/staging/temp



