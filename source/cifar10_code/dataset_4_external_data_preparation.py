import os

from clearml.utilities.pyhocon import ConfigFactory

import boto3

from clearml import Dataset

# from source.auxiliary_code import global_config


if __name__ == "__main__":
    # dataset_name = 'CIFAR10'
    #
    # cifar10_dataset = Dataset.get(dataset_project=global_config.DATASET_PROJECT, dataset_name=dataset_name)
    #
    # data_path = os.path.join(global_config.get_temp_data_path(), dataset_name)

    config = ConfigFactory.parse_file(os.path.join(os.environ["HOME"], "clearml.conf"))

    print(config)

    # client = boto3.client(
    #     service_name="s3",
    #     region_name=clearml_conf["sdk"]["aws"]["s3"]["region"],
    #     endpoint_url="https://{}".format(clearml_conf["sdk"]["aws"]["s3"]["host"]),
    #     aws_access_key_id=clearml_conf["sdk"]["aws"]["s3"]["key"],
    #     aws_secret_access_key=clearml_conf["sdk"]["aws"]["s3"]["secret"]
    # )
    #
    # object_list = client.list_objects(Bucket=clearml_conf["sdk"]["aws"]["s3"]["credentials"][0]["bucket"])

    # cifar10_dataset.add_files(
    #     path=os.path.join(data_path, 'train'),
    #     dataset_path=os.path.join(dataset_name, 'train'),
    #     verbose=True
    # )
    #
    # Dataset.upload(cifar10_dataset, verbose=True)
    #
    # cifar10_dataset.finalize()
