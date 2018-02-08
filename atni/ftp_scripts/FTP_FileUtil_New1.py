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

# All the required properties to drive the file pulling logic based on teh start and end dates are loaded below.
# More description about the properties can be found in the documentation or the properties template



dataset=config.get('All','dataset')
ftp_server_base_dir=config.get('All','ftp_server_base_dir')
fileHelper=FileHelper.FileHelper()
ftp_process_base_dir=config.get('All','ftp_process_base_dir')
staging_local_path = config.get('All','staging_local_path')
staging_hdfs_path = config.get('All','staging_hdfs_path')
unzipToTempDirOnHDFS =  config.get('All','unzipToTempDirOnHDFS')

# FTP connect details:

ftp_server=config.get('All','ftp_server')
username=config.get('All','ftp_username')
password=config.get('All','ftp_password')
lastFilePullDateStoreFile=ftp_process_base_dir+'/'+dataset+'_'+config.get('All','lastFilePullDateStoreFile')

# This would be the start date for the file pull from FTP server.

current_date = datetime.datetime.strptime(sys.argv[2], '%Y%m%d%H%M%S')
current_datetime_formatted = current_date.strftime("%Y%m%d%H%M%S")
currentFilePullDate = current_datetime_formatted

current_day = current_date.strftime("%Y%m%d")
print "current_date : " + current_datetime_formatted

# Create logs directory for the current dataset

log_dir=ftp_process_base_dir+'/logs/'+dataset+current_day
call(["mkdir","-p",log_dir])
log_filename=log_dir+'/'+dataset+'_'+current_datetime_formatted+'.log'
logging.basicConfig(filename=log_filename, level=logging.INFO)



#  end date time for the file pull from FTP..

lastFilePullDate = sys.argv[3]

# Connect to FTP Server

ftpUtilObj=ftpUtil.FtpUtil()

logging.info('$$  --Connecting to the FTP Server--   $$')

ftp=ftpUtilObj.ftpConn(ftp_server, username, password)


logging.info('--Started processing the files from : '+lastFilePullDate+' to '+ currentFilePullDate)

# Identify the FTP directories from where the files should be pulled.
# The logic is tied to the FTP directory structure of the ATNi.

daysToLookBack = int(config.get('All','daysToLookBack'))
ftp_server_base_dirs=[]
date=current_date
while daysToLookBack >= 0 :
    date= (current_date - datetime.timedelta(days=daysToLookBack))
    dir = ftp_server_base_dir+'/'+date.strftime("%Y")+'/'+date.strftime("%m")+'/'+date.strftime("%d")
    ftp_server_base_dirs.append(dir)
    daysToLookBack=daysToLookBack-1


# Variables to hold the counts of total files, successful files and failed files.

total_files_ftp=0
passed_files_ftp=0
failed_files_ftp=0

# Variables to hold successful file names and failed file names.

failed_files=[]
successful_files=[]

# Iterate over each directory on FTP and identify the new files based on current File pull date and old file pull date.
# Pull the new once and load them into HDFS.

