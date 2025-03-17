user profile
`tmp.melon_user_profile_test_20250306`

song - key mapping
`tmp.melon_song_key_mapping_test_20250306`
song, key collection
`tmp.melon_song_key_collection_test_20250306`

artist - key mapping
`tmp.melon_artist_key_mapping_test_20250306`
artist, key collection
`tmp.melon_artist_key_collection_test_20250306`

custom collection
`tmp.melon_custom_collection_test_20250306`

---

유저별 콘텐츠별 개수 
```sql
select user_id, const_kind, count(*)
from `tmp_winnie.demo_user_song_entries`
group by user_id, const_kind
```


```sql
config {
    type: "view",
}


with
source as (
    select 
        collection.*,
        song.*,
        ROW_NUMBER() OVER (PARTITION BY collection.id) AS _rn
    from `dev-ai-project-357507.tmp_winnie.demo_melon_custom_collection` collection, UNNEST(songs) song
),
_f_5 as (
    select * except(_rn)
    from source
    where _rn <= 5
),
target_collections as (
    SELECT 
        id,
        theme,
        style,
        collection_title as title,
        ARRAY_AGG(
            STRUCT(
                song_id,
                title,
                artist_names,
                album_id,
                img
            ) 
        ) AS songs
    FROM _f_5
    GROUP BY id, theme, style, collection_title
),
by_user as (
    select 
        user_entry.user_id,
        collection.id,
        collection.theme,
        collection.style,
        collection.title,
        collection.songs
    from `dev-ai-project-357507.tmp_winnie.demo_user_custom_entries` user_entry  
    join target_collections collection on user_entry.const_id = collection.id
)
select user_id,
       ARRAY_AGG(STRUCT(
               id,theme,style,title,songs
       )) as customs
from by_user
group by user_id


```

```sql
by_user as (
    select 
        user_entry.user_id,
        collection.id,
        collection.theme,
        collection.style,
        collection.title,
        collection.songs
    from `dev-ai-project-357507.tmp_winnie.demo_user_custom_entries` user_entry  
    join target_collections collection on user_entry.const_id = collection.id
)
select user_id,
       ARRAY_AGG(id,theme,style,title,songs) as customs
from by_user
group by user_id
```