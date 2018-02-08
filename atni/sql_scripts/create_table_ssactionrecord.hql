

create table ssactionrecord (
	callreference string,
	exchangeidentity string,
	filename string,
	forwardedsubnumber string,
	globalcallreference string,
	hotbillingtag2 bigint,
	locationcellid string,
	locationlac string,
	locationplmn string,
	locationsac string,
	msclassmark string,
	mscspc14 string,
	mscspc24 string,
	noreplycondtime bigint,
	operatorid bigint,
	recordsequencenumber string,
	recordtype bigint,
	recordingentity string,
	servedimei string,
	servedimsi string,
	servedmsisdn string,
	ssaction string,
	ssactionresult string,
	ssactiontime timestamp,
	ssparameters string,
	supplservice string,
	systemtype string,
	transactionidentification string
)
stored as parquet;