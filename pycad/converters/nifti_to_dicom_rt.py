# Copyright (c) 2023 PYCAD
# This file is part of the PYCAD library and is released under the MIT License:
# https://github.com/amine0110/pycad/blob/main/LICENSE


from rt_utils import RTStructBuilder
import logging
from tqdm import tqdm
import numpy as np
import nibabel as nib

class NiftiToDicomRT:
    def __init__(self, nifti_path, dicom_series_path, output_path, selected_classes):
        """
        Initialize NiftiToDicomRT converter
        
        Args:
            nifti_path: Path to input NIfTI mask file
            dicom_series_path: Directory containing DICOM series
            output_path: Path where to save output RTSTRUCT DICOM
            selected_classes: Dictionary mapping class indices to names {idx: "name"}
        """
        self.nifti_path = nifti_path
        self.dicom_path = dicom_series_path
        self.output_path = output_path
        self.selected_classes = selected_classes
        
        # Configure logging
        logging.basicConfig(level=logging.WARNING)  # avoid messages from rt_utils
        
        # Load and preprocess NIfTI data
        nifti_file = nib.load(self.nifti_path)
        array = nifti_file.get_fdata()
        self.mask_array = np.transpose(array, (2, 1, 0))
        self.mask_array = np.rot90(self.mask_array, k=-1)
        
        print("Loaded mask shape: ", self.mask_array.shape)

    def convert(self):
        """Convert NIfTI mask to DICOM RTSTRUCT"""
        # Create new RT Struct
        rtstruct = RTStructBuilder.create_new(dicom_series_path=self.dicom_path)

        # Add each class as an ROI
        for class_idx, class_name in tqdm(self.selected_classes.items()):
            binary_img = self.mask_array == class_idx
            if binary_img.sum() > 0:  # only save non-empty images
                rtstruct.add_roi(
                    mask=binary_img,  # binary numpy array
                    name=class_name
                )

        # Save the RTSTRUCT file
        rtstruct.save(str(self.output_path))