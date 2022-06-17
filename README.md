# ClearML Datasets

## Introduction

This is a toy example of the project with image datasets stored under ClearML platform.

It contains some of the most popular datasets, namely:
- CIDFAR10;
- MNIST;
- Fashion MNIST.
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

```shell
conda create python=3.8 --file environment.yaml
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

### Step 6: Check Datasets in clearml_datasets project

Type the following command in the terminal:

```shell
clearml-data search
```

You should see something like this:

```shell
clearml-data - Dataset Management & Versioning CLI
Search datasets
project          | name                             | tags                | created             | id                              
----------------------------------------------------------------------------------------------------------------------------------
ClearML - Nvidia Framework Examples/Clara | Example data                     |                     | 2021-02-14 17:07:24+00:00 | 2a619936b4204f5ebfeefefd66bddf03
ClearML - Nvidia Framework Examples/TLTv3 | Example Dataset                  |                     | 2021-04-08 06:41:30 | 9751c847f6664f52a096e1264b258fad
```

## How To...

This section gives an overview of what (and how) you can do with your datasets.

Below are steps with more detailed description of code snippets/commands/etc.

### Create a new Dataset entity

[TBD]

#### CIFAR10

[TBD]

#### MNIST

[TBD]

#### Fashion MNIST

[TBD]

### Upload data to your dataset

[TBD]

#### CIFAR10

[TBD]

#### MNIST

[TBD]

#### Fashion MNIST

[TBD]

### Add some meta-info about your Dataset

[TBD]

#### CIFAR10

[TBD]

#### MNIST

[TBD]

#### Fashion MNIST

[TBD]

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
