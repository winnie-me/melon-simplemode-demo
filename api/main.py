import random

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request
from google.cloud import bigquery, firestore
import os
from contextlib import asynccontextmanager

# API 라우터 파일 가져오기
from feature.bigquery_api import router as bigquery_router
from feature.firestore_api import router as firestore_router
from feature.trending_revival import router as trending_revival_router
from feature.song_collections import router as song_collections_router
from feature.artist_collections import router as artist_collections_router
from feature.custom_collections import router as custom_collections_router
from feature.listening_personality import router as listening_personality_router
from feature.seasonality import router as seasonality_router
from feature.user_history import router as user_history_router

# 환경 변수에서 프로젝트 ID 가져오기
PROJECT_ID = os.getenv("GCP_PROJECT_ID", "dev-ai-project-357507")

# ✅ 전역 BigQuery & Firestore 클라이언트
bigquery_client = None
fs_client = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.bigquery_client = bigquery.Client(project=PROJECT_ID)  # ✅ `app.state`에 저장
    app.state.fs_client = firestore.Client()  # database="simplemode-demo"
    print("Clients initialized.")

    # ✅ 모든 등록된 API 라우트 로그 출력
    print("\n🔹 Registered API Endpoints:")
    for route in app.routes:
        if hasattr(route, "methods"):
            methods = ", ".join(route.methods)
            print(f"  {methods}: {route.path}")

    yield  # FastAPI 실행

    app.state.bigquery_client.close()
    app.state.fs_client.close()
    print("Clients closed.")


app = FastAPI(lifespan=lifespan)

# CORS 설정 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ 분리된 API 라우터 등록
app.include_router(bigquery_router, prefix="/bigquery", tags=["BigQuery"])
app.include_router(firestore_router, prefix="/firestore", tags=["Firestore"])
app.include_router(trending_revival_router, prefix="/trending-revival", tags=["chacha"])
app.include_router(song_collections_router, prefix="/collections", tags=["julian-song"])
app.include_router(artist_collections_router, prefix="/artist-collections", tags=["julian-artist"])
app.include_router(custom_collections_router, prefix="/custom-collections", tags=["julian-custom"])
app.include_router(listening_personality_router, prefix="/listening-personality", tags=["listening-personality"])
app.include_router(seasonality_router, prefix="/seasonality", tags=["seasonality_router"])
app.include_router(user_history_router, prefix="/user-history", tags=["user_history_router"])


@app.get("/")
def read_root():
    return {"message": "API Server Running"}


@app.get("/data")
def get_bigquery_data(request: Request):
    song_ref = request.app.state.fs_client.collection("random_song")
    song_docs = song_ref.stream()

    docs_list = list(song_docs)

    results = []
    for doc in docs_list:
        doc_dict = doc.to_dict()
        results.append({
            'song_id': doc.id,
            "album_id": doc_dict.get('album_id'),
            "title": doc_dict.get('title'),
            "artist_names": doc_dict.get('artist_names'),
            "img": doc_dict.get('img'),
        })

    return {"data": results}


