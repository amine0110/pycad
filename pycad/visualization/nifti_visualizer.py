# Copyright (c) 2023 PYCAD
# This file is part of the PYCAD library and is released under the MIT License:
# https://github.com/amine0110/pycad/blob/main/LICENSE


from vedo import Volume, show
import random
from glob import glob

class NIFTIVisualizer:
    """
    Class to visualize one or multiple NIfTI files. Provides the ability to specify a custom background 
    and mesh colors for each volume.
    
    Example Usage:
    ```
    # Visualize a single NIfTI file with default settings

    from pycad.visualization import NIFTIVisualizer
    
    visualizer = NIFTIVisualizer("./data/sample1.nii")
    visualizer.visualize()

    # Visualize multiple NIfTI files with custom colors
    paths = ["./data/sample1.nii", "./data/sample2.nii.gz"]
    colors = ['viridis', 'inferno']
    visualizer = NIFTIVisualizer(paths, mesh_colors=colors)
    visualizer.visualize()
    ```

    Parameters:
    - path_to_files: Either a single path or a list of paths to the NIfTI files.
    - bg: Background color as a tuple of RGB values.
    - mesh_colors: List of colormap names for each mesh. If not specified, random colormaps are generated.
    """
    
    def __init__(self, path_to_files, bg=(1,1,1), mesh_colors=None):
        # Convert single file path to a list for uniformity
        if isinstance(path_to_files, str):
            path_to_files = [path_to_files]

        for path in path_to_files:
            if not (path.lower().endswith('.nii') or path.lower().endswith('.nii.gz')):
                raise ValueError(f"File '{path}' is not a valid NIfTI file. Accepted extensions are .nii or .nii.gz.")
        
        self.path_to_files = path_to_files
        self.bg = bg
        self.mesh_colors = mesh_colors if mesh_colors else self._generate_colors(len(path_to_files))

        if len(self.mesh_colors) < len(self.path_to_files):
            raise ValueError("Number of provided colors is less than the number of NIfTI files.")
    
    @staticmethod
    def _generate_colors(count):
        """Generate random colormap names."""
        available_colormaps = ['Accent', 'Blues', 'BrBG', 'BuGn', 'BuPu', 'CMRmap', 'Dark2', 'GnBu', 'Greens',
                               'Greys', 'OrRd', 'Oranges', 'PRGn', 'Paired', 'Pastel1', 'Pastel2', 'PiYG', 'PuBu',
                               'PuBuGn', 'PuOr', 'PuRd', 'Purples', 'RdBu', 'RdGy', 'RdPu', 'RdYlBu', 'RdYlGn', 
                               'Reds', 'Set1', 'Set2', 'Set3', 'Spectral', 'Wistia', 'YlGn', 'YlGnBu', 'YlOrBr',
                               'YlOrRd', 'afmhot', 'autumn', 'binary', 'bone', 'brg', 'bwr', 'cividis', 'cool',
                               'coolwarm', 'copper', 'cubehelix', 'flag', 'gist_earth', 'gist_gray', 'gist_heat',
                               'gist_ncar', 'gist_rainbow', 'gist_stern', 'gist_yarg', 'gnuplot', 'gnuplot2', 
                               'gray', 'hot', 'hsv', 'inferno', 'jet', 'magma', 'nipy_spectral', 'ocean', 
                               'pink', 'plasma', 'prism', 'rainbow', 'seismic', 'spring', 'summer', 'tab10', 
                               'tab20', 'tab20b', 'tab20c', 'terrain', 'turbo', 'twilight', 'twilight_shifted', 
                               'viridis', 'winter']
        
        return random.sample(available_colormaps, count)

    def visualize(self):
        volumes = []
        for path, color in zip(self.path_to_files, self.mesh_colors):
            vol = Volume(path).cmap(color)
            volumes.append(vol)

        # Display the volumes
        show(*volumes, bg=self.bg)