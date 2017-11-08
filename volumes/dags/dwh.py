# -*- coding: utf-8 -*-
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import airflow
from builtins import range
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.mssql_operator import MsSqlOperator
from airflow.models import DAG
from datetime import timedelta


args = {
    'owner': 'airflow',
    'start_date': airflow.utils.dates.days_ago(2)
}

dag = DAG(
    dag_id='dwh', default_args=args,
    schedule_interval='@daily',
    dagrun_timeout=timedelta(minutes=60))

task_select = MsSqlOperator(task_id='task_select',
                                        sql='SELECT * FROM OnlineEneco LIMIT 100',
                                        mssql_conn_id='azure_dwh',
                                        dag=dag)

if __name__ == "__main__":
    dag.cli()