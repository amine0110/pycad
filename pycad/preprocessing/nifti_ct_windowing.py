# Copyright (c) 2023 PYCAD
# This file is part of the PYCAD library and is released under the MIT License:
# https://github.com/amine0110/pycad/blob/main/LICENSE


import os
import numpy as np
import cv2
import nibabel as nib
from glob import glob
import matplotlib.pyplot as plt

class NiftiCTWindowing:
    """
    The class NiftiCTWindowing is used to apply windowing to NIfTI MRI images. 
    It can process a single NIfTI file or multiple files.

    This class is useful for MRI scans that have blur or noise, and is effective for these scenarios.
    
    Params:
    - window_center: The center of the window used for windowing.
    - window_width: The width of the window used for windowing.
    - visualize: Whether to show an example slice before and after windowing.

    ### Example of usage:
    ```Python
    from pycad.preprocessing import NiftiCTWindowing

    nifti_path = 'path/to/your/input/nifti.nii.gz'
    output_path = 'path/to/save/nifti.nii.gz'
    windower = NIfTIWindowing(window_center=40, window_width=400, visualize=True)
    windower.convert(nifti_path, output_path)
    ```
    """

    def __init__(self, window_center=40, window_width=400, visualize=False):
        self.window_center = window_center
        self.window_width = window_width
        self.visualize = visualize

    def apply_windowing(self, image):
        # Apply windowing - for example, a soft tissue window
        img_min = self.window_center - self.window_width // 2
        img_max = self.window_center + self.window_width // 2
        windowed_image = np.clip(image, img_min, img_max)

        # Normalize the windowed image for better visualization
        windowed_image = cv2.normalize(windowed_image, None, 0, 255, cv2.NORM_MINMAX)
        
        # Convert image back to the original scale with the new windowing
        windowed_image = ((windowed_image / 255.0) * (img_max - img_min)) + img_min

        return windowed_image.astype(np.int16)  # NIfTI images usually use 16-bit integers

    def process_file(self, nifti_path, output_path):
        # Load the NIfTI file
        nifti = nib.load(nifti_path)
        image = nifti.get_fdata().astype(np.float32)

        # Apply windowing
        windowed_image = self.apply_windowing(image)

        # Save the modified image
        new_nifti = nib.Nifti1Image(windowed_image, nifti.affine)
        nib.save(new_nifti, output_path)

        return image, windowed_image

    def convert(self, nifti_path, output_path):
        """
        Processes a NIfTI file.
        """
        # Ensure output directory exists
        output_dir = os.path.dirname(output_path)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        original_image, windowed_image = self.process_file(nifti_path, output_path)

        if self.visualize:
            self.display_example_slice(original_image, windowed_image)

    def display_example_slice(self, original_image, windowed_image):
        # Display the middle slice for 3D images
        slice_idx = original_image.shape[-1] // 2
        
        plt.figure(figsize=(12, 6))

        # Original Image
        plt.subplot(1, 2, 1)
        plt.imshow(original_image[..., slice_idx], cmap='gray')
        plt.title('Original MRI Image')
        plt.axis('off')

        # Windowed Image
        plt.subplot(1, 2, 2)
        plt.imshow(windowed_image[..., slice_idx], cmap='gray')
        plt.title('Windowed MRI Image')
        plt.axis('off')

        plt.show()