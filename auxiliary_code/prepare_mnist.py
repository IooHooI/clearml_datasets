from mnist import MNIST
import shutil
import random
import gzip
import os


def uncompress_file(root_path, from_file, to_file):
    with gzip.open(os.path.join(root_path, from_file), 'rb') as f_in:
        with open(os.path.join(root_path, to_file), 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)


if __name__ == "__main__":
    root_path = '../tmp/mnist'

    if not os.path.exists(os.path.join(root_path, 't10k-images-idx3-ubyte')):
        uncompress_file(root_path, 't10k-images-idx3-ubyte.gz', 't10k-images-idx3-ubyte')
    if not os.path.exists(os.path.join(root_path, 't10k-labels-idx1-ubyte')):
        uncompress_file(root_path, 't10k-labels-idx1-ubyte.gz', 't10k-labels-idx1-ubyte')
    if not os.path.exists(os.path.join(root_path, 'train-images-idx3-ubyte')):
        uncompress_file(root_path, 'train-images-idx3-ubyte.gz', 'train-images-idx3-ubyte')
    if not os.path.exists(os.path.join(root_path, 'train-labels-idx1-ubyte')):
        uncompress_file(root_path, 'train-labels-idx1-ubyte.gz', 'train-labels-idx1-ubyte')

    mnist_data = MNIST('../tmp/mnist')

    train_images, train_labels = mnist_data.load_training()
    # or
    test_images, test_labels = mnist_data.load_testing()

    index = random.randrange(0, len(train_images))  # choose an index ;-)
    print(mnist_data.display(train_images[index]))
