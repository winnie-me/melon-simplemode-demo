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

```sql
with _all as (
  select *, 'all' as _type
  from `dev-ai-project-357507.melon_user_analysis.listening_personality_v2`
  where h in (mod(46536104, 100),
    mod(59040609, 100),
    mod(37884321, 100),
    mod(52894215, 100),
    mod(59337842, 100)
    
  )
  and user_id in (46536104, 59040609, 37884321, 52894215, 59337842)
  and dt = (
      select max(dt)
      from `dev-ai-project-357507.melon_user_analysis.listening_personality_v2`
  )
),
lp_CC0006 as (
  select *, 'CC0006' as _type
  from `dev-ai-project-357507.melon_user_analysis.listening_personality_v2_CC0006`
  where h in (mod(46536104, 100),
    mod(59040609, 100),
    mod(37884321, 100),
    mod(52894215, 100),
    mod(59337842, 100)
    
  )
  and user_id in (46536104, 59040609, 37884321, 52894215, 59337842)
  and dt = (
      select max(dt)
      from `dev-ai-project-357507.melon_user_analysis.listening_personality_v2_CC0006`
  )
),
lp_CC0014 as (
  select *, 'CC0014' as _type
  from `dev-ai-project-357507.melon_user_analysis.listening_personality_v2_CC0014`
  where h in (mod(46536104, 100),
    mod(59040609, 100),
    mod(37884321, 100),
    mod(52894215, 100),
    mod(59337842, 100)
    
  )
  and user_id in (46536104, 59040609, 37884321, 52894215, 59337842)
  and dt = (
      select max(dt)
      from `dev-ai-project-357507.melon_user_analysis.listening_personality_v2_CC0014`
  )
),
_union as (
    select * from _all
    union all
    select * from lp_CC0006
    union all
    select * from lp_CC0014
)
select user_id,
       array_agg(struct(
           _type,
           tn_score,
           tn_components,
           cu_score,
           cu_components,
           lv_score,
           fe_score
       )) contents
from _union
group by user_id
```


```sql
with s as (
  select *, 'all' as _type
  from `dev-ai-project-357507.melon_user_analysis.listening_personality_v2`
  where h in (mod(46536104, 100),
    mod(59040609, 100),
    mod(37884321, 100),
    mod(52894215, 100),
    mod(59337842, 100)
    
  )
  and user_id in (46536104, 59040609, 37884321, 52894215, 59337842)
  and dt = (
      select max(dt)
      from `dev-ai-project-357507.melon_user_analysis.listening_personality_v2`
  )
),
_ordering as (
    select s.*, 
           tn.id as _tn_id, 
           tn.value as _tn_value, 
           tn.score as _tn_score, 
           cn.id as _cn_id,
           cn.value as _cn_value,
           cn.score as _cn_score
    from s, unnest(tn_components) tn, unnest(cu_components) cn
),
_agg as (

    select user_id, _type, tn_score, cu_score, lv_score, fe_score,
           array_agg(struct(
               _tn_id as id,
               _tn_value as value,
               _tn_score as score
           ) order by _tn_score desc) tn_components,
           array_agg(struct(
               _cn_id as id,
               _cn_value as value,
               _cn_score as score
           ) order by _cn_score desc) cn_components
    from _ordering
    group by user_id, _type, tn_score, cu_score, lv_score, fe_score
)
select * from _agg
```