import os

from clearml import Dataset

from source.auxiliary_code import global_config


if __name__ == "__main__":
    dataset_name = 'CIFAR10'

    cifar10_dataset = Dataset.get(dataset_project=global_config.DATASET_PROJECT, dataset_name=dataset_name)

    data_path = os.path.join(global_config.get_temp_data_path(), dataset_name)

    cifar10_dataset.add_files(
        path=os.path.join(data_path, 'train'),
        dataset_path=os.path.join(dataset_name, 'train'),
        verbose=True
    )

    Dataset.upload(cifar10_dataset, verbose=True)

    cifar10_dataset.finalize()
