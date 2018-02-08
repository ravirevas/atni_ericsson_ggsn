#!/usr/bin/env bash

cd $ATNI_REPO/ftp_scripts
sudo -u gtt python FTP_FileUtil_HistData_Processor.py ericsson_sgsn_hist.properties

