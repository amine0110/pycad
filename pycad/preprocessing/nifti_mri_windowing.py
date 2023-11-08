# Copyright (c) 2023 PYCAD
# This file is part of the PYCAD library and is released under the MIT License:
# https://github.com/amine0110/pycad/blob/main/LICENSE


import nibabel as nib
import numpy as np
import os
from tqdm import tqdm

class NiftiMriWindowing:
    '''
    This module is to apply windowing on the dark scans, it can be MRI or CBCT (these that gave great results in the testing phase). This is the NIFTI format version.

    Params:
    - input_filepath: the path to the input nifti file (.nii / .nii.gz)
    - output_filepath: the path to the output nifti file (.nii / .nii.gz)

    ### Example of usage:
    ```Python
    from pycad.preprocessing import NiftiMriWindowing

    input_filepath = './path/to/input/image.nii'
    output_filepath = './path/to/output/windowed_image.nii'
    windower = NiftiMriWindowing(input_filepath, output_filepath)
    windower.window_image(coef=4)
    ```
    '''
    def __init__(self, input_filepath, output_filepath):
        self.input_filepath = input_filepath
        self.output_filepath = output_filepath
        os.makedirs(os.path.dirname(self.output_filepath), exist_ok=True)

    def load_image(self):
        try:
            nifti_image = nib.load(self.input_filepath)
            return nifti_image
        except Exception as e:
            print(f"Failed to load NIfTI file: {e}")
            return None

    def apply_windowing(self, image, coef=4):
        data_array = image.get_fdata()
        mean_intensity = np.mean(data_array)
        std_intensity = np.std(data_array)

        lower_bound = mean_intensity - coef * std_intensity
        upper_bound = mean_intensity + coef * std_intensity

        windowed_data = np.clip(data_array, lower_bound, upper_bound)
        windowed_data_scaled = 255 * (windowed_data - lower_bound) / (upper_bound - lower_bound)

        return nib.Nifti1Image(windowed_data_scaled.astype(np.uint8), image.affine, image.header)

    def save_image(self, image):
        try:
            nib.save(image, self.output_filepath)
            print(f"Saved windowed image to {self.output_filepath}")
            return True
        except Exception as e:
            print(f"Failed to save windowed NIfTI image: {e}")
            return False

    def window_image(self, coef=4):
        # Load the NIfTI file
        nifti_image = self.load_image()
        if nifti_image is None:
            return

        # Apply windowing
        windowed_image = self.apply_windowing(nifti_image, coef=coef)

        # Save the windowed image
        if not self.save_image(windowed_image):
            print("An error occurred while saving the windowed image.")