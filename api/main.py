from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from google.cloud import bigquery
import os

app = FastAPI()

# CORS 미들웨어 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 도메인에서 요청 허용 (보안 고려 시 특정 도메인만 지정)
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드 허용
    allow_headers=["*"],  # 모든 헤더 허용
)

# 환경 변수에서 프로젝트 ID 가져오기
PROJECT_ID = os.getenv("GCP_PROJECT_ID", "dev-ai-project-357507")
# DATASET = "your_dataset"
# TABLE = "your_table"

@app.get("/")
def read_root():
    return {"message": "BigQuery API Server Running"}

@app.get("/data")
def get_bigquery_data():
    client = bigquery.Client(project=PROJECT_ID)
    query = f"""
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
    query_job = client.query(query)

    results = [dict(row) for row in query_job]
    return {"data": results}
