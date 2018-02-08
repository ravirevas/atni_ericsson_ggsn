#!/usr/bin/env bash

cd $ATNI_REPO/ftp_scripts
sudo -u commnet python FTP_FileUtil_HistData_Processor.py zteumts_hist.properties

