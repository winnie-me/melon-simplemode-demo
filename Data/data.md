
CREATE TABLE hadoop_kent.melon_ods_stat_production.o_fanon_log_ro (
   "_hoodie_commit_time" varchar,
   "_hoodie_commit_seqno" varchar,
   "_hoodie_record_key" varchar,
   "_hoodie_partition_path" varchar,
   "_hoodie_file_name" varchar,
   "act_date" timestamp,
   "member_key" bigint,
   "artist_id" bigint,
   "fanon_staus_code" varchar,
   "menu_id" bigint,
   "poc_code" varchar,
   "_metadata" row("sequence" bigint, "timestamp" timestamp, "operation" varchar, "partition" integer),
   "_hoodie_is_deleted" boolean,
   "log_date" varchar,
   "log_hour" varchar
)
WITH (
   external_location = 'hdfs://hadoop-kent/melon_ods_stat/production/raw/kafka/ods_stat/o_fanon_log/data',
   format = 'PARQUET',
   partitioned_by = ARRAY['log_date','log_hour']
)

---

CREATE TABLE hadoop_kent.melon_ods_stat_production.o_act_log_like_ro (
   "_hoodie_commit_time" varchar,
   "_hoodie_commit_seqno" varchar,
   "_hoodie_record_key" varchar,
   "_hoodie_partition_path" varchar,
   "_hoodie_file_name" varchar,
   "act_date" timestamp,
   "member_key" bigint,
   "conts_type_code" varchar,
   "conts_id" bigint,
   "like_yn" varchar,
   "menu_id" bigint,
   "poc_code" varchar,
   "first_like_yn" varchar,
   "_metadata" row("sequence" bigint, "timestamp" timestamp, "operation" varchar, "partition" integer),
   "_hoodie_is_deleted" boolean,
   "log_date" varchar,
   "log_hour" varchar
)
WITH (
   external_location = 'hdfs://hadoop-kent/melon_ods_stat/production/raw/kafka/ods_stat/o_act_log_like/data',
   format = 'PARQUET',
   partitioned_by = ARRAY['log_date','log_hour']
)