from clearml import Dataset

from source.auxiliary_code import global_config


if __name__ == "__main__":
    fashion_mnist_dataset = Dataset.create(dataset_project=global_config.DATASET_PROJECT, dataset_name='FASHION_MNIST')

    for dataset in Dataset.list_datasets(dataset_project=global_config.DATASET_PROJECT, only_completed=False):
        print(dataset)
