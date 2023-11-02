# Visualization in PYCAD
Welcome to the `visualization` submodule of PYCAD. This submodule is meticulously designed to offer a simple and intuitive interface for visualizing various data types common in medical imaging and computational design. From standard file formats like STL and NIfTI to more advanced data structures, this submodule is tailored to make visualization a breeze.

## Features

1. **Versatile Visualization**: The ability to handle various file formats and data structures, ensuring you have the tools needed for diverse visualization tasks.
2. **Customization**: From background colors to colormap configurations, the visualization tools offer a plethora of customization options to make the plots truly yours.
3. **Integrated with Major Libraries**: Built upon trusted libraries like vedo, our submodule ensures reliability while providing additional utility functions.
4. **Interactive Visualization**: Some tools within this submodule offer interactive visualization capabilities, allowing for detailed exploration of datasets.
5. **Expandable**: As the field of medical imaging grows, so will this submodule. It's architected to be easily expandable to accommodate new visualization techniques and formats.

## Quick Start

While specific instructions might differ based on the exact visualization tool you're using, here's a general guide to get started:

### 1. Importing the Necessary Tool:

```Python
from pycad.visualization import NIFTIVisualizer
```

### 2. Initialization:

```Python
visualizer = NIFTIVisualizer(files)
```

### 3. Visualization:

```Python
visualizer.visualize()
```

Visit individual tool documentation for more detailed guidelines and examples.

## Available Tools

- **STLVisualizer**: For visualizing STL files with options for multiple files and color customizations.
- **NIFTIVisualizer**: Offers the ability to visualize NIfTI files, supporting both single and multiple file visualizations with customizable colormaps.
- ... (more tools can be listed as they are added)

## Contribution & Feedback

We're always looking to improve and expand the capabilities of the visualization submodule. If you have suggestions, feedback, or want to contribute directly to its development, please visit our [GitHub repository](https://github.com/amine0110/pycad).

## License
This submodule, as with all parts of PYCAD, is released under the MIT License. See the [license file](https://github.com/amine0110/pycad/blob/main/LICENSE) for more details.