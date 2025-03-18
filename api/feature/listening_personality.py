import logging
from fastapi import APIRouter, Request

# 로그 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/list")
def lists(request: Request):
    user_id = request.query_params.get("user_id")
    # limit = request.query_params.get("limit", "20")

    logger.info(f"ref")
    if not user_id:
        return {"error": "Missing required query parameter: user_id"}
    user_id = int(user_id)
    # limit = int(limit)
    ref = request.app.state.fs_client.collection("user_listening_personality") \
        .where("user_id", "==", user_id) \
        .stream()
    # .limit(limit) \

    docs_list = list(ref)

    results = []
    for doc in docs_list:
        doc_dict = doc.to_dict()
        content_mapping = {}

        for content in doc_dict.get('contents'):
            content_mapping[content.get('_type')] = content

        results.append({
            'user_id': doc_dict.get('user_id'),
            'contents': content_mapping
        })

    return {"data": results}
