from clearml import Dataset

if __name__ == "__main__":
    mnist_dataset = Dataset.get(dataset_project='clearml_demo/clearml_datasets', dataset_name='MNIST')

    mnist_dataset.add_tags(['image', 'classification', 'example', 'small'])

    for dataset in Dataset.list_datasets(dataset_project='clearml_demo/clearml_datasets', only_completed=False):
        print(dataset)
