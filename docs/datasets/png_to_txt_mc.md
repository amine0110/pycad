# PngToTxtConverterMC Module Documentation
![Data splitter](https://github.com/amine0110/pycad/blob/main/assets/pngtotxt.png?raw=true)

## Overview
This module provides the `PngToTxtConverterMC` class, which converts PNG image masks into text files containing polygon data. This class is particularly useful for multi-class object detection tasks, where each image mask may contain multiple object classes.

## Classes
### `PngToTxtConverterMC`

**Description**
The `PngToTxtConverterMC` class is designed to convert multi-class image masks in PNG format to text files that contain polygons representing the shapes in the image masks.

#### `__init__(self, input_folder, output_folder, epsilon_coeff=0.001)`

**Parameters**

- `input_folder`: String, represents the path to the directory where the image masks in PNG format are stored.
- `output_folder`: String, represents the directory where the generated text files will be saved.
- `epsilon_coeff`: Float, optional, default is 0.001. This is the epsilon coefficient used for contour approximation in OpenCV's `cv2.approxPolyDP()` method.

**Behavior**

Initializes the attributes of the class and ensures that the output directory exists. If it doesn't, it will be created.

#### `multi_class_mask_to_yolo_polygons(self, mask, classes=[0, 1, 2])`

**Parameters**

- **mask**: NumPy array, the image mask containing different classes represented as different integer values.
- **classes**: List of integers, default is `[0, 1, 2]`. These are the classes that will be extracted from the mask.

**Returns**

Returns a list of strings, where each string represents a polygon corresponding to an object of a particular class.

**Behavior**

Processes the multi-class mask image to extract polygons. This method utilizes OpenCV's `cv2.findContours()` and `cv2.approxPolyDP()` methods for contour detection and approximation, respectively.

#### `run(self)`

**Behavior**

Iterates through all image masks in the `input_folder`, converts them to polygon data, and saves the polygons to text files in the `output_folder`.

## Example Usage

```Python
from pycad.datasets import PngToTxtConverterMC

input_folder = 'path/to/mask_images'
output_folder = 'path/to/output_txt_files'
epsilon_coeff = 0.001

converter = PngToTxtConverterMC(input_folder, output_folder, epsilon_coeff)
converter.run()
```