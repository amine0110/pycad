# Copyright (c) 2023 PYCAD
# This file is part of the PYCAD library and is released under the MIT License:
# https://github.com/amine0110/pycad/blob/main/LICENSE


import pydicom
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

class DicomSlider:
    '''
    This module is for DICOM visualization using Python and Matplotlib. This is a simple way of doing the visualization for the axial, coronal, and sagittal views.

    ### Example usage
    ```Python
    from pycad.visualization import DicomSlicer

    dicom_directory = 'path to the dicom folder'
    DicomSlider(dicom_directory)
    ```
    '''
    def __init__(self, directory, force=False):
        self.directory = directory
        self.slices, self.pixel_spacing = self.load_dicom_series(directory, force=force)
        self.current_view = 'axial'  # default view
        self.image_stack = self.build_image_stack(self.slices, self.pixel_spacing)
        self.fig, self.ax = plt.subplots()
        plt.subplots_adjust(left=0.25, bottom=0.35)
        self.setup_slider()
        self.setup_buttons()
        self.display_slice(0)
        plt.show()

    def load_dicom_series(self, directory, force=False):
        dicom_images = []
        for filename in os.listdir(directory):
            if filename.endswith('.dcm'):
                ds = pydicom.dcmread(os.path.join(directory, filename), force=force)
                dicom_images.append(ds)
        # Assuming all images have the same pixel spacing and checking for SliceThickness
        pixel_spacing = dicom_images[0].PixelSpacing
        slice_thickness = getattr(dicom_images[0], 'SliceThickness', pixel_spacing[0])  # Fallback to pixel spacing if SliceThickness is missing
        pixel_spacing.append(slice_thickness)
        dicom_images.sort(key=lambda x: (int(x.InstanceNumber) if x.InstanceNumber is not None else float('inf'), x.filename))
        return dicom_images, pixel_spacing

    def build_image_stack(self, slices, pixel_spacing):
        # Stack the image slices into a 3D numpy array
        image_stack = np.stack([s.pixel_array for s in slices])
        # Adjust for pixel spacing
        image_stack = np.swapaxes(image_stack, 0, 2)
        image_stack = np.swapaxes(image_stack, 0, 1)
        image_stack = np.flip(image_stack, 2)  # Flip for correct orientation
        return image_stack

    def display_slice(self, index):
        if self.current_view == 'axial':
            self.ax.imshow(self.image_stack[:, :, index], cmap=plt.cm.gray)
        elif self.current_view == 'coronal':
            self.ax.imshow(self.image_stack[:, index, :], cmap=plt.cm.gray)
        elif self.current_view == 'sagittal':
            self.ax.imshow(self.image_stack[index, :, :], cmap=plt.cm.gray)
        plt.draw()

    def update_slider(self, val):
        self.ax.clear()
        self.display_slice(int(val))

    def setup_slider(self):
        ax_slider = plt.axes([0.25, 0.1, 0.65, 0.03])
        self.slider = Slider(ax_slider, 'Slice', 0, self.image_stack.shape[2] - 1, valinit=0, valfmt='%0.0f')
        self.slider.on_changed(self.update_slider)

    def setup_buttons(self):
        ax_button_axial = plt.axes([0.25, 0.25, 0.15, 0.04])
        self.button_axial = Button(ax_button_axial, 'Axial')
        self.button_axial.on_clicked(self.change_view_axial)

        ax_button_coronal = plt.axes([0.45, 0.25, 0.15, 0.04])
        self.button_coronal = Button(ax_button_coronal, 'Coronal')
        self.button_coronal.on_clicked(self.change_view_coronal)

        ax_button_sagittal = plt.axes([0.65, 0.25, 0.15, 0.04])
        self.button_sagittal = Button(ax_button_sagittal, 'Sagittal')
        self.button_sagittal.on_clicked(self.change_view_sagittal)

    def change_view_axial(self, event):
        self.current_view = 'axial'
        self.slider.set_val(0)

    def change_view_coronal(self, event):
        self.current_view = 'coronal'
        self.slider.set_val(0)

    def change_view_sagittal(self, event):
        self.current_view = 'sagittal'
        self.slider.set_val(0)