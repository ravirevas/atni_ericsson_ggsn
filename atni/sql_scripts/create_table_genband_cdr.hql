create table genband_cdr (
	file_id bigint,
	connect_datetime timestamp,
	originating_number string,
	terminating_number string,
	elapsed_time decimal(12,2),
	dom_int_indicator string,
	trunkid1 string,
	trunkid2 string,
	call_code string,
	completion_ind string,
	answer_ind string,
	is_duplicate smallint
)
partitioned by (timeframe bigint)
stored as parquet;
