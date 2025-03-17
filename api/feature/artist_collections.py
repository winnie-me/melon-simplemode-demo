import logging
from fastapi import APIRouter, Request

# 로그 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/user-profile-artists")  # julian
def user_profile_artists(request: Request):
    user_id = request.query_params.get("user_id")
    # limit = request.query_params.get("limit", "20")

    logger.info(f"ref")
    if not user_id:
        return {"error": "Missing required query parameter: user_id"}
    user_id = int(user_id)
    # limit = int(limit)
    ref = request.app.state.fs_client.collection("user_profile_artists") \
        .where("user_id", "==", user_id) \
        .stream()
    # .limit(limit) \

    docs_list = list(ref)

    results = []
    for doc in docs_list:
        doc_dict = doc.to_dict()
        results.append({
            'user_id': doc_dict.get('user_id'),
            'artists': doc_dict.get('artists')
        })

    return {"data": results}


@router.get("/artist-key-mapping")  # julian
def artist_key_mapping(request: Request):
    artist_id = request.query_params.get("artist_id")

    if not artist_id:
        return {"error": "Missing required query parameter: artist_id"}
    artist_id = int(artist_id)

    ref = request.app.state.fs_client.collection("artist_key_mapping") \
        .where("artist_id", "==", artist_id) \
        .stream()

    docs_list = list(ref)

    results = []
    for doc in docs_list:
        doc_dict = doc.to_dict()
        results.append({
            'artist_id': doc_dict.get('artist_id'),
            'keys': doc_dict.get('keys')
        })

    return {"data": results}


@router.get("/artist-key-collection")  # julian
def artist_key_collection(request: Request):
    artist_id = request.query_params.get("artist_id")
    key_id = request.query_params.get("key_id")

    if not artist_id or not key_id:
        return {"error": "Missing required query parameter: artist_id, key_id"}
    artist_id = int(artist_id)
    key_id = int(key_id)

    ref = request.app.state.fs_client.collection("artist_key_collection") \
        .where("artist_id", "==", artist_id) \
        .where("key_id", "==", key_id) \
        .stream()

    docs_list = list(ref)

    results = []
    for doc in docs_list:
        doc_dict = doc.to_dict()
        results.append({
            'artist_id': doc_dict.get('artist_id'),
            'key_id': doc_dict.get('key_id'),
            'key_title': doc_dict.get('key_title'),
            'songs': doc_dict.get('songs')
        })

    return {"data": results}
