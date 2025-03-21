## Library
import pendulum
import logging

from airflow import models
from airflow.models import Variable, BaseOperator
from airflow.operators.bash import BashOperator

## Custom Libraries
from dependencies.date_utils import ts_by_run_id

## common variables
ENV = Variable.get('environment')

## DAG variables 
DAG_ID = 'melon-simplemode-demo-test'

user_defined_macros = {
    "ts_by_run_id": ts_by_run_id,
}

default_args = {
    'owner': 'winnie',
}

logging.getLogger().setLevel(logging.INFO)

PROJECT_ID = Variable.get('project')
REGION = "asia-northeast3"
CLOUD_RUN_JOB_NAME = "winnie-test-bigquery-sync-firestore"

with models.DAG(
        DAG_ID,
        tags=["melon-demo"],
        default_args=default_args,
        start_date=pendulum.datetime(2025, 3, 21, 0, 0, 0, tz="Asia/Seoul"),
        end_date=pendulum.datetime(2025, 3, 24, 0, 0, 0, tz="Asia/Seoul"),
        schedule_interval='@hourly',
        catchup=True,
        user_defined_macros=user_defined_macros,
        max_active_tasks=2
) as dag:
    invoke_cloud_run_job = BashOperator(
        task_id='invoke_cloud_run_job',
        bash_command='''
            gcloud run jobs execute winnie-test-bigquery-sync-firestore \\
            --region=asia-northeast3 \\
            --wait \\
            --tasks=1 \\
            --task-timeout=30m \\
            --format=json \\
            --log-http
        '''
    )

    invoke_cloud_run_job
