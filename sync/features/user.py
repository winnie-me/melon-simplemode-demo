from utils.resources import print_memory_usage
from utils.bq_utils import log_table_count


def users(bq_client, fs_client):
    query = f"""
    SELECT ARRAY_AGG(user_id) AS all_users
    FROM tmp_winnie.demo_users
    """
    query_job = bq_client.query(query)
    print_memory_usage()

    collection_ref = fs_client.collection("user")

    for row in query_job:
        row = dict(row)
        print(row)

        collection_ref.document("all_users").set({
            "all_users": row['all_users'],
        })



