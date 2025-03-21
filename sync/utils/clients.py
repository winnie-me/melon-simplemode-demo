from google.cloud import bigquery
from google.cloud import firestore
import os

# 싱글톤 클라이언트 인스턴스
_bigquery_client = None
_firestore_client = None

def get_bigquery_client():
    """BigQuery 클라이언트의 싱글톤 인스턴스를 반환합니다."""
    global _bigquery_client
    if _bigquery_client is None:
        # 환경 변수에서 프로젝트 ID를 가져오거나 기본값 사용
        project_id = os.environ.get('GCP_PROJECT')
        _bigquery_client = bigquery.Client()
        print("BigQuery 클라이언트 초기화 완료")
    return _bigquery_client


def get_firestore_client():
    """Firestore 클라이언트의 싱글톤 인스턴스를 반환합니다."""
    global _firestore_client
    if _firestore_client is None:
        # 환경 변수에서 프로젝트 ID를 가져오거나 기본값 사용
        # project_id = os.environ.get('GCP_PROJECT')
        _firestore_client = firestore.Client()
        print("Firestore 클라이언트 초기화 완료")
    return _firestore_client
