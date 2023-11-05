# DicomToNiftiConverter Documentation

## Overview
Medical imaging often requires the conversion of image data from one format to another to support various analysis tasks or to prepare data for different visualization tools. The `DicomToNiftiConverter` module within the PYCAD library facilitates the conversion of DICOM series to the NIfTI format. This is a sophisticated conversion utility capable of handling various organizational structures of DICOM files.

## Why NIfTI?
The Neuroimaging Informatics Technology Initiative (NIfTI) format is widely used in medical imaging and neuroimaging, as it allows for the storage of 3D medical imaging data along with the spatial information necessary to understand orientation and position within a given space. Converting DICOM series, which are typically individual slices, into a 3D NIfTI volume can greatly assist in the processing and analysis of medical imaging data. To know the difference between NIFTI and DICOMs, you can check out our blog post [here](https://pycad.co/what-is-the-difference-between-dicom-and-nifti-images/).

## Features
- Recursive search through directories for DICOM series.
- Conversion of series from folders or nested folders.
- Sophisticated handling of varying directory structures.
- Filtering of series based on a minimum number of images.
- Randomized output filename generation for confidentiality.
- Logging of conversion process and error handling.

## Installation
To use the DicomToNiftiConverter, ensure that you have the latest version of the PYCAD library installed. For more inf about the installation please see the [doc here](../getting_started.md).

## Usage
### Basic Conversion
Here is an example of how to use the DicomToNiftiConverter to convert DICOM series to NIfTI files:

```Python
from pycad.converters import DicomToNiftiConverter

# Specify the input directory containing DICOM series and the output directory for NIfTI files
input_dir = "/path/to/dicom_series"
output_dir = "/path/to/nifti_output"

# Create the converter instance with a minimum of 10 images per series
converter = DicomToNiftiConverter(min_images_per_series=10)

# Perform the conversion
converter.convert(input_dir, output_dir)
```

### Directory Structure Handling
The `DicomToNiftiConverter` is capable of handling the following directory structures:

- Single folder with DICOM files.
- Multiple folders each with their own series of DICOM files.
- Nested folders with multiple levels, each potentially containing DICOM series.

Regardless of the directory structure, as long as the subdirectory contains the minimum required number of DICOM images as specified by `min_images_per_series`, it will be processed.

## Logging
The module provides detailed logging throughout the conversion process, which can be viewed in real-time. This includes information logs upon successful conversions and error logs when conversions fail.

# FAQs
Q: Can the converter handle mixed file types in the source directory?\n
A: Yes, it filters and processes only .dcm files.\n
\n
Q: Is there a limit to the number of series that can be converted at once?\n
A: No, the converter will process all valid series it discovers within the input directory structure.\n

## Contact and Support
For support with the `DicomToNiftiConverter` or any other aspects of the PYCAD library, please reach out through [contact options on the official website](https://pycad.co/contact/).

For reporting issues or contributing to the library, please visit the [GitHub repository](https://github.com/amine0110/pycad).

## Conclusion
The `DicomToNiftiConverter` is a powerful tool for researchers and professionals in the medical imaging field, simplifying the process of converting DICOM image series to the versatile NIfTI format. With its recursive searching capabilities and robust error handling, it is designed to be a reliable component in your image processing pipeline.