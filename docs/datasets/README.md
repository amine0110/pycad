# Datasets in PYCAD
This folder contains various utilities for preprocessing medical imaging data, particularly for YOLO-based object detection models. These utilities help in splitting datasets, converting mask images to YOLO polygon formats, and generating the required `dataset.yaml` files.

## DataSplitter

### Description
This utility is designed to split a dataset into training, validation, and testing sets based on a user-defined ratio.

[Detailed Documentation](https://github.com/amine0110/pycad/blob/main/docs/datasets/data_splitter.md).

## PngToTxtConverterMC

### Description
This utility converts single-class PNG mask images into text files containing polygons suitable for YOLO models.

[Detailed Documentation](https://github.com/amine0110/pycad/blob/main/docs/datasets/png_to_txt_mc.md).

## PngToTxtConverterML

### Description
Designed for multi-label mask images, this utility converts PNG masks into text files containing polygons suitable for YOLO models.

[Detailed Documentation](https://github.com/amine0110/pycad/blob/main/docs/datasets/png_to_txt_ml.md).

## YOLODatasetYaml

### Description
This utility generates a dataset.yaml file required for training YOLOv8 models. It includes paths for training and validation data, the number of classes, and the names of those classes.

[Detailed Documentation](https://github.com/amine0110/pycad/blob/main/docs/datasets/yolo_dataset_yaml.md).