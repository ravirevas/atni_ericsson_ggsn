create table sgsnmtrecord (
	file_name string,
	cellIdentifier	string,
	cellIdentifierLastSM	string,
	chargingCharacteristics	string,
	chChSelectionMode string,
	eventTimeStamp	timestamp,
	localSequenceNumber	bigint,
	locationArea	string,
	locationAreaLastSM	string,
	msNetworkCapability	string,
	nodeID	string,
	numberOfSM	bigint,
	pLMNIdentifier	string,
	pLMNIdentifierLastSM	string,
	rATType	bigint,
	recordingEntity	string,
	recordType	bigint,
	routingArea	string,
	routingAreaLastSM	string,
	servedIMEI	string,
	servedIMSI	string,
	servedMSISDN	string,
	serviceCentre	string,
	smsResult	bigint
)
partitioned by (timeframe_day bigint,
timeframe_hr int)
stored as parquet;