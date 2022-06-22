import os
from clearml import Dataset


if __name__ == "__main__":
    cifar10_dataset = Dataset.get(
        dataset_project='clearml_datasets',
        dataset_name='CIFAR10'
    )

    cifar10_dataset.add_files(
        path='../tmp/cifar10/train',
        local_base_folder='data/train',
        dataset_path='data/train',
        verbose=True
    )

    Dataset.upload(
        cifar10_dataset,
        verbose=True
    )

    cifar10_dataset.finalize()
