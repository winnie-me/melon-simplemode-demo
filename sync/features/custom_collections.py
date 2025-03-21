from utils.resources import print_memory_usage
from utils.bq_utils import log_table_count


def user_profile_customs(bq_client, fs_client):
    query = f"""
    select * from tmp_winnie.demo_melon_custom_collection
    """
    query_job = bq_client.query(query)
    print_memory_usage()

    collection_ref = fs_client.collection("custom_collection")

    for row in query_job:
        row = dict(row)
        # print(row)

        collection_ref.document(str(row['id'])).set({
            "id": row['id'],
            "theme": row['theme'],
            "style": row['style'],
            "title": row['title'],
            "songs": row['songs']
        })

    query = "SELECT COUNT(*) FROM tmp_winnie.demo_melon_custom_collection"
    log_table_count(bq_client, query, 'demo_melon_custom_collection')


def user_profile_customs_list(bq_client, fs_client):
    query = f"""
    select * from tmp_winnie.demo_melon_custom_collection_list
    """
    query_job = bq_client.query(query)
    print_memory_usage()

    collection_ref = fs_client.collection("custom_collection_list")

    for row in query_job:
        row = dict(row)
        # print(row)

        collection_ref.document(str(row['user_id'])).set({
            "user_id": row['user_id'],
            "customs": row['customs']
        })

    query = "SELECT COUNT(*) FROM tmp_winnie.demo_melon_custom_collection_list"
    log_table_count(bq_client, query, 'demo_melon_custom_collection_list')
