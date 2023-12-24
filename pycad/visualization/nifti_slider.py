# Copyright (c) 2023 PYCAD
# This file is part of the PYCAD library and is released under the MIT License:
# https://github.com/amine0110/pycad/blob/main/LICENSE


import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

class NiftiSlider:
    '''
    This module is for NIfTI visualization using Python and Matplotlib. This is a simple way of doing the visualization for the axial, coronal, and sagittal views.

    ### Example usage
    ```Python
    from pycad.visualization import NiftiSlider

    nifti_file_path = 'path to the nifti file'
    NiftiSlider(nifti_file_path)
    ```
    '''
    def __init__(self, filepath):
        self.filepath = filepath
        self.image_data = self.load_nifti_file(filepath)
        self.current_view = 'axial'  # Define the current_view before setting up slider
        self.fig, self.ax = plt.subplots()
        plt.subplots_adjust(left=0.25, bottom=0.35)
        self.setup_slider()  # Now self.current_view is defined before this call
        self.display_slice(0)
        plt.show()

    def load_nifti_file(self, filepath):
        nifti = nib.load(filepath)
        image_data = nifti.get_fdata()
        return image_data

    def display_slice(self, index):
        if self.current_view == 'axial':
            slice = self.image_data[:, :, index]
        elif self.current_view == 'coronal':
            slice = self.image_data[:, index, :]
        elif self.current_view == 'sagittal':
            slice = self.image_data[index, :, :]
        
        # Update the image
        if not hasattr(self, 'image'):
            self.image = self.ax.imshow(slice.T, cmap='gray', origin='lower')
        else:
            self.image.set_data(slice.T)
        plt.draw()

    def update_slider(self, val):
        self.display_slice(int(val))

    def setup_slider(self):
        # Adjust the slider's max value based on the current view
        if self.current_view == 'axial':
            max_slice = self.image_data.shape[2] - 1
        elif self.current_view == 'coronal':
            max_slice = self.image_data.shape[1] - 1
        else:  # sagittal
            max_slice = self.image_data.shape[0] - 1

        ax_slider = plt.axes([0.25, 0.1, 0.65, 0.03])
        self.slider = Slider(ax_slider, 'Slice', 0, max_slice, valinit=0, valfmt='%0.0f')
        self.slider.on_changed(self.update_slider)

    def change_view_axial(self, event):
        self.current_view = 'axial'
        self.setup_slider()
        self.display_slice(0)

    def change_view_coronal(self, event):
        self.current_view = 'coronal'
        self.setup_slider()
        self.display_slice(0)

    def change_view_sagittal(self, event):
        self.current_view = 'sagittal'
        self.setup_slider()
        self.display_slice(0)