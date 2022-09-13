# ClearML Datasets

## Introduction

![alt text](https://424531.selcdn.ru/efim-test-clearml-bucket/images/data_registry_idea.jpeg "Title")

This is a toy example of the project with image datasets stored under ClearML platform.

It contains some of the most popular datasets, namely:
- CIDFAR10 ([link](https://www.cs.toronto.edu/~kriz/cifar.html) to the original page);
- MNIST ([link](http://yann.lecun.com/exdb/mnist/) to the original page);
- Fashion MNIST ([link](https://github.com/zalandoresearch/fashion-mnist#get-the-data) to the original page).
- etc (#todo: add more datasets).

Each package contains the code which:
- Creates a new Dataset entity;
- Uploads data to your dataset;
- Adds some meta-info about your Dataset;
- Creates a new version of the previous Dataset entity;
- Compares Datasets.

## Local environment setup

This section describes steps needed to create a local environment where you can start to work with code.

### Step 0: Enter the repository page

[Here](https://github.com/IooHooI/clearml_datasets) is the link to the respective repository on GitHub.

### Step 1: Cone the repository

```shell
git clone https://github.com/IooHooI/clearml_datasets.git
```

### Step 2: Enter the root repository folder

```shell
cd clearml_datasets
```

### Step 3: Create a conda environment from environment.yaml file

If conda is not installed on your machine you can just download Miniconda from [this](https://docs.conda.io/en/latest/miniconda.html) page and install it.

After installation is complete you can restart the terminal and then run this command:

```shell
conda env create --file environment.yml
```

### Step 4: Activate an environment

```shell
conda activate clearml_datasets
```

### Step 5: Check Clearml CLI connection with Clearml Server

Run the command below:
```shell
clearml-init
```

If the output looks SOMETHING like this:

```shell
ClearML SDK setup process
Configuration file already exists: <HOME DIRECTORY>/clearml.conf
Leaving setup, feel free to edit the configuration file.
```

Then it means that CLI configuration was done earlier.

Please, **MAKE SURE** that this `clearml.conf` file is pointed to the right Clearml Server
(i.e., check app/api/files endpoints and credentials).

Otherwise, you should follow the official CLI setup
[documentation](https://clear.ml/docs/latest/docs/getting_started/ds/ds_first_steps#connect-clearml-sdk-to-the-server).

### Step 5* (Optional): Check connection to your S3-storage

By default `clearml.conf` is generated without any information about S3 buckets.

It is possible, however, to direct all data input/output activities to some S3 bucket.

There are three parts in `clearml.conf` that you can change to configure your ClearML instance to work with S3.

First, you can edit `files_server`:
```yaml
# ClearML SDK configuration file
...
api {
    # Notice: 'host' is the api server (default port 8008), not the web server.
    api_server: https://api.bla.bla.bla.bla.ru
    web_server: https://app.bla.bla.bla.bla.ru
        
    # THIS IS THE FIRST PART
    files_server: s3://<YOUR S3 ENDPOINT>[:<YOUR PORT>]/<YOUR S3 BUCKET>
    
    # Credentials are generated using the webapp, https://app.bla.bla.bla.bla.ru/settings
    # Override with os environment: CLEARML_API_ACCESS_KEY / CLEARML_API_SECRET_KEY
    credentials {"access_key": "BLA", "secret_key": "BLA"}
}
...
```

Second, you can add `S3 credentials`:
```yaml
...
sdk {
...
  aws {
        # THIS IS THE SECOND PART
        s3 {
            host: "<YOUR S3 ENDPOINT>[:<YOUR PORT>]"
            key: "<YOUR S3 ACCESS KEY>"
            region: "<YOUR S3 REGION>"
            secret: "<YOUR S3 SECRET KEY>"
            use_credentials_chain: false
            credentials: [{
                bucket: "<YOUR S3 BUCKET>"
                secure: true
            }]
        }
        boto3 {
            pool_connections: 512
            max_multipart_concurrency: 16
        }
    }
...
}
...
```

And third, you can define `default output url`:
```yaml
...
development {
    ...
    
    # Default Task output_uri. if output_uri is not provided to Task.init, default_output_uri will be used instead.,
    # AND THIS IS THE THIRD PART
    default_output_uri: "s3://<YOUR S3 ENDPOINT>[:<YOUR PORT>]/<YOUR S3 BUCKET>/<YOUR>/<PATH>",
    ...
}
...
```

If you do not provide the second part, then the first and the third parts will be useless, so pay close attention to that.


### Step 6: Check Datasets in clearml_datasets project

Type the following command in the terminal:

```shell
clearml-data search --project clearml_datasets
```

You should see something like this:

```shell
clearml-data - Dataset Management & Versioning CLI
Search datasets
project          | name                             | tags                | created             | id                              
----------------------------------------------------------------------------------------------------------------------------------
```

Or if you haven't created the project `clearml_datasets` before then you'll see something like this:

```shell
clearml-data - Dataset Management & Versioning CLI
Search datasets

Error: No projects found when searching for `clearml_datasets`
```


## How To...

This section gives an overview of what (and how) you can do with your datasets.

Below are steps with more detailed description of code snippets/commands/etc.

### Create a new Dataset entity

This section describes how to create a new dataset in ClearML Server.
Essentially, a dataset in ClearML Server is just an experiment with the type `"data_processing"`.

However, there is a separate part of ClearML SDK which gives all functionality necessary 
to work with these experiments as with datasets.

#### CIFAR10

Here is the [link](https://github.com/IooHooI/clearml_datasets/blob/main/source/cifar10_code/dataset_1_creation.py)
to the script with dataset creation.

Here is how you can execute the script:

```shell
python source/cifar10_code/dataset_1_creation.py
```

After script execution you should see something like this:

```shell
{'name': 'CIFAR10', 'created': datetime.datetime(2022, 6, 21, 11, 11, 30, 448000, tzinfo=tzutc()), 'project': 'clearml_datasets', 'id': 'efb893860f554d459bfdf5775c7297ac', 'tags': []}
```

#### MNIST

Here is the [link](https://github.com/IooHooI/clearml_datasets/blob/main/source/mnist_code/dataset_1_creation.py)
to the script with dataset creation.

Here is how you can execute the script:

```shell
python source/mnist_code/dataset_1_creation.py
```

After script execution you should see something like this:

```shell
{'name': 'CIFAR10', 'created': datetime.datetime(2022, 6, 21, 11, 11, 30, 448000, tzinfo=tzutc()), 'project': 'clearml_datasets', 'id': 'efb893860f554d459bfdf5775c7297ac', 'tags': []}
{'name': 'MNIST', 'created': datetime.datetime(2022, 6, 21, 11, 11, 49, 844000, tzinfo=tzutc()), 'project': 'clearml_datasets', 'id': '1427074363534735ba938cbce11d67a4', 'tags': []}
```

#### Fashion MNIST

Here is the [link](https://github.com/IooHooI/clearml_datasets/blob/main/source/fashion_mnist_code/dataset_1_creation.py)
to the script with dataset creation.

Here is how you can execute the script:

```shell
python source/fashion_mnist_code/dataset_1_creation.py
```

After script execution you should see something like this:

```shell
{'name': 'CIFAR10', 'created': datetime.datetime(2022, 6, 21, 11, 11, 30, 448000, tzinfo=tzutc()), 'project': 'clearml_datasets', 'id': 'efb893860f554d459bfdf5775c7297ac', 'tags': []}
{'name': 'MNIST', 'created': datetime.datetime(2022, 6, 21, 11, 11, 49, 844000, tzinfo=tzutc()), 'project': 'clearml_datasets', 'id': '1427074363534735ba938cbce11d67a4', 'tags': []}
{'name': 'FASHION_MNIST', 'created': datetime.datetime(2022, 6, 21, 11, 14, 21, 182000, tzinfo=tzutc()), 'project': 'clearml_datasets', 'id': '9bec6260e7694a329a21664f8441ff53', 'tags': []}
```

After these steps are executed your datasets should look like this:

![alt text](https://424531.selcdn.ru/efim-test-clearml-bucket/images/datasets_created.png "Title")

### Add some meta-info about your Dataset

This section describes how to add some meta-info about your dataset.

Example: tags (but not only).

Later we also show how to calculate and store some descriptive statistics in your dataset.

#### CIFAR10

Here is the [link](https://github.com/IooHooI/clearml_datasets/blob/main/source/cifar10_code/dataset_2_meta_info_preparation.py)
to the script with dataset meta-info creation.

Here is how you can execute the script:

```shell
python source/cifar10_code/dataset_2_meta_info_preparation.py
```

After script execution you should see something like this:

```shell
{'name': 'CIFAR10', 'created': datetime.datetime(2022, 6, 21, 11, 11, 30, 448000, tzinfo=tzutc()), 'project': 'clearml_datasets', 'id': 'efb893860f554d459bfdf5775c7297ac', 'tags': ['classification', 'example', 'image', 'small']}
{'name': 'MNIST', 'created': datetime.datetime(2022, 6, 21, 11, 11, 49, 844000, tzinfo=tzutc()), 'project': 'clearml_datasets', 'id': '1427074363534735ba938cbce11d67a4', 'tags': []}
{'name': 'FASHION_MNIST', 'created': datetime.datetime(2022, 6, 21, 11, 14, 21, 182000, tzinfo=tzutc()), 'project': 'clearml_datasets', 'id': '9bec6260e7694a329a21664f8441ff53', 'tags': []}
```

Please take a closer look at tags that were added to the respective dataset.

#### MNIST

Here is the [link](https://github.com/IooHooI/clearml_datasets/blob/main/source/mnist_code/dataset_2_meta_info_preparation.py)
to the script with dataset meta-info creation.

Here is how you can execute the script:

```shell
python source/mnist_code/dataset_2_meta_info_preparation.py
```

After script execution you should see something like this:

```shell
{'name': 'CIFAR10', 'created': datetime.datetime(2022, 6, 21, 11, 11, 30, 448000, tzinfo=tzutc()), 'project': 'clearml_datasets', 'id': 'efb893860f554d459bfdf5775c7297ac', 'tags': ['classification', 'example', 'image', 'small']}
{'name': 'MNIST', 'created': datetime.datetime(2022, 6, 21, 11, 11, 49, 844000, tzinfo=tzutc()), 'project': 'clearml_datasets', 'id': '1427074363534735ba938cbce11d67a4', 'tags': ['classification', 'example', 'image', 'small']}
{'name': 'FASHION_MNIST', 'created': datetime.datetime(2022, 6, 21, 11, 14, 21, 182000, tzinfo=tzutc()), 'project': 'clearml_datasets', 'id': '9bec6260e7694a329a21664f8441ff53', 'tags': []}
```

Please take a closer look at tags that were added to the respective dataset.

#### Fashion MNIST

Here is the [link](https://github.com/IooHooI/clearml_datasets/blob/main/source/fashion_mnist_code/dataset_2_meta_info_preparation.py)
to the script with dataset meta-info creation.

Here is how you can execute the script:

```shell
python source/fashion_mnist_code/dataset_2_meta_info_preparation.py
```

After script execution you should see something like this:

```shell
{'name': 'CIFAR10', 'created': datetime.datetime(2022, 6, 21, 11, 11, 30, 448000, tzinfo=tzutc()), 'project': 'clearml_datasets', 'id': 'efb893860f554d459bfdf5775c7297ac', 'tags': ['classification', 'example', 'image', 'small']}
{'name': 'MNIST', 'created': datetime.datetime(2022, 6, 21, 11, 11, 49, 844000, tzinfo=tzutc()), 'project': 'clearml_datasets', 'id': '1427074363534735ba938cbce11d67a4', 'tags': ['classification', 'example', 'image', 'small']}
{'name': 'FASHION_MNIST', 'created': datetime.datetime(2022, 6, 21, 11, 14, 21, 182000, tzinfo=tzutc()), 'project': 'clearml_datasets', 'id': '9bec6260e7694a329a21664f8441ff53', 'tags': ['classification', 'example', 'image', 'small']}
```

Please take a closer look at tags that were added to the respective dataset.

After these steps are executed your datasets should look like this:

![alt text](https://424531.selcdn.ru/efim-test-clearml-bucket/images/datasets_meta_info_created.png "Title")

Of course these tags can be used to filter datasets you need.

### Upload data to your dataset

This section describes how to upload actual data to your dataset.

As in other tools/frameworks, a dataset is just an entity which holds some meta-info about your data.

But you should also actually store your data somewhere.

There are tonnes of data storage options: S3, Azure Blob Storage, Google Storage, FTP Server, HDFS etc.

In this case we have a File Server - the storage component of ClearML Server.

But we can also configure ClearML Server to work with S3/Azure Blob Storage/Google Storage instead of File Server.

#### CIFAR10

Here is the [link](https://github.com/IooHooI/clearml_datasets/blob/main/source/cifar10_code/dataset_3_data_preparation.py)
to the script with actual data uploading.

Here is how you can execute the script:

```shell
python source/cifar10_code/dataset_3_data_preparation.py
```

Once you run the script you should see something like this:

```shell
Add data/train/9/lorry_s_002104.png/lorry_s_002104.png
Add data/train/9/camion_s_000265.png/camion_s_000265.png
Add data/train/9/truck_s_002066.png/truck_s_002066.png
Add data/train/9/tow_truck_s_000968.png/tow_truck_s_000968.png
Add data/train/9/fire_truck_s_001749.png/fire_truck_s_001749.png
Add data/train/9/dump_truck_s_000934.png/dump_truck_s_000934.png
Add data/train/9/lorry_s_000085.png/lorry_s_000085.png
Add data/train/9/sound_truck_s_000508.png/sound_truck_s_000508.png
...
```

#### MNIST

Here is the [link](https://github.com/IooHooI/clearml_datasets/blob/main/source/mnist_code/dataset_3_data_preparation.py)
to the script with actual data uploading.

Here is how you can execute the script:

```shell
cd source/mnist_code/dataset_3_data_preparation.py
```

Once you run the script you should see something like this:

```shell
Add data/train/train-images-idx3-ubyte
Add data/train/train-labels-idx1-ubyte
Compressing /root/clearml_datasets/mnist_code/../tmp/mnist/train-images-idx3-ubyte
Compressing /root/clearml_datasets/mnist_code/../tmp/mnist/train-labels-idx1-ubyte
Uploading dataset changes (2 files compressed to 26.47 MB) to https://files.testing.ulala.achacha.trampampam.org
File compression and upload completed: total size 26.47 MB, 1 chunked stored (average size 26.47 MB)
2022-06-22 12:25:06,086 - clearml.Task - INFO - Waiting to finish uploads
2022-06-22 12:25:06,112 - clearml.Task - INFO - Finished uploading
```

#### Fashion MNIST

Here is the [link](https://github.com/IooHooI/clearml_datasets/blob/main/source/fashion_mnist_code/dataset_3_data_preparation.py)
to the script with actual data uploading.

Here is how you can execute the script:

```shell
cd source/fashion_mnist_code/dataset_3_data_preparation.py
```

Once you run the script you should see something like this:

```shell
Add data/train/train-images-idx3-ubyte
Add data/train/train-labels-idx1-ubyte
Compressing /root/clearml_datasets/fashion_mnist_code/../tmp/fashion_mnist/train-images-idx3-ubyte
Compressing /root/clearml_datasets/fashion_mnist_code/../tmp/fashion_mnist/train-labels-idx1-ubyte
Uploading dataset changes (2 files compressed to 26.47 MB) to https://files.testing.ulala.achacha.trampampam.org
File compression and upload completed: total size 26.47 MB, 1 chunked stored (average size 26.47 MB)
2022-06-22 12:25:06,086 - clearml.Task - INFO - Waiting to finish uploads
2022-06-22 12:25:06,112 - clearml.Task - INFO - Finished uploading
```

After these steps are executed your datasets should look like this:

![alt text](https://424531.selcdn.ru/efim-test-clearml-bucket/images/datasets_data_uploaded.png "Title")

Here is how data is uploaded:

![alt text]( "Title")


### Create a new version of the previous Dataset entity

[TBD]

#### CIFAR10

[TBD]

#### MNIST

[TBD]

#### Fashion MNIST

[TBD]

### Compare Datasets

[TBD]

#### CIFAR10

[TBD]

#### MNIST

[TBD]

#### Fashion MNIST

[TBD]
