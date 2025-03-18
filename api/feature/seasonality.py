import logging
from fastapi import APIRouter, Request

# 로그 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/list")  # chacha
def lists(request: Request):
    ref = request.app.state.fs_client.collection("seasonality_list") \
        .stream()

    docs_list = list(ref)

    results = []
    for doc in docs_list:
        doc_dict = doc.to_dict()

        for content in doc_dict.get('contents'):
            content['title'] = content.get('pred')

        results.append({
            'contents': doc_dict.get('contents')
        })

    return {"data": results}


@router.get("/detail")
def details(request: Request):
    pred = request.query_params.get("pred")

    if not pred:
        return {"error": "Missing required query parameter: pred"}

    ref = request.app.state.fs_client.collection("seasonality") \
        .where("pred", "==", pred) \
        .stream()

    docs_list = list(ref)

    results = []
    for doc in docs_list:
        doc_dict = doc.to_dict()
        content_mapping = {}

        results.append({
            'pred': doc_dict.get('pred'),
            'songs': doc_dict.get('songs')
        })

    return {"data": results}
