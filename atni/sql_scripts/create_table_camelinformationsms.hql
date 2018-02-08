create table camelinformationsms (
	file_name string,
	cAMELCallingPartyNumber	string,
	cAMELDestinationSubscriberNumber	string,
	cAMELSMSCAddress	string,
	defaultSMSHandling	smallint,
	freeFormatData	string,
	sCFAddress	string,
	serviceKey	bigint,
	smsReferenceNumber	string
)
stored as parquet;