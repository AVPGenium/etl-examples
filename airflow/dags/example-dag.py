from datetime import timedelta, datetime

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import timedelta

import airflow
from airflow.models import Variable
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.postgres_operator import PostgresOperator

BATCH_NUMBER = int(Variable.get("core__ingestion__batch_count", "3"))
PROCESS_DOWNLOAD_FILE = "process_download_segy_file"
PROCESS_REMOVE_FILE = "process_remove_segy_file"
PROCESS_SEGY_FILE = "process_segy_file"
PROCESS_SINGLE_MANIFEST_FILE = "process_single_manifest_segy_file"
PROCESS_BATCH_SEGY_FILE = "batch_segy_upload"
ENSURE_INTEGRITY_TASK = "provide_manifest_integrity_task"
SINGLE_MANIFEST_FILE_FIRST_OPERATOR = "validate_manifest_schema_task"

default_args = {
    "start_date": airflow.utils.dates.days_ago(0),
    "retries": 0,
    "retry_delay": timedelta(seconds=30),
    "trigger_rule": "none_failed",
}


def workflow(**context):
    print(context)


workflow_name = "ingest_test"

with DAG(
    workflow_name,
    default_args=default_args,
    description="GPN manifest with SegY files",
    schedule_interval=None,
    dagrun_timeout=timedelta(minutes=60)
) as dag:


    create_osdu_obj_tables = PostgresOperator(
        task_id="create_osdu_obj_table_task",
        postgres_conn_id="postgres_airflow_ingest",
        sql="sql/init_db.sql",
    )

    test = PythonOperator(
        task_id=PROCESS_BATCH_SEGY_FILE + '1',
        python_callable=workflow,
        provide_context=True,
        dag=dag)

    # Dummy operator as entry point into parallel task of batch upload
    batch_upload = DummyOperator(
        dag=dag,
        task_id=PROCESS_BATCH_SEGY_FILE
    )


create_osdu_obj_tables >> test >> batch_upload