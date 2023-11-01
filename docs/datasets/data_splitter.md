# DataSplitter Documentation
![Data splitter](https://github.com/amine0110/pycad/blob/main/assets/data_splitter_diagram.svg?raw=true)

## Theoretical Background

### What is Data Splitting?
Data splitting is the process of partitioning a dataset into two or more subsets. In the context of machine learning and computer vision, it's common to divide a dataset into training, validation, and sometimes testing sets.

### Why is Data Splitting Necessary?
- ***Generalization***: To build a model that generalizes well to new data, it's essential to validate it on a set of data that it has not seen during training.
- ***Overfitting***: Using separate training and validation sets can help diagnose and prevent overfitting.
- ***Performance Evaluation***: Validation sets are used to fine-tune models and to evaluate their performance.

### What is the YOLO Format?
YOLO (You Only Look Once) is a real-time object detection system, and it expects data to be in a specific directory format. Typically, there are separate folders for images and their corresponding label files for both training and validation sets.

## Module Documentation: `DataSplitter`

### Overview
`DataSplitter` is a Python class designed to partition image and label files into training and validation sets. It's optimized for the YOLO format, making it extremely useful for object detection tasks in medical imaging.

### Class Initialization
```Python
from pycad.datasets import DataSplitter

splitter = DataSplitter(images_dir, labels_dir, output_dir, train_size=0.8, random_state=42, delete_input=False)
```

### Parameters:
- ***images_dir***: Directory containing the input image files.
- ***labels_dir***: Directory containing the input label files.
- ***output_dir***: Directory where the training and validation sets will be saved.
- ***train_size***: Fraction of the data to be used for training (Default is 0.8).
- ***random_state***: Controls the randomness of the train-validation split (Default is 42).
- ***delete_input***: If set to True, deletes the input folders after the split (Default is False).

### Methods
#### `split_data()`

**Returns:**

- Four lists containing the filenames for the training images, validation images, training labels, and validation labels.

**Description:**

Splits the dataset into training and validation sets. This method is typically not called directly by the user.

#### `create_directories()`

**Description:**

Creates the necessary output directories if they don't exist. This includes folders for training and validation images and labels.

#### `copy_files(train_images, valid_images, train_labels, valid_labels)`

**Parameters:**

- `train_images`: List containing the filenames for the training images.
- `valid_images`: List containing the filenames for the validation images.
- `train_labels`: List containing the filenames for the training labels.
- `valid_labels`: List containing the filenames for the validation labels.

**Description:**

Copies the images and labels into their corresponding training and validation directories.

#### `run()`

**Description:**

This method orchestrates the entire process. It calls `split_data()` to get the lists of training and validation files, then `create_directories()` to ensure the output folders exist, and finally `copy_files()` to move the images and labels into their new directories.