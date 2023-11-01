# Converters in PYCAD

Welcome to the converters folder! This package is part of the PYCAD library, designed to provide you with powerful utilities for converting medical imaging data. We currently support three types of conversions:

1. NIFTI to STL (`Nifti2StlConverter`)
2. NIFTI to PNG (`NiftiToPngConverter`)
3. NIFTI to DICOM (`NiftiToDicomConverter`)

## Installation
To install the PYCAD library, run the following command:

```bash
git clone https://github.com/amine0110/pycad
```

## Getting Started
First, make sure to import the required converter class:

```Python
from pycad.converters import Nifti2StlConverter, NiftiToPngConverter, NiftiToDicomConverter
```

## Usage
Here is a brief rundown of how to use each converter.

#### **Nifti2StlConverter**

Converts NIFTI files to STL for 3D printing or further processing. Supports single and multi-class conversions.

[Detailed Documentation](https://github.com/amine0110/pycad/blob/main/docs/converters/nifti_to_stl.md)

#### **NiftiToPngConverter**

Converts NIFTI files to PNG images for easy visualization and sharing.

[Detailed Documentation](https://github.com/amine0110/pycad/blob/main/docs/converters/nifti_to_png.md)

#### **NiftiToDicomConverter**

Converts NIFTI files to DICOM for compatibility with most of the medical imaging software.

[Detailed Documentation](https://github.com/amine0110/pycad/blob/main/docs/converters/nifti_to_dicom.md)

## File Types
- ***NIFTI***: Mostly used for storing volumetric data and meta-information. Common in research settings.
- ***STL***: Stereolithography format, widely used for 3D printing and CAD software.
- ***PNG***: Standard image format for lossless compression.
- ***DICOM***: Standard for the communication and management of medical imaging information and related data.

## Contributing
If you would like to contribute, please fork the repository and use a feature branch. Pull requests are welcome.

## Contact
For more details about PYCAD and our suite of tools, please visit [PYCAD Website](https://pycad.co/)