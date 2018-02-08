#! /bin/bash
# Shutdown Script for Celery Daemons

echo "Shutting Down Celery"

#kills the process running on port 8793
for PID in `lsof -i:8793`;do kill -9 $PID ; done

#kills the remainder celeryd daemons
for pid in `ps -ef | grep "celeryd" | awk '{print $2}'` ; do kill -9 $pid ; done

#Kill the Airflow flower parent process
for pid in `ps -ef | grep "airflow flower" | awk '{print $2}'` ; do kill -9 $pid ; done
