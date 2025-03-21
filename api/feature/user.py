import logging
from fastapi import APIRouter, Request

# 로그 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/list")
def lists(request: Request):
    # user_id = request.query_params.get("user_id")
    # limit = request.query_params.get("limit", "20")

    # logger.info(f"ref")
    # if not user_id:
    #     return {"error": "Missing required query parameter: user_id"}
    # user_id = int(user_id)
    # limit = int(limit)
    ref = request.app.state.fs_client.collection("user") \
        .stream()
    # .limit(limit) \

    docs_list = list(ref)

    results = []
    for doc in docs_list:
        doc_dict = doc.to_dict()

        # for custom in doc_dict.get('customs'):
        #     songs = sorted(custom.get('songs', []), key=lambda song: song.get('_order', float('inf')))
        #     custom['songs'] = songs

        results.append({
            'all_users': doc_dict.get('all_users'),
            # 'customs': doc_dict.get('customs')
        })

    return {"data": results}
