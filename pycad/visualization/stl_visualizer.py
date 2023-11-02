# Copyright (c) 2023 PYCAD
# This file is part of the PYCAD library and is released under the MIT License:
# https://github.com/amine0110/pycad/blob/main/LICENSE


from vedo import load, show
import random


class STLVisualizer:
    """
    Class to visualize one or multiple STL files. Users can specify the path to a single STL file
    or provide multiple paths. Custom colors can also be assigned to the meshes.
    
    Example Usage:
    
    # Single STL file
    visualizer = STLVisualizer("./data/output_file.stl")
    visualizer.visualize()

    # Multiple STL files with custom colors
    paths = ['./data/multi_vis/hip_left.stl', './data/multi_vis/hip_right.stl']
    colors = ['#ffc800', '#aabcff']
    visualizer = STLVisualizer(paths, colors)
    visualizer.visualize()
    """
    
    def __init__(self, paths, colors=None, bg=(1,1,1)):
        # If a single path is provided, wrap it in a list for consistency
        if isinstance(paths, str):
            paths = [paths]

        self.paths = paths
        self.colors = colors if colors else self._generate_colors(len(paths))
        self.bg = bg
        
        if len(self.colors) < len(self.paths):
            raise ValueError(f"Number of colors provided ({len(self.colors)}) is less than the number of STL files ({len(self.paths)}).")

    @staticmethod
    def _generate_colors(count):
        """Generate random colors."""
        return ['#' + ''.join([random.choice('0123456789ABCDEF') for j in range(6)]) for i in range(count)]

    def visualize(self):
        meshes = []
        
        for path, color in zip(self.paths, self.colors):
            if not path.lower().endswith('.stl'):
                raise ValueError(f"File '{path}' is not an STL file.")
            
            mesh = load(path)
            mesh.color(color)
            meshes.append(mesh)

        # Display the meshes
        show(*meshes, bg=self.bg)