for cur_ftp_server_base_dir in ftp_server_base_dirs:

    logging.info('------- Now looking into '+cur_ftp_server_base_dir+'..')

    try:
        ftp.cwd(cur_ftp_server_base_dir)
    except Exception:
        print('Could not process directory.. '+cur_ftp_server_base_dir+'  . Continuing with the rest..')
        pass

    fileList = []
    dirContent = []

    # get contents of dir

    ftp.dir(dirContent.append)
    for line in dirContent:
        try:
            lineArr=line.split()
            fileModDate=ftp.sendcmd('MDTM '+lineArr[8])
            fileModDateFormatted=fileModDate.split()[1]
            origdate = datetime.datetime.strptime(fileModDateFormatted, '%Y%m%d%H%M%S')
            origdateLocal=origdate.replace(tzinfo=pytz.utc).astimezone(tzlocal())
            fileDate = origdateLocal.strftime('%Y%m%d%H%M%S')
            if lineArr[0][0]<>'d' and fileDate <= currentFilePullDate and fileDate > lastFilePullDate :
                fileList.append(fileDate[0:8] + ' ' +lineArr[8])
        except:
            failed_files.append('FTP_File_Fetch_Failed => '+line)

    # Iterate over each new file

    for file in fileList:
        total_files_ftp += 1
        dirPath=file.split()[0]
        filename=file.split()[1]
        try:

            # Changing the char # to - as # is not accepted by HDFS commands.
            localFileName = string.replace(filename, '#', '-')

            # creating the directory path if none exists already. The idea is to ensure that the user does not have
            # to create any directories before running the code.
            call(["mkdir","-p",ftp_process_base_dir+'/'+staging_local_path+'/'+dirPath])
            call(["chmod","-R", "777", ftp_process_base_dir+'/'+staging_local_path+'/'+dirPath])

            localFilePath = ftp_process_base_dir+'/'+staging_local_path+'/'+dirPath+'/' + localFileName
            logging.info('----------------Attempting to pull the file :" ' + filename + ' " from FTP to local staging directory : " '+ftp_process_base_dir+'/'+staging_local_path+'/'+dirPath+' "')
            fhandle = open(localFilePath, 'wb')
            ftp.retrbinary('RETR ' + filename, fhandle.write)
            fhandle.close()
            logging.info('-----------------Finished pulling the file :" ' + filename + ' " from FTP to local staging directory : " '+ftp_process_base_dir+'/'+staging_local_path+'/'+dirPath+' "')

            # copying the file to HDFS as is.

            call(["hadoop","fs", "-mkdir", "-p" ,  staging_hdfs_path+'/'+dirPath])

            logging.info('----------------Attempting to push the file :" ' + filename + ' " to HDFS location : "' +  staging_hdfs_path+'/'+dirPath )
            hdfs_file_path=staging_hdfs_path+'/'+dirPath+'/'+localFileName
            call(["hadoop", "fs", "-copyFromLocal",  "-f", localFilePath, hdfs_file_path])

            # Unzip the files to a temp diretory if required..   Some data sets are zipped and the data processing
            # applications that read files from HDFS are not capable of processing the files in zipped format.
            # Hence, an unzipped version of the file can be stored in a temp dir if required.

            if unzipToTempDirOnHDFS == 'Y':
                call(["hadoop","fs", "-mkdir", "-p" ,  staging_hdfs_path+'/temp/'])
                unzippedFilePath=localFilePath[0:-3]
                call(["rm","-f",unzippedFilePath])
                call(["gzip","-d",localFilePath])
                call(["hadoop", "fs", "-copyFromLocal",  "-f",unzippedFilePath,  staging_hdfs_path+'/temp/'])
                passed_files_ftp += 1

            logging.info('-----------------Finished pushing the file :" ' + filename + ' " to HDFS location : "' +  staging_hdfs_path+'/'+dirPath)

            successful_files.append(dirPath+'/'+filename)
        except:
            logging.info('------------xxxxxxxx  FAILED to process (either pull from FTP or push to HDFS ) the file : " ' + filename+' "' )
            failed_files_ftp += 1
            failed_files.append(dirPath+'/'+ filename)

#  Write successul and failed files into into DATASET/{lastprocessedDateTime}-{currentprocessedDateTime}

call(["mkdir","-p",ftp_process_base_dir+'/'+dataset+'_processed'])
call(["chmod","-R","777", ftp_process_base_dir+'/'+dataset+'_processed'])

# store the successful and failed files list to disk.

if len(successful_files)>0:

    for successful_file in successful_files:
        fileHelper.writeValueToFile(ftp_process_base_dir+'/'+dataset+'_processed/'+lastFilePullDate+'_'+currentFilePullDate+'succ.txt',successful_file)

for failed_file in failed_files:
    fileHelper.writeValueToFile(ftp_process_base_dir+'/'+dataset+'_processed/'+lastFilePullDate+'_'+currentFilePullDate+'failed.txt',failed_file)


