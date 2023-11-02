# NIFTIVisualizer Documentation

The `NIFTIVisualizer` class in the PYCAD library provides a user-friendly approach to visualize one or multiple NIfTI files using the vedo library. With this class, users can conveniently visualize volumetric data in NIfTI format without dealing with the intricacies of plotting and colormap configurations.

## Introduction

`NIFTIVisualizer` is designed for those who require a simple method to visualize NIfTI files, especially in the context of medical imaging. This documentation delves into the class structure, its methods, and standard use cases.

## Class Definition

```Python
class NIFTIVisualizer:
```

## Initialization

```Python
def __init__(self, path_to_files, bg=(1,1,1), mesh_colors=None):
```

- **path_to_files**: List of paths to NIfTI files or a single path as a string.
- **bg** (optional): Background color defined as a tuple of RGB values. Default is white `(1,1,1)`.
- **mesh_colors** (optional): List of colormap names for each volume. If not given, random colormaps are generated.

## Public Methods

```
def visualize(self):
```

- Loads and visualizes the NIfTI volumes using the specified or generated colormaps.

## Example Usage

### Single NIfTI File

```
from pycad.visualization import NIFTIVisualizer

visualizer = NIFTIVisualizer("./data/sample1.nii")
visualizer.visualize()
```

### Multiple NIfTI Files with Custom Colors

```
paths = ["./data/sample1.nii", "./data/sample2.nii.gz"]
colors = ['viridis', 'inferno']
visualizer = NIFTIVisualizer(paths, mesh_colors=colors)
visualizer.visualize()
```

## Notes

- The class only accepts paths ending with `.nii` or `.nii.gz`. Any other file type will raise a `ValueError`.
- The number of provided colormaps should match the number of NIfTI file paths. If not, a `ValueError` will be thrown.
- A wide range of colormaps is available, including `'viridis'`, `'inferno'`, `'magma'`, and many more. If not specified, random colormaps are chosen for each NIfTI file.