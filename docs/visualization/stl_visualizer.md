# STLVisualizer Documentation

The `STLVisualizer` class in the PYCAD library provides a convenient interface to visualize one or more STL files using the vedo library. With it, users can easily visualize complex 3D meshes from STL files, either with default or custom colors.

## Introduction

`STLVisualizer` is particularly useful when there is a need to quickly visualize 3D meshes from STL files without the overhead of configuring and managing individual plots and color schemes. This documentation provides a complete overview of the class, including its methods and typical usage scenarios.

## Class Definition

```Python
class STLVisualizer:
```

## Initialization

```Python
def __init__(self, paths, colors=None, bg=(1,1,1)):
```

- **paths**: List of paths to STL files or a single path as a string.
- **colors** (optional): List of colors corresponding to each STL file path. If not provided, random colors are generated.
- **bg** (optional): Background color for the visualization. Default is white `(1,1,1)`.

## Public Methods

```Python
def visualize(self):
```

- Loads and visualizes the STL meshes using the provided or generated colors.

## Example Usage

### Single STL File

```Python
from pycad.visualization import STLVisualizer

visualizer = STLVisualizer("./data/file.stl")
visualizer.visualize()
```

### Multiple STL Files with Custom Colors

```Python
paths = ['./data/multi_vis/hip_left.stl', './data/multi_vis/hip_right.stl']
colors = ['#ffc800', '#aabcff']
visualizer = STLVisualizer(paths, colors)
visualizer.visualize()
```

## Notes

- The number of colors provided should match the number of STL file paths. Otherwise, a `ValueError` will be raised.
- Only paths ending with `.stl` are accepted. If a different file type is provided, a `ValueError` will be raised.
