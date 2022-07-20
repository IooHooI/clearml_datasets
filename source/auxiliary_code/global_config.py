import os


DATASET_PROJECT = 'some_demo'
ROOT_PROJECT_NAME = 'clearml_datasets'
TEMP_DATA_PATH = 'tmp'


def get_temp_data_path():
    root_dir = os.path.dirname(os.path.abspath(__file__))

    dirs = root_dir.split(ROOT_PROJECT_NAME)

    return os.path.join(dirs[0], ROOT_PROJECT_NAME, TEMP_DATA_PATH)
