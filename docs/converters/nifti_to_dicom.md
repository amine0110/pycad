# NiftiToDicomConverter Documentation
![Nifti to dicom](https://github.com/amine0110/pycad/blob/main/assets/nifti2dcm_diagram.svg?raw=true)

## Theoretical Background

### What are NIFTI and DICOM Formats?

***NIFTI (Neuroimaging Informatics Technology Initiative)*** is a file format commonly used in the field of medical imaging. It's popular in research environments and is known for its capability to store a rich set of metadata along with the imaging data.

***DICOM (Digital Imaging and Communications in Medicine)*** is a standard commonly used for transmitting, storing, and sharing medical images. Unlike NIFTI, DICOM is widely used in clinical settings.

### Why Convert?
- **Compatibility**: Many medical imaging software do not support the NIFTI format but will support DICOM.

- **Metadata**: DICOM can carry a vast amount of metadata which is useful in clinical settings.

- **Standardization**: DICOM is the standard format in medical imaging making it essential for sharing data across different platforms and systems.

### Conversion Complexity
Converting a NIFTI file to a DICOM series involves:

- Reading the NIFTI file and extracting the imaging data.

- Rescaling image intensities.

- Mapping the metadata from the NIFTI file to DICOM tags.

- Writing each slice of the 3D image as a separate DICOM file with appropriate metadata.

---
## Module Documentation: `NiftiToDicomConverter`
### Overview

`NiftiToDicomConverter` is a Python class designed for converting NIFTI files to DICOM format. It can convert a single or multiple NIFTI files and saves each slice of the 3D image as a separate DICOM file.

### Class Initialization

```
from pycad.converters import NiftiToDicomConverter

converter = NiftiToDicomConverter()
```
No parameters are needed for initialization.

### Methods
`writeSlices(series_tag_values, new_img, i, out_dir)`

#### Parameters:
- `series_tag_values`: List of tuples containing DICOM metadata tags and their corresponding values.

- `new_img`: SimpleITK Image object representing the 3D image to be written.

- `i`: Index of the current slice to be written.

- `out_dir`: Directory where the DICOM files will be saved.

#### Description:

This is an internal helper function and is generally not called directly by the user. It takes a slice of a 3D image and writes it as a DICOM file. The metadata for the DICOM file is taken from `series_tag_values`.

`nifti2dicom_1file(in_dir, out_dir)`

#### Parameters:

`in_dir`: File path of the input NIFTI file.

`out_dir`: Directory where the DICOM files will be saved.

#### Description:

Converts a single NIFTI file into a series of DICOM files. Each slice of the 3D image is saved as a separate DICOM file in the directory specified by `out_dir`.

`nifti2dicom_mfiles(nifti_dir, out_dir)`

#### Parameters:

`nifti_dir`: Directory containing multiple NIFTI files.

`out_dir`: Directory where the DICOM files will be saved.

#### Description:

Converts multiple NIFTI files into DICOM series. The method iteratively calls `nifti2dicom_1file` for each NIFTI file in the directory specified by `nifti_dir`. Each converted DICOM series is saved in a separate folder under `out_dir`.