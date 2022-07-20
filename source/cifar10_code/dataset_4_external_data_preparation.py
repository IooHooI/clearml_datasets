import os

from clearml import Dataset

from clearml.utilities.pyhocon import ConfigFactory

from source.auxiliary_code import global_config


if __name__ == "__main__":
    dataset_name = 'CIFAR10'

    cifar10_dataset = Dataset.get(dataset_project=global_config.DATASET_PROJECT, dataset_name=dataset_name)

    data_path = os.path.join(global_config.get_temp_data_path(), dataset_name)

    clearml_conf = ConfigFactory.parse_file(os.path.join(os.environ["HOME"], "clearml.conf"))

    cifar10_dataset.add_external_files(
        source_url="s3://{}/{}/{}".format(
            clearml_conf["sdk"]["aws"]["s3"]["host"],
            clearml_conf["sdk"]["aws"]["s3"]["credentials"][0]["bucket"],
            "clearml_demo/clearml_datasets/EXTERNAL_FILES"
        ),
        dataset_path=os.path.join(dataset_name, 'train/external'),
        verbose=True
    )

    Dataset.upload(cifar10_dataset, verbose=True)
