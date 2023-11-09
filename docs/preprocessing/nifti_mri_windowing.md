# NiftiMriWindowing Documentation

## Overview
The `NiftiMriWindowing` module from the PYCAD library provides a way to enhance the contrast of medical imaging scans, specifically MRI or CBCT, by applying a windowing technique. This technique is especially beneficial for scans with low contrast where the details are not distinctly visible. The module accepts NIfTI format images as input and outputs the windowed images in the same format.

## How It Works
The windowing process involves adjusting the range of pixel intensities that are displayed in the image. By doing this, the contrast within a specified range of interest is enhanced, which can make the important structures in medical images more discernible. This module calculates the window based on the image's mean and standard deviation of intensities, which is then scaled to the full display range.

## Installation
Ensure you have the PYCAD library installed, which includes this module.

## Usage
Here is an example of how to use the `NiftiMriWindowing` module:
```python
from pycad.preprocessing import NiftiMriWindowing

input_filepath = './path/to/input/image.nii'
output_filepath = './path/to/output/windowed_image.nii'
windower = NiftiMriWindowing(input_filepath, output_filepath)
windower.window_image(coef=4)

```
## Parameters
-   `input_filepath`: Path to the input NIfTI file (.nii or .nii.gz)
-   `output_filepath`: Path to the output NIfTI file (.nii or .nii.gz)
-   `coef` (optional in `window_image` method): A coefficient that determines the window range. Higher values increase the window size, which includes more intensities but reduces contrast.
## Methods
### `__init__(self, input_filepath, output_filepath)`
Constructor for the `NiftiMriWindowing` class.

### `load_image(self)`
Loads the NIfTI image from the specified input file path.

### `apply_windowing(self, image, coef=4)`
Applies windowing to the loaded NIfTI image data using the specified coefficient.

### `save_image(self, image)`
Saves the windowed image to the specified output file path.

### `window_image(self, coef=4)`
Coordinates the loading, windowing, and saving of the NIfTI image.

## Dependencies
-   nibabel
-   numpy
-   os
-   tqdm

## Error Handling
The module includes basic error handling that reports back to the user when an image fails to load or save.

## Conclusion
The `NiftiMriWindowing` module is a simple yet powerful tool for enhancing the visibility of structures in MRI and CBCT scans, making it a valuable addition to the preprocessing steps in medical image analysis workflows.

## License
This module is part of the PYCAD library and is released under the MIT License. For more details, see the [LICENSE](https://github.com/amine0110/pycad/blob/main/LICENSE) file.