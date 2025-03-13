from datetime import datetime
from fastapi import APIRouter, Request

router = APIRouter()


@router.get("/detail")  # chacha
def details(request: Request):
    peak_month = request.query_params.get("peak_month")  # %Y-%m
    if not peak_month:
        return {"error": "Missing required query parameter: peak_month"}
    dt = datetime.fromisoformat(peak_month + '-01 00:00 +09:00')

    ref = request.app.state.fs_client.collection("trending_revival_songs") \
        .where("peak_month", "==", dt) \
        .stream()

    docs_list = list(ref)

    results = []
    for doc in docs_list:
        doc_dict = doc.to_dict()
        results.append({
            'peak_month': doc.id,
            'songs': doc_dict.get('songs')
        })

    return {"data": results}


@router.get("/list")  # chacha
def lists(request: Request):
    ref = request.app.state.fs_client.collection("trending_revival_songs_list") \
        .stream()

    docs_list = list(ref)

    results = []
    for doc in docs_list:
        doc_dict = doc.to_dict()
        results.append({
            'contents': doc_dict.get('contents')
        })

    return {"data": results}
