#!/usr/bin/env bash

nohup airflow webserver $* > /opt/airflow/logs/webserver.logs &

nohup airflow worker $* > /opt/airflow/logs/celery.logs &

nohup airflow scheduler > /opt/airflow/logs/scheduler.logs &
