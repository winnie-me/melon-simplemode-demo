from utils.logger import get_logger

logger = get_logger()

def log_table_count(bq_client, query, job_id):
    query = query
    query_job = bq_client.query(query)

    result_rows = list(query_job.result())

    if not result_rows:
        return None  # 결과가 없을 경우

    # result = query_job.result().to_dataframe()
    print(f"{job_id} : {result_rows[0][0]}")
    # logger.info(job_id, result)