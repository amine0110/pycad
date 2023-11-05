# Copyright (c) 2023 PYCAD
# This file is part of the PYCAD library and is released under the MIT License:
# https://github.com/amine0110/pycad/blob/main/LICENSE


import SimpleITK as sitk
import os
import logging
from glob import glob

class NiftiToNrrdConverter:

    """
    This converter converts the NIFTI files to NRRD, it can be one file or multiple files for the input, the code will take in consideration these two conditions.

    ## Example of usage
    ```Python
    from pycad.converters import NiftiToNrrdConverter

    converter = NiftiToNrrdConverter()
    input_path = "path/to/input/file/or/dir"  # Can be either a file or a directory
    output_dir = "path/to/save/file/or/files"
    converter.convert(input_path, output_dir)
    ```
    """
    def __init__(self):
        # Initialize the logger
        self.logger = logging.getLogger('NiftiToNrrdConverter')
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def convert(self, input_path, output_dir):
        """
        Converts NIfTI files to NRRD files. Handles both individual files and directories containing multiple files.
        """
        if os.path.isdir(input_path):
            self.convert_directory(input_path, output_dir)
        elif os.path.isfile(input_path):
            self.convert_file(input_path, output_dir)
        else:
            self.logger.error(f"The input path does not exist: {input_path}")

    def convert_file(self, input_file_path, output_dir):
        """
        Converts a single NIfTI file to an NRRD file.
        """
        try:
            # Read the NIfTI image
            nifti_image = sitk.ReadImage(input_file_path)

            # Generate the corresponding output file path with .nrrd extension
            base_name = os.path.basename(input_file_path).split('.')[0]
            output_file_path = os.path.join(output_dir, f'{base_name}.nrrd')

            # Write the image as an NRRD file
            sitk.WriteImage(nifti_image, output_file_path)
            self.logger.info(f'Converted {input_file_path} to {output_file_path}')
        except Exception as e:
            self.logger.error(f'Failed to convert {input_file_path}: {e}')

    def convert_directory(self, input_dir, output_dir):
        """
        Converts all NIfTI files in the input directory to NRRD files in the output directory.
        """
        # Find all .nii and .nii.gz files in the directory
        nifti_files = glob(os.path.join(input_dir, '*.nii')) + glob(os.path.join(input_dir, '*.nii.gz'))

        for nifti_file in nifti_files:
            self.convert_file(nifti_file, output_dir)

