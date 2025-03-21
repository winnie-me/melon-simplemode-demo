import logging
from concurrent.futures import ThreadPoolExecutor
from utils.clients import get_bigquery_client, get_firestore_client
from features.song_collections import user_profile_songs, song_key_mapping, song_key_collection
from features.artist_collections import user_profile_artists, artist_key_mapping, artist_key_collection
from features.custom_collections import user_profile_customs, user_profile_customs_list
from features.user import users

# ✅ 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("cloud_run_job")

# ✅ 그룹별 함수 리스트 정의
task_groups = {
    "song_collections": [user_profile_songs, song_key_mapping, song_key_collection],
    "artist_collections": [user_profile_artists, artist_key_mapping, artist_key_collection],
    "custom_collections": [user_profile_customs, user_profile_customs_list],
}


def run_task_group(group_name, task_list, bq_client, fs_client):
    """그룹별 작업 실행"""
    logger.info(f"그룹 {group_name} 실행 시작 🚀")
    for task in task_list:
        task(bq_client, fs_client)  # 개별 함수 실행
    logger.info(f"그룹 {group_name} 실행 완료 🎯")


if __name__ == "__main__":
    logger.info("Cloud Run Job 시작 🎯")

    bq_client = get_bigquery_client()
    fs_client = get_firestore_client()

    # 초기화 로직
    users(bq_client, fs_client)

    futures = []
    # 병렬 실행
    with ThreadPoolExecutor(max_workers=len(task_groups)) as executor:
        for group_name, task_list in task_groups.items():
            future = executor.submit(run_task_group, group_name, task_list,
                                     bq_client, fs_client)
            futures.append(future)

        # 모든 작업이 완료될 때까지 기다림
        for future in futures:
            try:
                result = future.result()  # 이 호출은 작업이 완료될 때까지 블록됩니다
                logger.info(f"작업 그룹 완료: {result}")
            except Exception as e:
                logger.error(f"작업 그룹 실행 중 오류 발생: {str(e)}")

    logger.info("Cloud Run Job 전체 실행 완료 🎯")
