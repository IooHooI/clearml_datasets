from clearml import Dataset


if __name__ == "__main__":
    fashion_mnist_dataset = Dataset.create(dataset_project='clearml_demo/clearml_datasets', dataset_name='FASHION_MNIST')

    for dataset in Dataset.list_datasets(dataset_project='clearml_demo/clearml_datasets', only_completed=False):
        print(dataset)
