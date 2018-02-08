create table sgsnsmorecord (
	file_name string,
	cAMELInformationSMSKey	string,
	cellIdentifier	string,
	chargingCharacteristics	string,
	chChSelectionMode	string,
	destinationNumber	string,
	eventTimeStamp	timestamp,
	localSequenceNumber	bigint,
	locationArea	string,
	messageReference	string,
	msNetworkCapability	string,
	nodeID	string,
	pLMNIdentifier	string,
	rATType	bigint,
	recordingEntity	string,
	recordType	bigint,
	routingArea	string,
	servedIMEI	string,
	servedIMSI	string,
	servedMSISDN	string,
	serviceCentre	string,
	smsResult	bigint
)
partitioned by (timeframe_day bigint,
timeframe_hr int)
stored as parquet;