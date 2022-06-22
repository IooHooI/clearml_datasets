import os
from clearml import Dataset


if __name__ == "__main__":
    cifar10_dataset = Dataset.get(
        dataset_project='clearml_datasets',
        dataset_name='CIFAR10'
    )

    for address, dirs, files in os.walk('../tmp/cifar10/train'):
        for name in files:
            cifar10_dataset.add_files(
                path=os.path.join(address, name),
                dataset_path=os.path.join('data', '/'.join(address.split('/')[-2:]), name),
                verbose=True
            )

    for address, dirs, files in os.walk('../tmp/cifar10/test'):
        for name in files:
            cifar10_dataset.add_files(
                path=os.path.join(address, name),
                dataset_path=os.path.join('data', '/'.join(address.split('/')[-2:]), name),
                verbose=True
            )

    Dataset.upload(
        cifar10_dataset,
        verbose=True
    )

    cifar10_dataset.finalize()
