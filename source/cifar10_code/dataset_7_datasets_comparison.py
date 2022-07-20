import os

from clearml import Dataset

from source.auxiliary_code import global_config


if __name__ == "__main__":
    dataset_name = 'CIFAR10'

    cifar10_dataset = Dataset.get(
        dataset_project=global_config.DATASET_PROJECT,
        dataset_name='{}_with_tets'.format(dataset_name)
    )

    cifar10_dataset.finalize()

    old_cifar10_dataset = Dataset.get(dataset_project=global_config.DATASET_PROJECT, dataset_name=dataset_name)

