# NrrdToDicomConverter Documentation

The `NrrdToDicomConverter` class is designed to facilitate the conversion of NRRD (Nearly Raw Raster Data) files into DICOM (Digital Imaging and Communications in Medicine) series. This conversion is crucial in the medical imaging field where DICOM is the standard for handling, storing, processing, and transmitting medical images.

## Features
- **Single File Conversion**: Convert a single NRRD file into a DICOM series with a designated output directory for the generated series.
- **Multiple Files Conversion**: Batch convert multiple NRRD files into their corresponding DICOM series within an output directory, with each series placed in its respective folder.

## Usage

### Convert a Single NRRD File
```python
from pycad.converters import NrrdToDicomConverter

# Paths to the input NRRD file and the output directory
in_dir = 'path/to/nrrd/file'
out_dir = 'path/to/output/dicom/series'

# Create an instance of the converter
converter = NrrdToDicomConverter()

# Perform the conversion
converter.nrrd2dicom_1file(in_dir, out_dir)
```

### Convert Multiple NRRD Files

```Python
from pycad.converters import NrrdToDicomConverter

# Directory containing multiple NRRD files
nrrd_dir = 'path/to/nrrd/files'
# Output directory to store the DICOM series
out_dir = 'path/to/output/dicom/series'

# Create an instance of the converter
converter = NrrdToDicomConverter()

# Perform the batch conversion
converter.nrrd2dicom_mfiles(nrrd_dir, out_dir)
```

## Methods
### `writeSlices`
A utility function to write each slice of the image with appropriate DICOM metadata.

#### Parameters:

- `series_tag_values`: List of tuples with DICOM tags and their values.
- `new_img`: The SimpleITK image object that is being written as slices.
- `i`: Index of the slice in the series.
- `out_dir`: Output directory for the DICOM files.

### `nrrd2dicom_1file`
Converts a single NRRD file to a DICOM series.

#### Parameters:

- `in_dir`: Path to the NRRD file.
- `out_dir`: Output directory for the DICOM series.

### `nrrd2dicom_mfiles`
Batch converts multiple NRRD files to DICOM series and stores them in the provided output directory.

#### Parameters:

- `nrrd_dir`: Directory containing the NRRD files to be converted.
- `out_dir`: Output directory to store the resulting DICOM series.

## License
This module is part of the PYCAD library and is released under the MIT License. The full license text is available at the [PYCAD GitHub repository](https://github.com/amine0110/pycad/blob/main/LICENSE).