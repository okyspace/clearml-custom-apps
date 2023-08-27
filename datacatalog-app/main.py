import argparse
from time import sleep
from clearml import Task, Dataset

def add_arguments(parser):
    parser.add_argument(
        "--search-entry",
        type=str,
        default="datasets-mnist",
        help="search entry",
    )

def main():
    parser = argparse.ArgumentParser(description="ClearML Datacatalog: Gather datasets available in ClearML")
    add_arguments(parser)
    args = parser.parse_args()

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
            dataset_name=args.search_entry, 
            only_completed=True)
        print("datasets {}".found(datasets))
        task.set_parameter(name='General/datasets_names', value=datasets)

    sleep(10)


if __name__ == "__main__":
    main()
