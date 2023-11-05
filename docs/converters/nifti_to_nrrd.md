# NiftiToNrrdConverter Documentation

The `NiftiToNrrdConverter` module is a versatile and efficient conversion tool in the PYCAD library, designed to transform neuroimaging data stored in the NIFTI format (.nii or .nii.gz) into the NRRD format. This conversion is essential for researchers and practitioners in medical imaging and computer vision fields who require a consistent data format for preprocessing, analysis, or machine learning model training.\n
\n
NIFTI (Neuroimaging Informatics Technology Initiative) is a widely adopted format for storing MRI data, while NRRD (Nearly Raw Raster Data) is a format that is often preferred for its flexibility and ease of use in certain applications, such as volume rendering and handling of multi-dimensional datasets.

## Key Features:
- **Flexibility**: Handles individual files as well as batches of files located within a directory.
- **Ease of Use**: The module provides a straightforward and clear API with logging support for tracking the conversion process.
- **Versatility**: Can be easily integrated into data processing pipelines for automated batch processing.

## Usage:
Here’s a simple example of how to use the `NiftiToNrrdConverter`:

```Python
from pycad.converters import NiftiToNrrdConverter

# Initialize converter
converter = NiftiToNrrdConverter()

# Specify the path to the input NIFTI file or directory containing multiple files
input_path = "path/to/input/file/or/dir"

# Specify the output directory to store the converted NRRD files
output_dir = "path/to/output/directory"

# Perform the conversion
converter.convert(input_path, output_dir)
```

This code will handle both single file and directory inputs, ensuring all NIFTI files found are converted to the NRRD format.

## Functions:
### `__init__(self)`

Initializes the converter and sets up logging to monitor the conversion process.

### `convert(self, input_path, output_dir)`

The primary method called to perform the conversion. It detects whether the input path is a file or directory and calls the appropriate method to handle the conversion.

### `convert_file(self, input_file_path, output_dir)`

Converts a single NIFTI file to an NRRD file. It is called internally by `convert()` if the input path is a file.

### `convert_directory(self, input_dir, output_dir)`

Converts all NIFTI files found in the specified directory to NRRD files. It is called internally by `convert()` if the input path is a directory.

## Why is NIFTI to NRRD Conversion Important?

- **Compatibility**: Some software tools and libraries prefer NRRD over other formats, making this conversion crucial for compatibility.
- **Preservation of Metadata**: NRRD format is designed to store detailed metadata, which is vital for some analysis tasks.
- **Multi-Dimensional Data Support**: NRRD is well-suited for multi-dimensional data, which is common in medical imaging applications.

## Conclusion
The `NiftiToNrrdConverter` module is an integral part of the PYCAD library, adding to its robust suite of tools for medical imaging. By simplifying the conversion process, it aids researchers and developers in streamlining their workflows and ensuring data consistency across different stages of their projects.