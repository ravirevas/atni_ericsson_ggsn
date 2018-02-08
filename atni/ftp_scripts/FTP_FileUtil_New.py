import sys
sys.path.append("./pytz-2016.6.1")
import datetime
import os
import logging
import ftpUtil
import FileHelper
import pytz
import string
from subprocess import call
from dateutil.tz import tzlocal

import ConfigParser
config = ConfigParser.RawConfigParser()
config.read(sys.argv[1])


# Dataset config:

# Get the local datetime. This would be the time till which the files will be pulled from FTP for the current run.

#current_date = datetime.datetime.now()

# ASSIGNING CURRENTDATE FROM PARAM2
current_date = datetime.datetime.strptime(sys.argv[2], '%Y%m%d%H%M%S')
lastFilePullDate = sys.argv[3]

current_datetime_formatted = current_date.strftime("%Y%m%d%H%M%S")
# Determine the current File Pull Datetime. Make it 1 minute less than the current time stamp to avoid issues due to seconds mismatch.

#currentFilePullDate = (current_date - datetime.timedelta(minutes=1)).strftime("%Y%m%d%H%M%S")
currentFilePullDate = current_datetime_formatted

#   Pull the last processed date too.



logging.info('--Started processing the FTP files from : '+lastFilePullDate+' to '+ currentFilePullDate)

print('--Started processing the FTP files from : '+lastFilePullDate+' to '+ currentFilePullDate)

