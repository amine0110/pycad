# DicomToNrrdConverter Documentation

## Module Overview
The `DicomToNrrdConverter` is a utility class within the PYCAD library that facilitates the conversion of DICOM image series to NRRD files. This can be applied to individual patient scans or bulk-converted for multiple patients, each containing a series of DICOM images.

## Usage
The module is designed for flexibility, allowing users to specify the minimum number of images per series to be considered for conversion. This is particularly useful to avoid attempting to convert directories with insufficient data, which cannot form a complete NRRD file.

## Initialization

```Python
from pycad.converters import DicomToNrrdConverter

# Initialize the converter with a specific minimum number of images required for a valid series.
converter = DicomToNrrdConverter(min_images_per_series=10)
```

## Conversion Process
To perform the conversion process, the user must specify the input directory (containing one or more DICOM series) and the output directory (where the NRRD files will be saved).

```Python
input_dir = "path/to/input/folder"
output_dir = "path/to/output/folder"

# Execute the conversion from DICOM to NRRD
converter.convert(input_dir, output_dir)
```

## Class Methods
### `__init__(self, min_images_per_series=5)`
Initializes a new instance of the `DicomToNrrdConverter` class.

#### Parameters:
- `min_images_per_series` (int): The minimum number of DICOM images to consider a directory a valid series for conversion.

### `find_dicom_series(self, root_dir)`
Searches for DICOM series within the given directory, subject to the `min_images_per_series` constraint.

#### Parameters:
- `root_dir` (str): The path to the directory to search for DICOM series.

#### Returns
A list of tuples, each containing the path to a series directory and a list of DICOM file paths within it.

### `convert_series_to_nrrd(self, dicom_series, output_path)`
Converts a specified DICOM series to an NRRD file.

#### Parameters:
- `dicom_series` (tuple): A tuple containing the directory path and list of DICOM files that form a series.
- `output_path` (str): The directory where the NRRD file will be saved.

#### Behavior
The method attempts to read the series of DICOM images and convert them into a single NRRD file, with the output file's name based on the DICOM series directory name and a random identifier.

### `convert(self, input_dir, output_dir)`
Conducts the conversion of all valid DICOM series found in the input_dir to NRRD files, which are saved in the `output_dir`.

#### Parameters:
- `input_dir` (str): The directory where the DICOM series are located.
- `output_dir` (str): The directory where the converted NRRD files will be saved.

## Error Handling and Logging
The class is equipped with a logger to handle and report information, warnings, and errors during the conversion process. It logs the status of each conversion attempt, providing feedback on the process's success or failure.

## License
This module is part of the PYCAD library and is released under the MIT License. The license can be reviewed at the official [PYCAD GitHub repository](https://github.com/amine0110/pycad/blob/main/LICENSE).