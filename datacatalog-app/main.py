from time import sleep

from clearml import Task, Dataset
from clearml.backend_api.session.client import APIClient

task = Task.init(
    project_name="DataOps",
    task_name="Datacatalog App",
    task_type=Task.TaskTypes.service,
    reuse_last_task_id=False,
)

logger = task.get_logger()

while True:
    print("Fetching list of Datasets ...")

    datasets = Dataset.get(
        dataset_name="datasets-mnist", 
        only_completed=True)
    task.set_parameter(name='General/datasets_names', value=datasets)

    sleep(10)
