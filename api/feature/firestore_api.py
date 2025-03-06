import random
from fastapi import APIRouter, Request

router = APIRouter()


# ✅ Firestore에서 랜덤 키 4개 가져오기
@router.get("/random-key")
def get_fs_data(request: Request):
    key_ref = request.app.state.fs_client.collection("key")
    key_docs = key_ref.stream()

    docs_list = list(key_docs)
    random_docs = random.sample(docs_list, min(4, len(docs_list)))

    results = []
    for doc in random_docs:
        doc_dict = doc.to_dict()
        results.append({
            'key': doc.id,
            'consistency': doc_dict.get('consistency')
        })

    return {"data": results}
