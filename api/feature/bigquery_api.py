from fastapi import APIRouter, Request

router = APIRouter()


# ✅ BigQuery 데이터 조회 API
@router.get("/data")
def get_bigquery_data(request: Request):
    query = """
    with source as (
        SELECT song_id 
        FROM `prod-ai-project.melon.daily_user_song_plays` 
        where time_id = timestamp_trunc(timestamp_sub(current_timestamp(), interval 1 day), day, 'Asia/Seoul')
        LIMIT 10
    ),
    add_song_info as (
        select *
        from source
        left join `prod-ai-project.melon.songs` songs on source.song_id = songs.song_id
    ),
    add_albub_info as (
        select song.*, album.img
        from add_song_info song
        left join `prod-ai-project.melon.albums` album on song.album_id = album.album_id
    ) 
    select * from add_albub_info
    """
    query_job = request.app.state.bigquery_client.query(query)

    results = [dict(row) for row in query_job]
    return {"data": results}
