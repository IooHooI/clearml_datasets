import os

from clearml import Dataset

from source.auxiliary_code import global_config


if __name__ == "__main__":
    dataset_name = 'CIFAR10'

    cifar10_dataset = Dataset.get(dataset_project=global_config.DATASET_PROJECT, dataset_name=dataset_name)

    cifar10_dataset.finalize()

    new_cifar10_dataset = Dataset.create(
        dataset_project=global_config.DATASET_PROJECT,
        dataset_name='{}_with_tets'.format(dataset_name),
        parent_datasets=[cifar10_dataset]
    )

    data_path = os.path.join(global_config.get_temp_data_path(), dataset_name)

    new_cifar10_dataset.add_files(
        path=os.path.join(data_path, 'test'),
        dataset_path=os.path.join(dataset_name, 'test'),
        verbose=True
    )

    Dataset.upload(new_cifar10_dataset, verbose=True)
