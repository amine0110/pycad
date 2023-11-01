# Nifti2StlConverter Documentation
![Nifti to dicom](https://github.com/amine0110/pycad/blob/main/assets/nifti2stl.png?raw=true)

## Introduction
The `Nifti2StlConverter` is a specialized class designed for converting medical images from NIFTI (Neuroimaging Informatics Technology Initiative) format to STL (STereoLithography) format. These two formats serve different purposes in the field of medical imaging, and their interoperability is crucial for various applications, such as 3D printing, surgical planning, and more.

## NIFTI vs STL: What's the Difference?

### NIFTI:
- **File Format**: NIFTI is primarily used for storing volumetric images.
- **Data Structure**: It handles 3D or 4D arrays.
- **Metadata**: Includes a rich set of metadata, including spatial orientation, dimensions, and voxel sizes.
- **Applications**: Mainly used in MRI, CT scans, and other medical imaging modalities.

### STL:
- **File Format**: STL is used for representing 3D surface geometry.
- **Data Structure**: It describes only the surface geometry of a three-dimensional object without any representation of color, texture, or other common CAD model attributes.
- **Metadata**: Minimal to none.
- **Applications**: Widely used in 3D printing, computer simulations, and computer-aided design.

## Why Convert NIFTI to STL?
1. **3D Visualization**: STL files can be easily visualized, manipulated, and printed in 3D.
2. **Surgical Planning**: STL files can be used to produce physical 3D models for surgical planning.
3. **Data Simplification**: While NIFTI files contain more information, STL files can be simpler to work with for specific applications.

## Methods Overview

### `nifti2stl_vtk()`
- **Purpose**: Converts a single NIFTI file to an STL file using VTK.
- **Output**: All classes in the NIFTI file will be considered as one single class and color.
- **Additional Parameters**: None.

### `nifti2stl_vedo()`
- **Purpose**: Converts a single NIFTI file to one or multiple STL files using Vedo.
- **Output**: Creates separate STL files based on the number of classes present in the NIFTI file.
- **Additional Parameters**: None.

### `nifti2stl_vtk_multi_class()`
- **Purpose**: Converts a single NIFTI file to one or multiple STL files using VTK.
- **Output**: Allows customization for mesh smoothing and size reduction.
- **Additional** Parameters:
    - *smoothing*: Boolean flag for mesh smoothing.
    - *reduce_meshes*: Boolean flag for reducing mesh size.
    - *number_of_iterations*: Integer specifying the number of iterations for smoothing (default is 50).
    - *percent_reductions*: Float specifying the percentage for mesh size reduction (default is 0.5).

## Usage

Here's how you can use the `Nifti2StlConverter` in your project:

```Python
from pycad.converters import Nifti2StlConverter

# Initialize the converter
converter = Nifti2StlConverter('path/to/nifti/file', 'path/to/output/dir')

# Using VTK for a single-class conversion
converter.nifti2stl_vtk()

# Using Vedo for multi-class conversion
converter.nifti2stl_vedo()

# Using VTK for multi-class conversion with custom smoothing and mesh reduction
converter.nifti2stl_vtk_multi_class(smoothing=True, reduce_meshes=True, number_of_iterations=50, percent_reductions=0.5)
```