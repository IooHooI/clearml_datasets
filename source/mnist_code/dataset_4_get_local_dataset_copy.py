import os
from clearml import Dataset

from source.auxiliary_code import global_config


if __name__ == "__main__":
    mnist_dataset = Dataset.get(dataset_project=global_config.DATASET_PROJECT, dataset_name='MNIST')

    target_folder = mnist_dataset.get_local_copy()

    print(target_folder)

