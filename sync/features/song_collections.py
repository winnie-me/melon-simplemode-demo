from utils.resources import print_memory_usage
from utils.bq_utils import log_table_count


def user_profile_songs(bq_client, fs_client):
    query = f"""
    select * from tmp_winnie.demo_melon_user_profile_songs
    """
    query_job = bq_client.query(query)
    print_memory_usage()

    collection_ref = fs_client.collection("user_profile_songs")

    for row in query_job:
        row = dict(row)

        collection_ref.document(str(row['user_id'])).set({
            "user_id": row['user_id'],
            "songs": row['songs']
        })

    query = "SELECT COUNT(*) FROM tmp_winnie.demo_melon_user_profile_songs"
    log_table_count(bq_client, query, 'demo_melon_user_profile_songs')


def song_key_mapping(bq_client, fs_client):
    query = f"""
    select * from tmp_winnie.demo_melon_song_key_mapping
    """
    query_job = bq_client.query(query)
    print_memory_usage()

    collection_ref = fs_client.collection("song_key_mapping")

    for row in query_job:
        row = dict(row)
        # print(row)

        collection_ref.document(str(row['song_id'])).set({
            "song_id": row['song_id'],
            "keys": row['keys']
        })

    query = "SELECT COUNT(*) FROM tmp_winnie.demo_melon_song_key_mapping"
    log_table_count(bq_client, query, 'demo_melon_song_key_mapping')


def song_key_collection(bq_client, fs_client):
    query = f"""
    select * from tmp_winnie.demo_melon_song_key_collection
    """
    query_job = bq_client.query(query)
    print_memory_usage()

    collection_ref = fs_client.collection("song_key_collection")

    for row in query_job:
        row = dict(row)

        collection_ref.document(f"{row['song_id']}_{row['key_id']}").set({
            "song_id": row['song_id'],
            "key_id": row['key_id'],
            "key_title": row['key_title'],
            "songs": row['songs']
        })

    query = "SELECT COUNT(*) FROM tmp_winnie.demo_melon_song_key_collection"
    log_table_count(bq_client, query, 'demo_melon_song_key_collection')

