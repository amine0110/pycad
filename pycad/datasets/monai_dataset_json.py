import os
import shutil
import json
from glob import glob
import random

class MONAIDatasetOrganizer:
    '''
    This module can be used to create the `dataset.json` file to train medical imaging models using MONAI.\n
    It can help you do the split of the train/valid and fill the json file in the correct format needed for MONAI.

    ## Example of usage:
    ```Python
    from pycad.datasets import MONAIDatasetOrganizer

    labels = ["background", "vessels", "tumor"]  # Replace with actual labels
    train_volumes = glob("path/to/train/volumes/*.nii.gz")
    test_volumes = glob("path/to/test/volumes/*.nii.gz")
    train_segmentations = glob("path/to/train/labels/*.nii.gz")

    organizer = MONAIDatasetOrganizer('./data/vessels/', labels=labels)

    organizer.prepare_dataset(train_volumes, test_volumes, train_segmentations, val_split=0.1)
    # Optional: If you have separate validation data, otherwise set val_volumes and val_segmentations
    ```
    '''
    def __init__(self, base_dir, output_file='dataset.json', labels=None):
        self.base_dir = base_dir
        self.output_file = output_file
        if labels is None:
            labels = {
                "0": "background",
                "1": "spleen",
                "2": "rkidney",
                # ... add the rest of your labels here
            }
        self.labels = labels
    
    def create_directories(self):
        os.makedirs(os.path.join(self.base_dir, 'imagesTr'), exist_ok=True)
        os.makedirs(os.path.join(self.base_dir, 'imagesTs'), exist_ok=True)
        os.makedirs(os.path.join(self.base_dir, 'imagesVal'), exist_ok=True)  # New directory for validation images
        os.makedirs(os.path.join(self.base_dir, 'labelsTr'), exist_ok=True)
        os.makedirs(os.path.join(self.base_dir, 'labelsVal'), exist_ok=True)  # New directory for validation labels
    
    def move_files(self, files, destination):
        for file in files:
            shutil.move(file, os.path.join(destination, os.path.basename(file)))
    
    def split_dataset(self, train_volumes, train_segmentations, val_split=0.2):
        paired_files = list(zip(train_volumes, train_segmentations))
        random.shuffle(paired_files)
        split_idx = int(len(paired_files) * val_split)
        return paired_files[split_idx:], paired_files[:split_idx]
    
    def organize_dataset(self, train_volumes, test_volumes, train_segmentations, val_split=None):
        train_paired, val_paired = ([], [])
        if val_split is not None:
            train_paired, val_paired = self.split_dataset(train_volumes, train_segmentations, val_split)
        else:
            train_paired = list(zip(train_volumes, train_segmentations))
        
        train_volumes, train_segmentations = zip(*train_paired) if train_paired else ([], [])
        val_volumes, val_segmentations = zip(*val_paired) if val_paired else ([], [])
        
        self.move_files(train_volumes, os.path.join(self.base_dir, 'imagesTr'))
        self.move_files(train_segmentations, os.path.join(self.base_dir, 'labelsTr'))
        self.move_files(test_volumes, os.path.join(self.base_dir, 'imagesTs'))
        self.move_files(val_volumes, os.path.join(self.base_dir, 'imagesVal'))
        self.move_files(val_segmentations, os.path.join(self.base_dir, 'labelsVal'))
    
    def generate_dataset_json(self):
        train_images = sorted(glob(os.path.join(self.base_dir, 'imagesTr', '*.nii.gz')))
        val_images = sorted(glob(os.path.join(self.base_dir, 'imagesVal', '*.nii.gz')))
        test_images = sorted(glob(os.path.join(self.base_dir, 'imagesTs', '*.nii.gz')))
        train_labels = sorted(glob(os.path.join(self.base_dir, 'labelsTr', '*.nii.gz')))
        val_labels = sorted(glob(os.path.join(self.base_dir, 'labelsVal', '*.nii.gz')))

        dataset_json = {
            "description": "Medical Image Dataset",
            "labels": self.labels,
            "licence": "cc-by-sa-4.0",
            "training": [{'image': os.path.relpath(img, self.base_dir), 'label': os.path.relpath(lbl, self.base_dir)} for img, lbl in zip(train_images, train_labels)],
            "validation": [{'image': os.path.relpath(img, self.base_dir), 'label': os.path.relpath(lbl, self.base_dir)} for img, lbl in zip(val_images, val_labels)],
            "test": [os.path.relpath(img, self.base_dir) for img in test_images],
        }

        with open(os.path.join(self.base_dir, self.output_file), 'w') as outfile:
            json.dump(dataset_json, outfile, indent=4)

    def prepare_dataset(self, train_volumes, test_volumes, train_segmentations, val_split=None):
        self.create_directories()
        self.organize_dataset(train_volumes, test_volumes, train_segmentations, val_split)
        self.generate_dataset_json()