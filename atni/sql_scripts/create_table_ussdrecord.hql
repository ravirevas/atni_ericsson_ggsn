

create table ussdrecord (
	callreference string,
	endtime timestamp,
	errorcode string,
	exchangeidentity string,
	filename string,
	hotbillingtag bigint,
	hotbillingtag2 bigint,
	locationcellid string,
	locationlac string,
	locationplmn string,
	locationsac string,
	msclassmark string,
	operatorid bigint,
	recordsequencenumber string,
	recordtype bigint,
	recordingentity string,
	servedimei string,
	servedimsi string,
	servedmsisdn string,
	starttime timestamp,
	systemtype string,
	ussddatacodingscheme string,
	ussdinteractioncount bigint,
	ussdoperationcode string,
	ussdservicecode bigint,
	ussdunstructureddata string
)
stored as parquet;