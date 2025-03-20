
팬맺기   
```sql
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
```

---

좋아요 
```sql
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
```

---

```sql

create or replace table `tmp_winnie.demo_melon_user_profile_history` as 
SELECT 
    date('2025-03-19') as dt,
    user.id AS user_id, 
    entryPoint.kind as const_kind, 
    entryPoint.id as const_id, 
    entryPoint.title as const_title, 
    entryPoint.score as const_score 
FROM `tmp.melon_user_profile` user, UNNEST(entryPoints) entryPoint
WHERE user.id IN (46536104, 59040609, 37884321, 52894215, 59337842)
---

MERGE INTO `tmp_winnie.demo_melon_user_profile_history` AS B
USING (
    SELECT 
        date('2025-03-06') as dt,
        user.id AS user_id, 
        entryPoint.kind as const_kind, 
        entryPoint.id as const_id, 
        entryPoint.title as const_title, 
        entryPoint.score as const_score 
    FROM `tmp.melon_user_profile_test_20250306` user, UNNEST(entryPoints) entryPoint
    WHERE user.id IN (46536104, 59040609, 37884321, 52894215, 59337842)
) AS A
ON B.user_id = A.user_id 
and B.const_kind = A.const_kind 
and B.const_id = A.const_id 
and B.const_score = A.const_score 
and B.dt = date(timestamp('2025-03-06'), 'Asia/Seoul') 

WHEN MATCHED THEN
  UPDATE SET
    B.user_id = A.user_id,
    B.const_kind = A.const_kind,
    B.const_id = A.const_id,
    B.const_score = A.const_score 

WHEN NOT MATCHED THEN
  INSERT (user_id, const_kind, const_id, const_score, dt)
  VALUES (A.user_id, A.const_kind, A.const_id, A.const_score, date(timestamp('2025-03-06'), 'Asia/Seoul'))
```

```sql
MERGE INTO `tmp_winnie.demo_melon_user_profile_history` AS B
USING (
    SELECT 
        date(CURRENT_TIMESTAMP(), 'Asia/Seoul') as dt,
        user.id AS user_id, 
        entryPoint.kind as const_kind, 
        entryPoint.id as const_id, 
        entryPoint.title as const_title, 
        entryPoint.score as const_score 
    FROM `tmp.melon_user_profile` user, UNNEST(entryPoints) entryPoint
    WHERE user.id IN (46536104, 59040609, 37884321, 52894215, 59337842)
) AS A
ON B.user_id = A.user_id 
and B.const_kind = A.const_kind 
and B.const_id = A.const_id 
and B.const_score = A.const_score 
and B.dt = date(CURRENT_TIMESTAMP(), 'Asia/Seoul') 

WHEN MATCHED THEN
  UPDATE SET
    B.user_id = A.user_id,
    B.const_kind = A.const_kind,
    B.const_id = A.const_id,
    B.const_score = A.const_score 

WHEN NOT MATCHED THEN
  INSERT (user_id, const_kind, const_id, const_score, dt)
  VALUES (A.user_id, A.const_kind, A.const_id, A.const_score, date(CURRENT_TIMESTAMP(), 'Asia/Seoul'))
```

```sql
    SELECT id, entryPoints 
    FROM `tmp.melon_user_profile`
    WHERE id IN (46536104, 59040609, 37884321, 52894215, 59337842)
```






















