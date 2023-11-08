# Copyright (c) 2023 PYCAD
# This file is part of the PYCAD library and is released under the MIT License:
# https://github.com/amine0110/pycad/blob/main/LICENSE


import os
import pydicom
from pydicom.errors import InvalidDicomError
import SimpleITK as sitk
import numpy as np
from glob import glob
from tqdm import tqdm  # for progress bar

class DicomMriWindowing:
    '''
    This module is to apply windowing on the dark scans, it can be MRI or CBCT (these that gave great results in the testing phase).

    Params:
    - input_dir: path to the dicom directory
    - output_dir: path to the save the dicoms after windowing

    ### Example of usage:
    ```Python
    from pycad.preprocessing import DicomMriWindowing

    input_dir = './path/to/input/dicoms'
    output_dir = './path/to/save/windowed/dicoms'
    windower = DicomMriWindowing(input_dir, output_dir)
    windower.window_series()
    ```
    '''
    def __init__(self, input_dir, output_dir):
        self.input_dir = input_dir
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def load_series(self, dicom_paths):
        series_reader = sitk.ImageSeriesReader()
        series_reader.SetFileNames(dicom_paths)
        try:
            image_3d = series_reader.Execute()
            return image_3d
        except RuntimeError as e:
            print(f"Failed to load DICOM series: {e}")
            return None

    def apply_windowing(self, image_3d, coef=4):
        statistics_filter = sitk.StatisticsImageFilter()
        statistics_filter.Execute(image_3d)
        mean_intensity = statistics_filter.GetMean()
        std_intensity = statistics_filter.GetSigma()

        lower_bound = mean_intensity - coef * std_intensity
        upper_bound = mean_intensity + coef * std_intensity

        windowed_image = sitk.IntensityWindowing(image_3d, 
                                                windowMinimum=lower_bound, 
                                                windowMaximum=upper_bound, 
                                                outputMinimum=0.0, 
                                                outputMaximum=255.0)
        return windowed_image

    def save_dicom_slice(self, dcm, slice_arr, index):
        try:
            dcm.PixelData = slice_arr.tobytes()
            dcm.Rows, dcm.Columns = slice_arr.shape
            dcm.save_as(os.path.join(self.output_dir, f'slice_{str(index).zfill(4)}.dcm'))
            return True
        except Exception as e:
            print(f"Failed to save DICOM slice: {e}")
            return False

    def window_series(self, coef=4):
        dicom_paths = glob(os.path.join(self.input_dir, '*.dcm'))
        
        # Load the DICOM series
        image_3d = self.load_series(dicom_paths)
        if image_3d is None:
            return
        
        # Apply windowing
        windowed_image = self.apply_windowing(image_3d, coef=coef)
        windowed_array = sitk.GetArrayFromImage(windowed_image).astype(np.int16)

        # Iterate over each slice
        for i in tqdm(range(len(windowed_array)), desc="Processing"):
            try:
                dcm = pydicom.dcmread(dicom_paths[i])
                if not self.save_dicom_slice(dcm, windowed_array[i], i):
                    break
            except InvalidDicomError:
                print(f"Invalid DICOM file: {dicom_paths[i]}")
                break
            except FileNotFoundError:
                print(f"File not found: {dicom_paths[i]}")
                break