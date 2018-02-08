__author__ = 'vijaydatla'
import sys
sys.path.append("./pytz-2016.6.1")
import datetime
import logging
import FileHelper
from subprocess import call
import ConfigParser
config = ConfigParser.RawConfigParser()

# Read the properties file from the first argument.
# The properties file contains all the configuration required for the FTP FileUtil to work.

config.read(sys.argv[1])

# All the required properties to derive the start and end dates of the Incremental file fetching are loaded below.
# More description about the properties can be found in the documentation or the properties template

dataset=config.get('All','dataset')
fileHelper=FileHelper.FileHelper()
ftp_process_base_dir=config.get('All','ftp_process_base_dir')
iterateByMinutes = config.get('All','iterateByMinutes')
lastFilePullDate = config.get('All','lastFilePullDate')
finalFilePullDate = config.get('All','finalFilePullDate')
noof_iterations = int(config.get('All','noof_iterations'))
lastFilePullDateStoreFile=ftp_process_base_dir+'/'+dataset+'_'+config.get('All','lastFilePullDateStoreFile')

# Creating the file that stores the last File Pull Date if it does not exist.

call(["touch",lastFilePullDateStoreFile])
call(["chmod","777", lastFilePullDateStoreFile])

fileHelper=FileHelper.FileHelper()


current_date = datetime.datetime.now()


# Determining the current file pull date for incremental load.
# Basically the current file pull date would be
#   either the current datetime (-1 minutes)
#   or the finalFilePullDate

currentFilePullDate = None
currentFilePullDate_tmp = (current_date - datetime.timedelta(minutes=1)).strftime("%Y%m%d%H%M%S")

if finalFilePullDate <= currentFilePullDate_tmp:
    currentFilePullDate=finalFilePullDate
else:
    currentFilePullDate=currentFilePullDate_tmp


# Read the last file pull date from the corresponding lastFilePullDateStoreFile file.

lastFilePullDate_formatted = fileHelper.readValueFromFile(lastFilePullDateStoreFile)

# If the file does not exist or if there is not value initially,
# read the lastFilePullDate from the properties file.

if lastFilePullDate_formatted == None:
    lastFilePullDate_formatted = config.get('All','lastFilePullDate')

# Invoke the FTPFilePullUtil for each time slot derived based on the
#   lastFilePullDate,
#   noof_iterations,
#   currentFilePullDate

# The idea is to pull the files from FTP for a specific number of minutes in iterations.
# Each iteration would save the lastFilePullDate

while (int(currentFilePullDate) > int(lastFilePullDate_formatted)) & (noof_iterations > 0):

    lastFilePullDate_Dt = datetime.datetime.strptime(lastFilePullDate_formatted, '%Y%m%d%H%M%S')

    lastFilePullDate = (lastFilePullDate_Dt + datetime.timedelta(minutes=int(iterateByMinutes))).strftime("%Y%m%d%H%M%S")

    # Set the lastFilePullDate to currentFilePullDate if the lastFilePullDate is going beyond the intended currentFilePullDate

    if currentFilePullDate <= lastFilePullDate:
        lastFilePullDate = currentFilePullDate

    logging.info('--Started processing the files from : '+lastFilePullDate+' to '+ currentFilePullDate)

    print "currentFilePullDate: "+ lastFilePullDate
    print "lastFilePullDate: "+ lastFilePullDate_formatted

    ##    CALL THE FTP_PULLER

    call(["python","FTP_FileUtil_New1.py",sys.argv[1],lastFilePullDate,lastFilePullDate_formatted])

    fileHelper.overwriteValueToFile(lastFilePullDateStoreFile,lastFilePullDate)

    logging.info('--Finished processing the files from : '+lastFilePullDate+' to '+ currentFilePullDate)

    lastFilePullDate_formatted = lastFilePullDate

    noof_iterations = noof_iterations - 1






