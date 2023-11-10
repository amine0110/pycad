# MONAIDatasetOrganizer Documentation
![Dataset Organizer](https://github.com/amine0110/pycad/blob/main/assets/dataset_organizer_diagram.svg?raw=true)

## Theoretical Background

### What is Dataset Organization?
Dataset organization involves arranging the data into a structured format, making it easy to access and manage for various tasks such as training machine learning models.

### Why is Dataset Organization Important?
- ***Efficiency***: Organized data can be more easily preprocessed, accessed, and loaded during training and testing of models.
- ***Consistency***: It ensures that the data structure is consistent across different stages of model development.
- ***Scalability***: Well-organized datasets are easier to scale and maintain over time.

### What is the nnU-Net Format?
nnU-Net is a framework for biomedical image segmentation that requires datasets to follow a specific directory and file organization. This typically involves separate directories for training images, training labels, and testing images.

## Module Documentation: `MONAIDatasetOrganizer`

### Overview
`MONAIDatasetOrganizer` is a Python class designed to structure image and label files into training, validation, and testing sets following the nnU-Net format, which is particularly useful for segmentation tasks in medical imaging.

### Class Initialization
```python
from pycad.datasets import MONAIDatasetOrganizer

organizer = MONAIDatasetOrganizer(base_dir, output_file='dataset.json')
```

### Parameters:
- `base_dir`: The base directory where the dataset is located and where the structured dataset directories will be created.
- `output_file`: The name of the JSON file that will contain the dataset information (Default is `dataset.json`).

## Methods
### `create_directories()`

#### Description:
Creates the necessary directories for the training, validation, and testing sets, including separate folders for images and labels.

### `move_files(files, destination)`

#### Parameters:
- `files`: A list of file paths that need to be moved.
- `destination`: The directory to which the files will be moved.

#### Description:
Moves the specified files to the given destination directory.

### `split_dataset(train_volumes, train_segmentations, val_split)`

#### Parameters:

- `train_volumes`: List of file paths to the training volumes.
- `train_segmentations`: List of file paths to the training segmentation labels.
- `val_split`: The fraction of the dataset to reserve for validation.

#### Returns:

Two lists of tuples, the first for training and the second for validation, where each tuple contains the paths to the volume and its corresponding label.

#### Description:

Splits the dataset into training and validation sets based on the specified validation split fraction.

### `organize_dataset(train_volumes, test_volumes, train_segmentations, val_split)`

#### Parameters:

- `train_volumes`: List of file paths to the training volumes.
- `test_volumes`: List of file paths to the test volumes.
- `train_segmentations`: List of file paths to the training segmentation labels.
- `val_split`: The fraction of the dataset to reserve for validation (optional).

#### Description:

Organizes the dataset by moving files into the corresponding directories for training, validation, and testing.

### `generate_dataset_json()`

#### Description:

Generates a JSON file containing paths and labels for the training, validation, and testing sets according to the nnU-Net format.

### `prepare_dataset(train_volumes, test_volumes, train_segmentations, val_split)`

#### Parameters:

- `train_volumes`: List of file paths to the training volumes.
- `test_volumes`: List of file paths to the test volumes.
- `train_segmentations`: List of file paths to the training segmentation labels.
- `val_split`: The fraction of the dataset to reserve for validation (optional).

#### Description:

A high-level method that prepares the entire dataset by creating directories, organizing files, and generating the JSON file.

