# NiftiToPngConverter Documentation
![Nifti to dicom](https://github.com/amine0110/pycad/blob/main/assets/nifti2png_diagram.svg?raw=true)

## Introduction
The `NiftiToPngConverter` class is designed to convert medical images from the NIFTI format to PNG images. This class is a part of the `pycad` library and can be particularly useful in preprocessing steps for machine learning models that use medical images.

Important: Before performing the conversion, please check the values of `max_v` and `min_v` to properly window the Hounsfield Units. For more information, consult this [video](https://youtu.be/prLnvOg1ckU?si=TI1ugbqplWnPLrSx).

## Installation
To use this class, make sure to import it as follows:

```Python
from pycad.converters import NiftiToPngConverter
```

## Usage
Initialize the NiftiToPngConverter class with optional parameters for the Hounsfield window (`max_v` and `min_v`).

```Python
converter = NiftiToPngConverter(max_v=200, min_v=-200)
```

## Methods
### `__init__(max_v=200, min_v=-200)`

Initializes the converter object.

- `max_v`: The maximum Hounsfield Unit for windowing. Default is 200.
- `min_v`: The minimum Hounsfield Unit for windowing. Default is -200.

### `prepare_image(image_data, data_type='vol')`

Prepares the image data for conversion. This function normalizes the images based on the provided Hounsfield window.

- `image_data`: The image data in numpy array form.
- `data_type`: Either 'vol' for volume or 'seg' for segmentation.

### `convert_nifti_to_png(in_dir, out_dir, data_type)`

Converts a single NIFTI file into PNG images. Images are saved in the specified output directory.

- `in_dir`: The directory containing the input NIFTI file.
- `out_dir`: The directory to save the output PNG files.
- `data_type`: Either 'vol' for volume or 'seg' for segmentation.

### `convert_nifti_to_png_dir(in_dir, out_dir, data_type)`

Converts multiple NIFTI files in a directory into PNG images.

- `in_dir`: The directory containing the input NIFTI files.
- `out_dir`: The directory to save the output PNG files.
- `data_type`: Either 'vol' for volume or 'seg' for segmentation.

### `run(in_dir_vol=None, in_dir_seg=None, out_dir=None)`

The main function to perform the conversion for both volumes and segmentations.

- `in_dir_vol`: The directory containing the volume NIFTI files.
- `in_dir_seg`: The directory containing the segmentation NIFTI files.
- `out_dir`: The directory to save the output PNG files.

## Examples
### Example 1: Converting a Single NIFTI File

```Python
# Initialize the converter
converter = NiftiToPngConverter(max_v=200, min_v=-200)

# Convert a single NIFTI file to PNG
converter.convert_nifti_to_png('path/to/nifti/file', 'path/to/output/dir', 'vol')
```

### Example 2: Converting Multiple NIFTI Files

```Python
# Initialize the converter
converter = NiftiToPngConverter(max_v=200, min_v=-200)

# Convert multiple NIFTI files to PNG
converter.convert_nifti_to_png_dir('path/to/nifti/directory', 'path/to/output/dir', 'vol')
```