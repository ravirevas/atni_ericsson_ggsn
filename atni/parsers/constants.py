# DATASETS

LOG_BASE = "/opt/atni_repo/"
REPOSITORY_BASE = "/opt/atni_repo/"

AIRSPAN = "airspan"
GENBAND = "genband"
ERICSSON_SGSN = "ericsson_sgsn"
ZTEUMTS = "zteumts"

# HDFS Directories start

AIRSPAN_HDFS_BASE = "/etl/gtt/airspan/"
AIRSPAN_HDFS_STAGING = "/etl/gtt/airspan/staging/"
AIRSPAN_HDFS_COMPLETE = "/etl/gtt/airspan/complete"
AIRSPAN_HDFS_FAILED = "/etl/gtt/airspan/failed"
AIRSPAN_HDFS_DUPLICATE = "/etl/gtt/airspan/duplicate"

GENBAND_HDFS_BASE = "/etl/gtt/genband/"
GENBAND_HDFS_STAGING = "/etl/gtt/genband/staging/temp/"
GENBAND_HDFS_COMPLETE = "/etl/gtt/genband/complete"
GENBAND_HDFS_FAILED = "/etl/gtt/genband/failed"
GENBAND_HDFS_DUPLICATE = "/etl/gtt/genband/duplicate"


GENBAND_HDFS_HIST_BASE = "/etl/gtt/genband/hist"
GENBAND_HDFS_HIST_STAGING = "/etl/gtt/genband/hist/staging/temp/"
GENBAND_HDFS_HIST_COMPLETE = "/etl/gtt/genband/hist/complete"
GENBAND_HDFS_HIST_FAILED = "/etl/gtt/genband/hist/failed"


ERICSSON_SGSN_HDFS_BASE = "/etl/gtt/ericsson_sgsn/"
ERICSSON_SGSN_HDFS_STAGING = "/etl/gtt/ericsson_sgsn/staging/temp/"
ERICSSON_SGSN_HDFS_COMPLETE = "/etl/gtt/ericsson_sgsn/complete"
ERICSSON_SGSN_HDFS_FAILED = "/etl/gtt/ericsson_sgsn/failed"
ERICSSON_SGSN_HDFS_DUPLICATE = "/etl/gtt/ericsson_sgsn/duplicate"


ZTEUMTS_HDFS_BASE = "/etl/commnet/zteumts/"
ZTEUMTS_HDFS_STAGING = "/etl/commnet/zteumts/staging/temp/"
ZTEUMTS_HDFS_COMPLETE = "/etl/commnet/zteumts/complete"
ZTEUMTS_HDFS_FAILED = "/etl/commnet/zteumts/failed"
ZTEUMTS_HDFS_DUPLICATE = "/etl/commnet/zteumts/duplicate"


# HDFS Directories end

# Log Directories start

AIRSPAN_LOG = LOG_BASE + "ftp_process/logs/airspan/"
GENBAND_LOG = LOG_BASE + "ftp_process/logs/genband/"
ERICSSON_SGSN_LOG = LOG_BASE + "ftp_process/logs/ericsson_sgsn/"
ZTEUMTS_LOG = LOG_BASE + "ftp_process/logs/zteumts/"

# Log Directories end

# ######  SPARK CONSTANTS ##########


# ###################### AIRSPAN CONSTANTS ######################

#AIRSPAN_IN_PATH = "/Users/ram/Projects/ATNi/atni_repository/atni/data/airspan/in/accountP_22_5_16#12_12_15.dat.gz"
AIRSPAN_IN_PATH = AIRSPAN_HDFS_STAGING
AIRSPAN_OUT_PATH = ""
AIRSPAN_TABLE_NAME = "gtt.airspan_cdr"
AIRSPAN_STATS_TABLE_NAME = "gtt.airspan_stats"

# ###################### GENBAND CONSTANTS ######################

GENBAND_IN_PATH = GENBAND_HDFS_STAGING
GENBAND_OUT_PATH = ""
GENBAND_TABLE_NAME = "gtt.genband_cdr"
GENBAND_STATS_TABLE_NAME = "gtt.genband_parser_stats"

# ###################### ERICSSON CONSTANTS ######################

