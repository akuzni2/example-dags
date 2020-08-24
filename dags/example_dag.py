import airflow
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import timedelta

from project1.example import step1, step2

print("starting the dag")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(1),
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG(
    'example_dag', default_args=default_args,
    schedule_interval="@hourly")

step1_job = PythonOperator(task_id="step_1", provide_context=True, python_callable=step1, dag=dag)

step2_job = PythonOperator(task_id="step_2", provide_context=True, python_callable=step2, dag=dag)

# steps step2 downstream of step1
step1_job >> step2_job
