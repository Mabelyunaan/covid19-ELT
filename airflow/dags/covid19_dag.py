from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data


default_args = {
    "owner": "airflow",
    "retries": 1,
}

with DAG(
    dag_id="covid_etl_pipeline",
    default_args=default_args,
    description="COVID-19 ETL Pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:

    extract_task = PythonOperator(
        task_id="extract_covid_data",
        python_callable=extract_data,
    )

    transform_task = PythonOperator(
        task_id="transform_covid_data",
        python_callable=transform_data,
        op_kwargs={
            "extract_path": "data/extract",
            "transform_path": "data/transform",
        },
    )

    load_task = PythonOperator(
        task_id="load_covid_data",
        python_callable=load_data,
        op_kwargs={
            "csv_path": "data/transform/covid_metrics_long.csv",
        },
    )

    extract_task >> transform_task >> load_task
