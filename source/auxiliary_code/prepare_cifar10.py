import os
import numpy as np
import tqdm
from PIL import Image


def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict


if __name__ == "__main__":
    test_batches = [
        "../tmp/cifar10/cifar-10-batches-py/test_batch"
    ]
    train_batches = [
        "../tmp/cifar10/cifar-10-batches-py/data_batch_1",
        "../tmp/cifar10/cifar-10-batches-py/data_batch_2",
        "../tmp/cifar10/cifar-10-batches-py/data_batch_3",
        "../tmp/cifar10/cifar-10-batches-py/data_batch_4",
        "../tmp/cifar10/cifar-10-batches-py/data_batch_5"
    ]

    if not os.path.exists("../../tmp/cifar10/train"):
        os.mkdir("../../tmp/cifar10/train")
    if not os.path.exists("../../tmp/cifar10/test"):
        os.mkdir("../../tmp/cifar10/test")

    for batch_path in train_batches:
        batch = unpickle(batch_path)

        for i in tqdm.tqdm(range(len(batch[b'data']))):
            if not os.path.exists("../tmp/cifar10/train/{}".format(batch[b'labels'][i])):
                os.mkdir("../tmp/cifar10/train/{}".format(batch[b'labels'][i]))

            im = Image.fromarray(np.reshape(batch[b'data'][i], (32, 32, 3), order='F'))

            im.save(
                "../tmp/cifar10/train/{}/{}".format(
                    batch[b'labels'][i],
                    batch[b'filenames'][i].decode('utf-8')
                )
            )

    for batch_path in test_batches:
        batch = unpickle(batch_path)

        for i in tqdm.tqdm(range(len(batch[b'data']))):
            if not os.path.exists("../tmp/cifar10/test/{}".format(batch[b'labels'][i])):
                os.mkdir("../tmp/cifar10/test/{}".format(batch[b'labels'][i]))

            im = Image.fromarray(np.reshape(batch[b'data'][i], (32, 32, 3), order='F'))

            im.save(
                "../tmp/cifar10/test/{}/{}".format(
                    batch[b'labels'][i],
                    batch[b'filenames'][i].decode('utf-8')
                )
            )
