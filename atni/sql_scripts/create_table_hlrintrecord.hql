

create table hlrintrecord (
	basicservice string,
	callingnumberbeforesdc string,
	dcinterrogatedoricallednumber string,
	exchangeidentity string,
	filename string,
	hotbillingtag2 bigint,
	interrogationresult string,
	interrogationtime timestamp,
	numberofforwarding bigint,
	operatorid bigint,
	oricallednumberbeforesdc string,
	recordsequencenumber string,
	recordtype bigint,
	recordingentity string,
	routingnumber string,
	sdcinterrogatedcallingnumber string,
	sdcinterrogationflag string,
	servedimsi string,
	servedmsisdn string
)
stored as parquet;