# What is new in the release?
This section will contain all the updates and the new features from the latest release of the library. So whenever a new release of the library is released then this documentation will be updated with the latest features only.

# Features
Here is a list of features that are available in the release `0.0.9`:
- Replaced the DataSplitter from sklearn based module to a very custom implementation.
- Added a unit test for the DataSplitter module.
- DICOM Slider for 2D visualization of CT, MRI, PET,...
- NIFTI Slider for 2D visualization of CT, MRI, PET,...
- The mandible segmentation tutorial with a Google Colab implementation.

## DataSplitter
When doing multiple tests on the DataSplitter module that was based on sklearn, we found some issues with the data sorting (especially in Google Colab). For this reason we decided to create our custom implementation of the DataSplitter module. Now you can create train/valid/test folders with the images and labels subfolders with easier ways. The module can be accessed [here](../pycad/datasets/data_splitter.py) and the example of usage is included in the doucmentation.

## DataSplitter Unittest
As a good practise, it is recommended to create a unittest for each module of the library. For this reason we started by the module DataSplitter since it was causing issues in the data sorting. You can access and use this unittest [here](../pycad/unittests/data_splitter_unittest.py).

## DICOM Slider / NIFTI Slider
For multiple reasons, we may need a built-in DICOM/NIFTI viewer so that we can use it to test the different operations using the `pycad` library. So you can test your operations from now directly using pycad.visualization module, for example when you apply windowing to a CT scan or MRI, you can visualize the difference.

## Tutorial
The mandible segmentation tutorial is now accessible through Google Colab, where it is simple and easy for the beginners. You will see that it is direct to the point and it doesn't require a lot of knowledge to understand the tutorial, and the goal of this tutorial is to show you how to use the pycad library to prepare your dataset for training a 2D segmentation model using YOLOv8. The tutrial can be found [here](../tutorials/pycad_yolov8.ipynb).

![mandible](../assets/panoramic_prediction.png)