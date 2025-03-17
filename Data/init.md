
user profile
tmp.melon_user_profile_test_20250306
song - key mapping
tmp.melon_song_key_mapping_test_20250306
song, key collection
tmp.melon_song_key_collection_test_20250306

```sql
from tmp_winnie.demo_melon_user_profile
```

차차 역주행 데이터 (완료)
```sql
create or replace view tmp_winnie.demo_trending_revival_songs as 

-- select * from add_albub_info
```

줄리안 
- tmp_winnie.demo_melon_user_profile_songs
- tmp_winnie.demo_melon_song_key_mapping
- tmp_winnie.demo_melon_song_key_collection
```sql
create or replace view tmp_winnie.demo_melon_user_profile_songs as 

;
```
```sql 
create or replace view tmp_winnie.demo_melon_song_key_mapping as 

```
```sql
create or replace view tmp_winnie.demo_melon_song_key_collection as 

```
줄리안이 전체 pool 대상으로 song_id, key_id 만 조회해서 전달하라는 의미셨구나 -> 그렇게 output 되도록 넣으면 됨
```sql
with s as (
  select count(*) as _count
  from `tmp_winnie.demo_melon_song_key_collection`
  group by song_id, key_id
)
select _count, count(*)
from s 
group by _count
order by _count
```

```sql
WITH 
user_entries AS ( 
    with s as (
      SELECT 
        user.id AS user_id, 
        entryPoint.kind as const_kind, 
        entryPoint.id as song_id, 
        -- entryPoint.title as const_title, 
        entryPoint.score as const_score, 
        ROW_NUMBER() OVER (PARTITION BY user.id ORDER BY entryPoint.score desc) AS rn
      FROM `tmp.melon_user_profile_test_20250306` user, UNNEST(entryPoints) entryPoint
      WHERE user.id IN (46536104, 59040609, 37884321, 52894215)
    ),
    top_50_per_user as (
      SELECT * except(rn)
      FROM s
      WHERE rn <= 50
    )
    select * from top_50_per_user
)
select * from user_entries
```

```sql
with
add_song_info as (
    select 
        source.song_id
        ,source.peak_month
        ,songs.album_id
        ,songs.title
        ,songs.artist_names
    from `dev-ai-project-357507.tmp_winnie.trending_revival_songs_250312` source
    left join `prod-ai-project.melon.songs` songs on source.song_id = songs.song_id
),
add_albub_info as (
    select song.*, album.img
    from add_song_info song
    left join `prod-ai-project.melon.albums` album on song.album_id = album.album_id
) 
SELECT 
    peak_month,
    FORMAT_TIMESTAMP('%y-%m', peak_month, 'Asia/Seoul') as title,
    ARRAY_AGG(
        STRUCT(
            song_id,
            title,
            artist_names,
            album_id,
            img
        ) 
        limit 3
    ) AS songs
FROM add_albub_info
GROUP BY peak_month
order by peak_month desc 
```



----------------
```sql

```


























