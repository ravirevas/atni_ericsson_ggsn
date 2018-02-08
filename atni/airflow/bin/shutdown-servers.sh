#! /bin/bash
# Restart Script for Airflow webserver

BIN_DIR=$(dirname "$0")

sh ${BIN_DIR}/shutdown-webserver.sh

sh ${BIN_DIR}/shutdown-scheduler.sh

sh ${BIN_DIR}/shutdown-celery.sh
