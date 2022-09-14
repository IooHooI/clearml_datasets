import os
import numpy as np
import tqdm
import shutil
import requests
from typing import Dict, Tuple, List, Text
from PIL import Image

from source.auxiliary_code.global_config import get_temp_data_path


def unpickle(file: Text) -> Dict:
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict


def prepare_temp_folder(dataset_name: Text) -> Text:
    temp_folder_path = get_temp_data_path()

    if not os.path.exists(temp_folder_path):
        os.mkdir(temp_folder_path)

    if not os.path.exists(os.path.join(temp_folder_path, dataset_name)):
        os.mkdir(os.path.join(temp_folder_path, dataset_name))

    return temp_folder_path


def get_data_archive(temp_folder: Text) -> Text:
    archive_name = "cifar-10-python.tar.gz"
    archive_url = "https://www.cs.toronto.edu/~kriz/{}".format(archive_name)

    archive_path = os.path.join(temp_folder, archive_name)

    print("Downloading data archive from {}".format(archive_url))

    if not os.path.exists(archive_path):
        r = requests.get(archive_url)

        open(os.path.join(temp_folder, archive_name), 'wb').write(r.content)

    return archive_path


def unzip_data(archive_path: Text) -> Text:
    data_folder = archive_path.split("/")[-1].split(".")[0]

    extract_dir = "{}/{}".format("/".join(archive_path.split("/")[:-1]), data_folder)

    print("Extracting data archive to {}".format(extract_dir))

    shutil.unpack_archive(archive_path, extract_dir)

    return extract_dir


def transform_images(batches: List[Text]) -> List[Dict]:
    images = []

    for batch_path in batches:
        batch = unpickle(batch_path)

        for i in tqdm.tqdm(range(len(batch[b'data']))):
            images.append({
                "image": Image.fromarray(np.reshape(batch[b'data'][i], (32, 32, 3), order='F')),
                "label": str(batch[b'labels'][i]),
                "file_name": batch[b'filenames'][i].decode('utf-8')
            })

    return images


def save_images(images: List[Dict], folder: Text) -> List[Text]:
    image_paths = []
    for i in tqdm.tqdm(range(len(images))):
        if not os.path.exists(os.path.join(folder, images[i]["label"])):
            os.mkdir(os.path.join(folder, images[i]["label"]))

        images[i]["image"].save(os.path.join(folder, images[i]["label"], images[i]["file_name"]))
        image_paths.append(os.path.join(folder, images[i]["label"], images[i]["file_name"]))

    return image_paths


def extract(dataset_name: Text) -> Text:
    temp_folder_path = prepare_temp_folder(dataset_name)

    archive_path = get_data_archive(os.path.join(temp_folder_path, dataset_name))

    data_path = unzip_data(archive_path)

    return data_path


def transform(data_path: Text) -> Tuple[List, List]:
    test_batches = [
        os.path.join(data_path, "cifar-10-batches-py", "test_batch")
    ]
    train_batches = [
        os.path.join(data_path, "cifar-10-batches-py", "data_batch_1"),
        os.path.join(data_path, "cifar-10-batches-py", "data_batch_2"),
        os.path.join(data_path, "cifar-10-batches-py", "data_batch_3"),
        os.path.join(data_path, "cifar-10-batches-py", "data_batch_4"),
        os.path.join(data_path, "cifar-10-batches-py", "data_batch_5")
    ]

    print("Extracting train images from pickle batches")
    train_images = transform_images(train_batches)
    print("Extracting test images from pickle batches")
    test_images = transform_images(test_batches)

    return test_images, train_images


def load(images: Tuple[List, List], dataset_name: Text) -> Tuple[List, List]:
    test_images, train_images = images

    temp_folder_path = get_temp_data_path()

    dataset_folder = os.path.join(temp_folder_path, dataset_name)

    dataset_train_folder = os.path.join(dataset_folder, "train")
    dataset_test_folder = os.path.join(dataset_folder, "test")

    if not os.path.exists(dataset_train_folder):
        os.mkdir(dataset_train_folder)
    if not os.path.exists(dataset_test_folder):
        os.mkdir(dataset_test_folder)

    print("Saving train images to {}".format(dataset_train_folder))
    train_image_paths = save_images(train_images, dataset_train_folder)
    print("Saving test images to {}".format(dataset_test_folder))
    test_image_paths = save_images(test_images, dataset_test_folder)

    return train_image_paths, test_image_paths


if __name__ == "__main__":
    data_path = extract("CIFAR10")

    images = transform(data_path)

    res = load(images, "CIFAR10")
