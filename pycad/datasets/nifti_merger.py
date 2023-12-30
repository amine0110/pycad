# Copyright (c) 2023 PYCAD
# This file is part of the PYCAD library and is released under the MIT License:
# https://github.com/amine0110/pycad/blob/main/LICENSE


import os
import shutil
import nibabel as nib
import numpy as np
from glob import glob

class MultiClassNiftiMerger:
    '''
    If you have multiple nifti files representing different classes for the same patient, then this 
    function is for you, it helps you merge the nifti files into one nifti file.

    ### Params
    - volume_path: Path to the volume NIfTI file.
    - class_paths: List of paths to the class NIfTI files.
    - output_dir: Directory where the merged files will be saved.
    - move_volumes: Flag to control whether to move corresponding volumes.

    ### Example of usage

    ```Python
    # Example usage for directories
    from pycad.datasets import MultiClassNiftiMerger

    volume_dir = 'datasets/hips/hip_right100/volumes'
    class_dirs = ['datasets/hips/hip_right100/segmentations', 'datasets/hips/hip_left100/segmentations']
    output_dir = 'datasets/hips/merged'
    MultiClassNiftiMerger.process_directories(volume_dir, class_dirs, output_dir, move_volumes=True)
    ```
    '''
    
    def __init__(self, volume_path, class_paths, output_dir, move_volumes=False):
        self.volume_path = volume_path
        self.class_paths = class_paths
        self.output_dir = output_dir
        self.move_volumes = move_volumes

        self.segmentations_dir = os.path.join(output_dir, 'segmentations')
        self.volumes_dir = os.path.join(output_dir, 'volumes')

    def check_files(self):
        # Check if files exist
        paths_to_check = [self.volume_path] + self.class_paths
        for path in paths_to_check:
            if not os.path.exists(path):
                raise FileNotFoundError(f"File not found: {path}")

    def combine_classes(self):
        self.check_files()

        # Create directories for output
        os.makedirs(self.segmentations_dir, exist_ok=True)
        if self.move_volumes:
            os.makedirs(self.volumes_dir, exist_ok=True)

        # Initialize a combined array with zeros
        first_nifti = nib.load(self.class_paths[0])
        combined_classes = np.zeros(first_nifti.shape, dtype=np.int16)

        # Assign new class labels
        for idx, class_path in enumerate(self.class_paths):
            class_nifti = nib.load(class_path)
            class_data = class_nifti.get_fdata()
            combined_classes[class_data > 0] = idx + 1

        # Create a new NIfTI image for the combined classes
        combined_nifti = nib.Nifti1Image(combined_classes, affine=class_nifti.affine)

        # Save the new NIfTI file
        combined_filename = os.path.basename(self.volume_path).replace('volume', 'combined')
        combined_path = os.path.join(self.segmentations_dir, combined_filename)
        nib.save(combined_nifti, combined_path)

        # Optionally move the volume file
        if self.move_volumes:
            shutil.copy(self.volume_path, self.volumes_dir)

        print(f"Combined NIfTI file saved at: {combined_path}")

    @staticmethod
    def process_directories(volume_dir, class_dirs, output_dir, ext='.nii.gz', move_volumes=False):
        volume_files = glob(os.path.join(volume_dir, f'*{ext}'))

        for volume_file in volume_files:
            volume_filename = os.path.basename(volume_file)
            class_paths = [glob(os.path.join(class_dir, f"{volume_filename.split('.')[0]}*{ext}")) for class_dir in class_dirs]
            class_paths = [item for sublist in class_paths for item in sublist] # Flatten list

            if class_paths:
                merger = MultiClassNiftiMerger(
                    volume_file,
                    class_paths,
                    output_dir,
                    move_volumes
                )
                merger.combine_classes()