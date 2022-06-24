import os

from clearml import Dataset

from source.auxiliary_code import global_config


if __name__ == "__main__":
    dataset_name = 'FASHION_MNIST'

    fashion_mnist_dataset = Dataset.get(dataset_project=global_config.DATASET_PROJECT, dataset_name=dataset_name)

    data_path = os.path.join(global_config.get_temp_data_path(), dataset_name)

    fashion_mnist_dataset.add_files(
        path=os.path.join(data_path, 'train-images-idx3-ubyte'),
        dataset_path=os.path.join(dataset_name, 'train'),
        verbose=True
    )
    fashion_mnist_dataset.add_files(
        path=os.path.join(data_path, 'train-labels-idx1-ubyte'),
        dataset_path=os.path.join(dataset_name, 'train'),
        verbose=True
    )

    Dataset.upload(fashion_mnist_dataset, verbose=True)

    fashion_mnist_dataset.finalize()
