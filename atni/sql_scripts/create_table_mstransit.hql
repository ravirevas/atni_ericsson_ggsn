create table mstransit (
CallDuration bigint,
CalledNumber string,
CalledTONNPI string,
CallingNumber string,
CallingTONNPI string,
CallReference string,
CauseForTermination string,
ChargedParty bigint,
DateForStartofcharge timestamp,
Diagnostics bigint,
ExchangeIdentity string,
GSMISDNBasicService string,
Id bigint,
IncomingCic string,
IncomingTKGP string,
IncomingTKGPName string,
LastPartialOutput bigint,
MSCIdentification string,
MSCIdenTONNPI string,
MscSpc14 string,
MscSpc24 string,
OutgoingCic string,
OutgoingTKGP string,
OutgoingTKGPName string,
PartialOutputRecNum bigint,
RecordExtensions string,
RecordOffset bigint,
RecordType bigint,
RedirectingNumber string,
RedirectingTONNPI string,
RoamingNumber string,
RoamingTONNPI string,
SequenceNumber string,
TimeForAnswer timestamp,
TimeForRelease timestamp,
TimeForSeizeChannel timestamp
)
stored as parquet;