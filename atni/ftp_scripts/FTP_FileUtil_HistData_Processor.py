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



# Read the last file pull date from the corresponding lastFilePullDateStoreFile file.

lastFilePullDate_formatted = fileHelper.readValueFromFile(lastFilePullDateStoreFile)

# If the file does not exist or if there is not value initially,
# read the lastFilePullDate from the properties file.

if lastFilePullDate_formatted == None:
    lastFilePullDate_formatted = config.get('All','lastFilePullDate')

# Invoke the FTPFilePullUtil for each time slot derived based on the
#   lastFilePullDate,
#   noof_iterations,
#   finalFilePullDate

# The idea is to pull the files from FTP for a specific number of minutes in iterations.
# Each iteration would save the lastFilePullDate

while (int(finalFilePullDate) < int(lastFilePullDate_formatted)) & (noof_iterations > 0):

    lastFilePullDate_Dt = datetime.datetime.strptime(lastFilePullDate_formatted, '%Y%m%d%H%M%S')

    lastFilePullDate = (lastFilePullDate_Dt + datetime.timedelta(minutes=int(iterateByMinutes))).strftime("%Y%m%d%H%M%S")

    # Set the lastFilePullDate to finalFilePullDate if the lastFilePullDate is going beyond the intended finalFilePullDate

    if finalFilePullDate >= lastFilePullDate:
        lastFilePullDate = finalFilePullDate

    logging.info('--Started processing the files from : '+lastFilePullDate+' to '+ lastFilePullDate_formatted)

    print "currentFilePullDate: "+ lastFilePullDate
    print "lastFilePullDate: "+ lastFilePullDate_formatted

    ##    CALL THE FTP_PULLER

    call(["python","FTP_FileUtil_New1.py",sys.argv[1],lastFilePullDate_formatted,lastFilePullDate])

    fileHelper.overwriteValueToFile(lastFilePullDateStoreFile,lastFilePullDate)

    logging.info('--Finished processing the files from : '+lastFilePullDate+' to '+ lastFilePullDate_formatted)

    lastFilePullDate_formatted = lastFilePullDate

    noof_iterations = noof_iterations - 1




