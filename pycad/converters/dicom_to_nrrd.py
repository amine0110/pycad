# Copyright (c) 2023 PYCAD
# This file is part of the PYCAD library and is released under the MIT License:
# https://github.com/amine0110/pycad/blob/main/LICENSE


import SimpleITK as sitk
import os
import logging

class DicomToNrrdConverter:

    """
    The class DicomToNrrdConverter is used to convert dicom series into nrrd file, it can be used for one patient (one folder of dicom series) or multiple patient (multiple folders of dicom series).\n

    Params:
    - min_images_per_series: the minimum number of dicom series to validate the conversion, so if for example the folder or subfolder contains only one or two dicoms, then there is no need to validate the conversion because we can't convert one dicom to a nrrd file.\n

    ## Example of usage:
    ```Python
    from pycad.converters import DicomToNrrdConverter

    input_dir = "path/to/input/folder"  # This directory can contain one or more series of DICOM images.
    output_dir = "path/to/output/folder"
    converter = DicomToNrrdConverter(min_images_per_series=10)  # Set the minimum number of images per series.
    converter.convert(input_dir, output_dir)
    ```


    """

    def __init__(self, min_images_per_series=5):
        self.min_images_per_series = min_images_per_series  # Minimum number of DICOM images to consider a directory a valid series.
        # Initialize the logger
        self.logger = logging.getLogger('DicomToNrrdConverter')
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def find_dicom_series(self, root_dir):
        """
        Recursively searches for DICOM series in the given directory and returns the paths.
        Only includes directories with at least `self.min_images_per_series` DICOM files.
        """
        series_paths = []
        for subdir, dirs, files in os.walk(root_dir):
            dicom_files = [os.path.join(subdir, file) for file in files if file.lower().endswith('.dcm')]
            if len(dicom_files) >= self.min_images_per_series:
                series_paths.append((subdir, dicom_files))
        return series_paths

    def convert_series_to_nrrd(self, dicom_series, output_path, output_filename=None):
        """
        Converts a DICOM series to a NRRD file, naming the output based on the parent directory of the DICOM series.
        """
        try:
            reader = sitk.ImageSeriesReader()
            dicom_names = reader.GetGDCMSeriesFileNames(dicom_series[0])
            reader.SetFileNames(dicom_names)
            image = reader.Execute()

            # Use the directory name of the DICOM series as the file name for the Nrrd image.
            if output_filename:
                output_filename = os.path.join(output_path, output_filename)
            else:
                dir_name = os.path.basename(os.path.normpath(dicom_series[0]))    
                output_filename = os.path.join(output_path, dir_name+'.nrrd')
                
            sitk.WriteImage(image, output_filename)
            self.logger.info(f'Converted: {output_filename}')
        except Exception as e:
            self.logger.error(f'Failed conversion for series {dicom_series[0]}: {e}')

    def convert(self, input_dir, output_dir, output_filename=None):
        """
        Converts all valid DICOM series found in the input directory to NRRD files in the output directory,
        using the directory names as file names.
        """
        series_paths = self.find_dicom_series(input_dir)
        if not series_paths:
            self.logger.warning('No valid DICOM series found.')
            return

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        for series in series_paths:
            self.convert_series_to_nrrd(series, output_dir, output_filename)