#ERICSSON_IN_PATH = "/Users/ram/Projects/ATNi/atni_repository/atni/data/ericsson/in/2016182chsLog_261_00_20160701_0018.gz"
ERICSSON_IN_PATH = ERICSSON_SGSN_HDFS_STAGING
ERICSSON_OUT_PATH = ""
ERICSSON_FILE_CHUNK_SIZE = 10000

ERICSSON_PDP_TABLE_NAME = "gtt.sgsnpdprecord"
ERICSSON_PDP_TRAFFIC_VOLUME_TABLE = "gtt.trafficvolumes"
ERICSSON_PDP_CAMEL_INFO_PDP_TABLE = "gtt.camelinformationpdp"
ERICSSON_PDP_RECORD_EXTENSIONS_TABLE = "gtt.recordextensions"

ERICSSON_SMO_TABLE_NAME = "gtt.sgsnsmorecord"
ERICSSON_SMO_CAMEL_SMS_TABLE = "gtt.camelinformationsms"

ERICSSON_SMT_TABLE_NAME = "gtt.sgsnmtrecord"
ERICSSON_STATS_TABLE_NAME = "gtt.ericsson_sgsn_stats"
####################### ZTEUMTS-ASN1 CONSTANTS ######################

#ZTEUMTS_IN_PATH = "/tmp/parsers/atni/parsers/zteumts_asn1/B2016061536247.dat.gz"
ZTEUMTS_IN_PATH = ZTEUMTS_HDFS_STAGING
ZTEUMTS_OUT_PATH = ""
# The chunk size is fixed and cannot be varied. This is as per the structure of umts record
ZTEUMTS_FILE_CHUNK_SIZE = 2048
ZTEUMTS_OUTGATEWAY_TABLE_NAME = "commnet.outgatewayrecord"
ZTEUMTS_COMMONEQUIP_TABLE_NAME = "commnet.commonequipmentrecord"
ZTEUMTS_MOCALL_TABLE_NAME = "commnet.mocallrecord"
ZTEUMTS_USSD_TABLE_NAME = "commnet.ussdrecord"
ZTEUMTS_MTLCS_TABLE_NAME = "commnet.mtlcsrecord"
ZTEUMTS_INCGATEWAY_TABLE_NAME = "commnet.incgatewayrecord"
ZTEUMTS_SSACTION_TABLE_NAME = "commnet.ssactionrecord"
ZTEUMTS_MOSMS_TABLE_NAME = "commnet.mosmsrecord"
ZTEUMTS_MTSMS_TABLE_NAME = "commnet.mtsmsrecord"
ZTEUMTS_MTCALL_TABLE_NAME = "commnet.mtcallrecord"
ZTEUMTS_MCFCALL_TABLE_NAME = "commnet.mcfcallrecord"
ZTEUMTS_GSICPH_TABLE_NAME = "commnet.gsicphrecord"
ZTEUMTS_HLRINT_TABLE_NAME = "commnet.hlrintrecord"
ZTEUMTS_MOLCS_TABLE_NAME = "commnet.molcsrecord"
ZTEUMTS_MTRF_TABLE_NAME = "commnet.mtrfrecord"
ZTEUMTS_NCSCPH_TABLE_NAME = "commnet.ncscphrecord"
ZTEUMTS_NILCS_TABLE_NAME = "commnet.nilcsrecord"
ZTEUMTS_VIG_TABLE_NAME = "commnet.vigrecord"
ZTEUMTS_MCFCPH_TABLE_NAME = "commnet.mcfcphrecord"
ZTEUMTS_TCICPH_TABLE_NAME = "commnet.tcicphrecord"
ZTEUMTS_MSCSRVCC_TABLE_NAME = "commnet.mscsrvccrecord"
ZTEUMTS_ROAM_TABLE_NAME = "commnet.roamrecord"
ZTEUMTS_MOCPH_TABLE_NAME = "commnet.mocphrecord"
ZTEUMTS_MOECALL_TABLE_NAME = "commnet.moecallrecord"
ZTEUMTS_TERMCAMELINT_TABLE_NAME = "commnet.termcamelintrecord"
ZTEUMTS_STATS_TABLE_NAME = "commnet.zteumts_stats"
# ###################### Common configuration ######################

WRITE_FORMAT = "parquet"
WRITE_MODE = "append"

IMPALA_DAEMON = "172.19.100.103"
IMPALA_PORT = "21050"


