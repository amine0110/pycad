# Copyright (c) 2023 PYCAD
# This file is part of the PYCAD library and is released under the MIT License:
# https://github.com/amine0110/pycad/blob/main/LICENSE


import os
import pydicom
import numpy as np
import cv2
import logging
from glob import glob
import matplotlib.pyplot as plt

class DicomCTWindowing:
    """
    The class DicomCTWindowing is used to apply windowing to DICOM CT images. 
    It can process a single series of DICOM files or multiple series in different folders.

    This class is useful for the CT scans that has blur or noise, it is so effective for these scenarios, you can checkout our demos.
    
    Params:
    - window_center: The center of the window used for windowing.
    - window_width: The width of the window used for windowing.
    - visualize: Whether to show an example slice before and after windowing at the end of processing.
    
    ## Example of usage:
    ```Python
    from pycad.preprocessing import DicomCTWindowing
    
    dicom_dir = "path/to/dicom/series"  # Directory with DICOM files.
    output_dir = "path/to/output"
    window_center = 40
    window_width = 400
    converter = DicomCTWindowing(window_center, window_width, visualize=True)
    converter.convert(dicom_dir, output_dir)
    ```
    """

    def __init__(self, window_center=40, window_width=400, visualize=False):
        self.window_center = window_center
        self.window_width = window_width
        self.visualize = visualize
        # Initialize the logger
        self.logger = logging.getLogger('DicomCTWindowing')
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def preprocess_ct_image(self, dicom_path, output_path, i, force=False):
        # Load the DICOM file
        dcm = pydicom.read_file(dicom_path, force=force)
        original_image = dcm.pixel_array.astype(float)

        # Rescale to Hounsfield units (HU)
        image = original_image * dcm.RescaleSlope + dcm.RescaleIntercept
        
        # Apply windowing - for example, a soft tissue window

        img_min = self.window_center - self.window_width // 2
        img_max = self.window_center + self.window_width // 2
        image = np.clip(image, img_min, img_max)

        # Normalize the image for better visualization
        image = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX)
        
        # Convert image back to the original scale with the new windowing
        image = ((image / 255.0) * (img_max - img_min)) + img_min

        # Update DICOM tags
        dcm.WindowCenter = self.window_center
        dcm.WindowWidth = self.window_width
        dcm.RescaleIntercept = img_min
        dcm.RescaleSlope = (img_max - img_min) / 255.0

        # Convert to the necessary data type
        image = image.astype(np.int16)  # Most CT images use 16-bit signed integers
        dcm.PixelData = image.tobytes()

        # Save the modified image
        path_to_save = f'{output_path}/slice_{str(i).zfill(4)}.dcm'
        dcm.save_as(path_to_save)

        return original_image, image

    def process_directory(self, input_dir, output_dir, force=False):
        """
        Processes all DICOM files in a given directory, applies windowing, and saves the output.
        """
        # Ensure output directory exists
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        dicom_paths = glob(os.path.join(input_dir, '*.dcm'))
        if not dicom_paths:
            self.logger.warning(f'No DICOM files found in {input_dir}.')
            return

        example_image = None
        for i, dicom_path in enumerate(sorted(dicom_paths)):
            try:
                original_image, preprocessed_image = self.preprocess_ct_image(dicom_path, output_dir, i, force=force)
                if self.visualize and example_image is None:
                    example_image = (original_image, preprocessed_image)
            except Exception as e:
                self.logger.error(f'Error processing file {dicom_path}: {e}')
        
        if self.visualize and example_image is not None:
            self.display_example_slice(example_image[0], example_image[1])

    def display_example_slice(self, original_image, preprocessed_image):
        """
        Displays an example slice before and after processing.
        """
        plt.figure(figsize=(12, 6))

        # Original Image
        plt.subplot(1, 2, 1)
        plt.imshow(original_image, cmap='gray')
        plt.title('Original CT Image')
        plt.axis('off')

        # Preprocessed Image
        plt.subplot(1, 2, 2)
        plt.imshow(preprocessed_image, cmap='gray')
        plt.title('Preprocessed CT Image')
        plt.axis('off')

        plt.show()

    def convert(self, input_dir_or_dirs, output_dir):
        """
        Processes one or multiple directories of DICOM files.
        """
        if isinstance(input_dir_or_dirs, str):
            self.process_directory(input_dir_or_dirs, output_dir)
        elif isinstance(input_dir_or_dirs, list):
            for input_dir in input_dir_or_dirs:
                individual_output_dir = os.path.join(output_dir, os.path.basename(input_dir))
                self.process_directory(input_dir, individual_output_dir)
        else:
            self.logger.error('Invalid input. Please provide a directory path or a list of directory paths.')