# PngToTxtConverterML Documentation
![Data splitter](https://github.com/amine0110/pycad/blob/main/assets/pngtotxt.png?raw=true)

## Overview
The `PngToTxtConverterML` module provides utilities to convert PNG image masks to text files that store polygon coordinates. It is specifically designed to work with multiple labels where each subfolder in the input directory represents a different class.

## Classes

`PngToTxtConverterML`

**Description**

Converts PNG image masks into text files that store polygons. Designed to work with multi-label masks, where each subfolder in the input folder represents a different class.

### `__init__(self, input_folder, output_folder, epsilon_coeff=0.01)`

**Parameters**

- `input_folder`: Path to the folder containing subfolders for each class's mask images.
- `output_folder`: Path to the folder where generated .txt files will be saved.
- `epsilon_coeff`: Epsilon coefficient for contour approximation.

**Behavior**

Initializes class attributes and ensures the output directory exists.

### `binary_mask_to_yolo_polygon(self, binary_mask, class_index)`

**Parameters**

- `binary_mask`: Binary image mask for a single class.
- `class_index`: The index of the class.

**Returns**

A list of strings, each string represents a polygon for an object of class `class_index`.

**Behavior**

Generates polygons from the binary mask image and returns them.

### `run(self)`

**Behavior**

Processes image masks for each class in each subfolder and generates corresponding .txt files with polygons.

## Examples
To use the `PngToTxtConverterML` class, here is a sample code snippet:

```Python
from pycad.datasets import PngToTxtConverterML

input_folder = 'path/to/input/folder'
output_folder = 'path/to/output/folder'
epsilon_coeff = 0.01  # Example epsilon coefficient value

# Create an instance of the PngToTxtConverterML class
converter = PngToTxtConverterML(input_folder, output_folder, epsilon_coeff)

# Run the conversion
converter.run()
```

