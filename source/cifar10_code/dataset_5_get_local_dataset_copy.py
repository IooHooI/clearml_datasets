from clearml import Dataset

from source.auxiliary_code import global_config


if __name__ == "__main__":
    dataset_name = 'CIFAR10'

    cifar10_dataset = Dataset.get(dataset_project=global_config.DATASET_PROJECT, dataset_name=dataset_name)

    target_folder = cifar10_dataset.get_local_copy()

    print(target_folder)
