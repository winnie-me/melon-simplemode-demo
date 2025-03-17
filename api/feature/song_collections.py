from fastapi import APIRouter, Request

router = APIRouter()


@router.get("/user-profile-songs")  # julian
def user_profile_songs(request: Request):
    user_id = request.query_params.get("user_id")
    # limit = request.query_params.get("limit", "20")

    if not user_id:
        return {"error": "Missing required query parameter: user_id"}
    user_id = int(user_id)
    # limit = int(limit)

    ref = request.app.state.fs_client.collection("user_profile_songs") \
        .where("user_id", "==", user_id) \
        .stream()
    # .limit(limit) \

    docs_list = list(ref)

    results = []
    for doc in docs_list:
        doc_dict = doc.to_dict()
        results.append({
            'user_id': doc_dict.get('user_id'),
            'songs': doc_dict.get('songs')
        })

    return {"data": results}


@router.get("/song-key-mapping")  # julian
def song_key_mapping(request: Request):
    song_id = request.query_params.get("song_id")

    if not song_id:
        return {"error": "Missing required query parameter: song_id"}
    song_id = int(song_id)

    ref = request.app.state.fs_client.collection("song_key_mapping") \
        .where("song_id", "==", song_id) \
        .stream()

    docs_list = list(ref)

    results = []
    for doc in docs_list:
        doc_dict = doc.to_dict()
        results.append({
            'song_id': doc_dict.get('song_id'),
            'keys': doc_dict.get('keys')
        })

    return {"data": results}


@router.get("/song-key-collection")  # julian
def song_key_collection(request: Request):
    song_id = request.query_params.get("song_id")
    key_id = request.query_params.get("key_id")

    if not song_id or not key_id:
        return {"error": "Missing required query parameter: song_id, key_id"}
    song_id = int(song_id)
    key_id = int(key_id)

    ref = request.app.state.fs_client.collection("song_key_collection") \
        .where("song_id", "==", song_id) \
        .where("key_id", "==", key_id) \
        .stream()

    docs_list = list(ref)

    results = []
    for doc in docs_list:
        doc_dict = doc.to_dict()
        results.append({
            'song_id': doc_dict.get('song_id'),
            'key_id': doc_dict.get('key_id'),
            'key_title': doc_dict.get('key_title'),
            'songs': doc_dict.get('songs')
        })

    return {"data": results}
