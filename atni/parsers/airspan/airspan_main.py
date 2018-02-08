import sys
import os


from pyspark import SparkConf, SparkContext, HiveContext
from pyspark.sql.types import *
from atni.parsers.constants import *
from atni.parsers.utilities import *
from airspan_schema.airspan import *

import subprocess
import logging
import uuid


print logging.INFO

def main(argv=None):
    os.environ["SPARK_HOME"]='/usr/lib/spark'

    # logging.basicConfig(filename=get_logging_file_name("parse", AIRSPAN_LOG, AIRSPAN), level=logging.INFO)

#    input_path = AIRSPAN_IN_PATH
    input_path = 'C:\\Users\\Ravi\\Desktop\\sample.dat'
    
    print input_path

    sc = get_spark_context("airspan_spark_job")
    
    
    sqlContext = get_sql_context(sc)

    # Custom schema to read input

    hdfs_airspan_paths = input_path


    iteration_id = get_current_time_and_day()
    airspan_stats = []

    for path in hdfs_airspan_paths:

        # Read the input file,split with a delimiter and extract input fields
        total_count = 0
        success_count = 0
        fail_count = 0

        calls = sc.textFile(path)
        file_name = get_file_name(path)

        print "############file_path is:" + path
        print "############file_name is:" + file_name
        
        check_sum = get_file_check_sum(str(path))
        #check_sum = 123445678
        calls_parts = calls.map(lambda l: l.split(";"))

        total_count = calls_parts.count()
        calls_parsed = calls_parts.map(lambda p: (file_name, long(p[1]), append_timezone_offset(convert_calltime_to_timestamp(p[4])), p[9], p[10], int(p[11]), int(p[12]), p[13], int(p[15]),
                                                  int(p[16]), p[19], p[20], p[22], int(p[40]), p[56], int(p[57]), long(append_timezone_offset(convert_calltime_to_timestamp(p[4])).strftime("%Y%m%d")), long(append_timezone_offset(convert_calltime_to_timestamp(p[4])).strftime("%H"))))

        success_count = calls_parsed.count()
        print "##################$$$$$$$$ Parsing complete. Fetching stats now ##########$$$$$$$$$$$$:" + str(success_count)
        stats = [[str(iteration_id) ,str(uuid.uuid4()), file_name, check_sum , total_count, success_count,
                 fail_count, get_current_time_day(), get_current_time()]]
        

        print stats

       
       

if __name__ == "__main__":
    sys.exit(main())
