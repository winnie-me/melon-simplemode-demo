import logging
from fastapi import APIRouter, Request

# 로그 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/user-profile-customs")  # julian
def user_profile_customs(request: Request):
    user_id = request.query_params.get("user_id")
    # limit = request.query_params.get("limit", "20")

    logger.info(f"ref")
    if not user_id:
        return {"error": "Missing required query parameter: user_id"}
    user_id = int(user_id)
    # limit = int(limit)
    ref = request.app.state.fs_client.collection("user_profile_customs") \
        .where("user_id", "==", user_id) \
        .stream()
    # .limit(limit) \

    docs_list = list(ref)

    results = []
    for doc in docs_list:
        doc_dict = doc.to_dict()
        results.append({
            'user_id': doc_dict.get('user_id'),
            'customs': doc_dict.get('customs')
        })

    return {"data": results}


@router.get("/custom-collection")  # julian
def custom_key_collection(request: Request):
    id = request.query_params.get("id")

    if not id:
        return {"error": "Missing required query parameter: id"}
    id = int(id)

    ref = request.app.state.fs_client.collection("custom_collection") \
        .where("id", "==", id) \
        .stream()

    docs_list = list(ref)

    results = []
    for doc in docs_list:
        doc_dict = doc.to_dict()
        songs = sorted(doc_dict.get('songs', []), key=lambda song: song.get('_order', float('inf')))

        results.append({
            'id': doc_dict.get('id'),
            'theme': doc_dict.get('theme'),
            'style': doc_dict.get('style'),
            'title': doc_dict.get('title'),
            'songs': songs #doc_dict.get('songs')
        })

    return {"data": results}


@router.get("/list")
def lists(request: Request):
    user_id = request.query_params.get("user_id")
    # limit = request.query_params.get("limit", "20")

    logger.info(f"ref")
    if not user_id:
        return {"error": "Missing required query parameter: user_id"}
    user_id = int(user_id)
    # limit = int(limit)
    ref = request.app.state.fs_client.collection("custom_collection_list") \
        .where("user_id", "==", user_id) \
        .stream()
    # .limit(limit) \

    docs_list = list(ref)

    results = []
    for doc in docs_list:
        doc_dict = doc.to_dict()

        for custom in doc_dict.get('customs'):
            songs = sorted(custom.get('songs', []), key=lambda song: song.get('_order', float('inf')))
            custom['songs'] = songs

        results.append({
            'user_id': doc_dict.get('user_id'),
            'customs': doc_dict.get('customs')
        })

    return {"data": results}
