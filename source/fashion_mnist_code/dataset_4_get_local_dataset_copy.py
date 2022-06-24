from clearml import Dataset

from source.auxiliary_code import global_config


if __name__ == "__main__":
    fashion_mnist_dataset = Dataset.get(dataset_project=global_config.DATASET_PROJECT, dataset_name='FASHION_MNIST')

    target_folder = fashion_mnist_dataset.get_local_copy()

    print(target_folder)
