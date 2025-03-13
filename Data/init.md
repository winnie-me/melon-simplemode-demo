
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
    ARRAY_AGG(
        STRUCT(
            song_id,
            title,
            artist_names,
            album_id,
            img
        ) 
    ) AS songs
FROM add_albub_info
GROUP BY peak_month
-- select * from add_albub_info
```

줄리안 
- tmp_winnie.demo_melon_user_profile_songs
- tmp_winnie.demo_melon_song_key_mapping
- tmp_winnie.demo_melon_song_key_collection
```sql
create or replace view tmp_winnie.demo_melon_user_profile_songs as 
WITH 
user_entries AS ( -- 특정 유저당 score desc 30곡만 가져오기 
    with s as (
      SELECT 
        user.id AS user_id, 
        entryPoint.kind as const_kind, 
        entryPoint.id as song_id, 
        entryPoint.title as const_title, 
        entryPoint.score as const_score, 
        ROW_NUMBER() OVER (PARTITION BY user.id ORDER BY entryPoint.score desc) AS rn
      FROM `tmp.melon_user_profile_test_20250306` user, UNNEST(entryPoints) entryPoint
      WHERE user.id IN (46536104, 59040609)
    ),
    top_50_per_user as (
      SELECT * except(rn)
      FROM s
      WHERE rn <= 30
    )
    select * from top_50_per_user
),
songs as (
    with source as (
        select 
            user_id,
            const_kind,
            song_id,
    --         const_title,
            const_score
        from user_entries
        where const_kind = 'song'
    ),
    add_song_info as (
        select source.*
            ,songs.album_id
            ,songs.title
            ,songs.artist_names
        from source
        left join `prod-ai-project.melon.songs` songs on source.song_id = songs.song_id
    ),
    add_albub_info as (
        select song.*, album.img
        from add_song_info song
        left join `prod-ai-project.melon.albums` album on song.album_id = album.album_id
    ) 
    select * from add_albub_info
)
SELECT 
    user_id,
    ARRAY_AGG(
        STRUCT(
            song_id,
            title,
            artist_names,
            album_id,
            img,
            const_score
        ) 
        ORDER BY const_score DESC
    ) AS songs
FROM songs
GROUP BY user_id
;
```
```sql 
create or replace view tmp_winnie.demo_melon_song_key_mapping as 
WITH 
user_entries AS ( -- 특정 유저당 score desc 30곡만 가져오기 
    with s as (
      SELECT 
        user.id AS user_id, 
        entryPoint.kind as const_kind, 
        entryPoint.id as const_id, 
        entryPoint.title as const_title, 
        entryPoint.score as const_score, 
        ROW_NUMBER() OVER (PARTITION BY user.id ORDER BY entryPoint.score desc) AS rn
      FROM `tmp.melon_user_profile_test_20250306` user, UNNEST(entryPoints) entryPoint
      WHERE user.id IN (46536104, 59040609)
    ),
    top_50_per_user as (
      SELECT * except(rn)
      FROM s
      WHERE rn <= 30
    )
    select * from top_50_per_user
),
target_songs as (
    select distinct const_id
    from user_entries
),
target_keywords as (
    select 
        k.id as song_id,
        k.keys
    from target_songs song
    join `tmp.melon_song_key_mapping_test_20250306` k on song.const_id = k.id
)
select * from target_keywords
```
```sql
create or replace view tmp_winnie.demo_melon_song_key_collection as 
WITH 
user_entries AS ( -- 특정 유저당 score desc 30곡만 가져오기 
    with s as (
      SELECT 
        user.id AS user_id, 
        entryPoint.kind as const_kind, 
        entryPoint.id as const_id, 
        entryPoint.title as const_title, 
        entryPoint.score as const_score, 
        ROW_NUMBER() OVER (PARTITION BY user.id ORDER BY entryPoint.score desc) AS rn
      FROM `tmp.melon_user_profile_test_20250306` user, UNNEST(entryPoints) entryPoint
      WHERE user.id IN (46536104, 59040609)
    ),
    top_50_per_user as (
      SELECT * except(rn)
      FROM s
      WHERE rn <= 30
    )
    select * from top_50_per_user
),
target_songs as (
    select distinct const_id
    from user_entries
),
target_seed_songs as (
    select 
        seed_song.*
    from target_songs song
    join `tmp.melon_song_key_collection_test_20250306` seed_song 
        on song.const_id = seed_song.song_id
),
f_seed_songs_30 as (
    with 
    s as (
      SELECT 
        seed_song.song_id, 
        seed_song.key_id, 
        seed_song.key_title, 
        pool.id as pool_id, 
        pool.songs as sub_songs,
        ROW_NUMBER() OVER (PARTITION BY seed_song.song_id) AS pool_rn
      FROM target_seed_songs seed_song, UNNEST(pools) pool
    ),
    pool_songs as (
        select s.* except(sub_songs),
               sub_song as sub_song_id, 
               ROW_NUMBER() OVER (PARTITION BY song_id, pool_id) AS seed_song_rn
        from s, UNNEST(sub_songs) sub_song
    )
    select 
        song_id,
        key_id,
        key_title,
        pool_id,
        pool_rn,
        sub_song_id
    from pool_songs
    where seed_song_rn <= 30
),
add_song_meta as (
    with add_song_info as (
        select source.*
            ,songs.album_id
            ,songs.title
            ,songs.artist_names
        from f_seed_songs_30 source 
        left join `prod-ai-project.melon.songs` songs 
            on source.sub_song_id = songs.song_id
    ),
    add_albub_info as (
        select song.*, album.img
        from add_song_info song
        left join `prod-ai-project.melon.albums` album on song.album_id = album.album_id
    ) 
    select * from add_albub_info
)
SELECT 
    song_id, key_id, key_title,
    ARRAY_AGG(
        STRUCT(
            sub_song_id as song_id,
            title,
            artist_names,
            album_id,
            img
        ) 
    ) AS songs
FROM add_song_meta
GROUP BY song_id, key_id, key_title
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

