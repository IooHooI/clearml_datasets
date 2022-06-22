from clearml import Dataset


if __name__ == "__main__":
    mnist_dataset = Dataset.get(dataset_project='clearml_demo/clearml_datasets', dataset_name='FASHION_MNIST')

    mnist_dataset.add_files(path='../tmp/fashion_mnist/train-images-idx3-ubyte', dataset_path='data/train', verbose=True)
    mnist_dataset.add_files(path='../tmp/fashion_mnist/train-labels-idx1-ubyte', dataset_path='data/train', verbose=True)

    Dataset.upload(mnist_dataset, verbose=True)

    mnist_dataset.finalize()
