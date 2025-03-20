import random
from fastapi import APIRouter, Request

router = APIRouter()


# ✅ Firestore에서 랜덤 키 4개 가져오기
@router.get("/list")
def lists(request: Request):
    # key_ref = request.app.state.fs_client.collection("demo_user_history")
    # key_docs = key_ref.stream()
    #
    # docs_list = list(key_docs)
    # random_docs = random.sample(docs_list, min(4, len(docs_list)))
    #
    # results = []
    # for doc in random_docs:
    #     doc_dict = doc.to_dict()
    #     results.append({
    #         'key': doc.id,
    #         'consistency': doc_dict.get('consistency')
    #     })
    #
    # return {"data": results}

    ref = request.app.state.fs_client.collection("demo_user_history") \
        .stream()

    docs_list = list(ref)

    results = []
    for doc in docs_list:
        doc_dict = doc.to_dict()

        # for content in doc_dict.get('contents'):
        #     content['title'] = content.get('seasonality')

        results.append({
            'dt': doc_dict.get('dt'),
            'user_ids': doc_dict.get('user_ids')
        })

    return {"data": results}