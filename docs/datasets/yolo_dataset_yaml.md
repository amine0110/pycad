# YOLODatasetYaml Documentation
![Dataset Yaml](https://github.com/amine0110/pycad/blob/main/assets/datasetyaml.svg?raw=true)

## Overview
The `YOLODatasetYaml` module provides a utility class for generating a `dataset.yaml` file, which is essential for training a YOLOv8 model. The class handles paths for both training and validation data, specifies the number of classes (`nc`), and names those classes.

## Classes

### `YOLODatasetYaml`

**Description**

This class is for creating the `dataset.yaml` file needed to train a YOLOv8 model. The YAML file will include paths for training and validation data, the number of classes (`nc`), and the names of those classes.

### `__init__(self, train_path, valid_path, nc, *class_names)`

**Parameters**

- `train_path`: The path to the directory containing training images and labels.
- `valid_path`: The path to the directory containing validation images and labels.
- `nc`: The number of classes to train.
- `class_names`: Variable-length argument list for class names.

**Behavior**

Initializes class attributes and sets the class names via the set_class_names method.

### `set_class_names(self, *class_names)`

**Parameters**

- `class_names`: Variable-length argument list for class names.

**Behavior**

Validates and sets the class names.

**Exceptions**

Raises a `ValueError` if the number of classes (`nc`) doesn't match the number of class names provided.

### `save(self, save_path)`

**Parameters**

- `save_path`: The path where the `dataset.yaml` file will be saved.

**Behavior**

Writes the `dataset.yaml` content to a file.

### `create_yaml(self, save_path)`

**Parameters**

- `save_path`: The path where the `dataset.yaml` file will be saved.

**Behavior**

Calls the `save` method to create the ``dataset.yaml`` file.

## Example Usage

```Python
from pycad.datasets import YOLODatasetYaml

config = YOLODatasetYaml("path/to/train", "path/to/valid", 3, "t1", "t2", "t3")
config.create_yaml("dataset.yaml")
```