#! /bin/bash
# Shutdown Script for Airflow 

echo "Shutting Down Web Server"

#Kill the Airflow webserver parent process
for pid in `ps -ef | grep "airflow-webserver" | awk '{print $2}'` ; do kill -9 $pid ; done

#Kill the Airflow webserver gunicor processes
for pid in `ps -ef | grep "airflow.www.app" | awk '{print $2}'` ; do kill -9 $pid ; done
