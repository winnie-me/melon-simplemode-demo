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

# 환경 변수에서 프로젝트 ID 가져오기
PROJECT_ID = os.getenv("GCP_PROJECT_ID", "dev-ai-project-357507")

# ✅ 전역 BigQuery & Firestore 클라이언트
bigquery_client = None
fs_client = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.bigquery_client = bigquery.Client(project=PROJECT_ID)  # ✅ `app.state`에 저장
    app.state.fs_client = firestore.Client(database="simplemode-demo")  # ✅ Firestore도 저장
    print("Clients initialized.")

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


@app.get("/")
def read_root():
    return {"message": "API Server Running"}


@app.get("/data")
def get_bigquery_data(request: Request):
    song_ref = request.app.state.fs_client.collection("random_song")
    song_docs = song_ref.stream()

    docs_list = list(song_docs)
    random_docs = random.shuffle(docs_list)

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
