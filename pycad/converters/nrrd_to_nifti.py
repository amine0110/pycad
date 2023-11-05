# Copyright (c) 2023 PYCAD
# This file is part of the PYCAD library and is released under the MIT License:
# https://github.com/amine0110/pycad/blob/main/LICENSE


import SimpleITK as sitk
import os
import logging
from glob import glob

class NrrdToNiftiConverter:

    """
    This converter converts the NRRD files into NIFTI format.

    ## Example of usage:
    ```Python
    from pycad.converters import NrrdToNiftiConverter

    converter = NrrdToNiftiConverter()
    input_path = "path/to/nrrd/file/or/dir" # Can be either a file or a directory
    output_dir = "path/to/save/nifti/file/or/files"
    converter.convert(input_path, output_dir)
    ```
    """
    def __init__(self):
        # Initialize the logger
        self.logger = logging.getLogger('NrrdToNiftiConverter')
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def convert(self, input_path, output_dir):
        """
        Converts NRRD files to NIfTI files. Handles both individual files and directories containing multiple files.
        """
        os.makedirs(output_dir, exist_ok=True)

        if os.path.isdir(input_path):
            self.convert_directory(input_path, output_dir)
        elif os.path.isfile(input_path):
            self.convert_file(input_path, output_dir)
        else:
            self.logger.error(f"The input path does not exist: {input_path}")

    def convert_file(self, input_file_path, output_dir):
        """
        Converts a single NRRD file to a NIfTI file.
        """
        try:
            # Read the NRRD image
            nrrd_image = sitk.ReadImage(input_file_path)

            # Generate the corresponding output file path with .nii extension
            base_name = os.path.basename(input_file_path).split('.')[0]
            output_file_path = os.path.join(output_dir, f'{base_name}.nii.gz')

            # Write the image as a NIfTI file
            sitk.WriteImage(nrrd_image, output_file_path)
            self.logger.info(f'Converted {input_file_path} to {output_file_path}')
        except Exception as e:
            self.logger.error(f'Failed to convert {input_file_path}: {e}')

    def convert_directory(self, input_dir, output_dir):
        """
        Converts all NRRD files in the input directory to NIfTI files in the output directory.
        """
        # Find all .nrrd files in the directory
        nrrd_files = glob(os.path.join(input_dir, '*.nrrd'))

        for nrrd_file in nrrd_files:
            self.convert_file(nrrd_file, output_dir)