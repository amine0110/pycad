# Copyright (c) 2023 PYCAD
# This file is part of the PYCAD library and is released under the MIT License:
# https://github.com/amine0110/pycad/blob/main/LICENSE


import os
from sklearn.model_selection import train_test_split
import shutil


class DataSplitter:
    '''
    This class is for splitting the images and labels into train/valid folders. The format by default is the yolo format, it is as follows:\n
    train\n
    |__ images\n
        |__ image_0\n
        |__ image_1\n
        |__ ...\n
    |__ labels\n
        |__ labels_0\n
        |__ labels_1\n
        |__ ...\n
    \n
    valid\n
    |__ images\n
        |__ image_0\n
        |__ image_1\n
        |__ ...\n
    |__ labels\n
        |__ label_0\n
        |__ label_1\n
        |__ ...\n
    
    `Params`:
    - images_dir: the directory where the input images are stored
    - labels_dir: the directory where the input labels are stored
    - output_dir: the directory to save the split files, train, valid (you don't need to specify the folders name train and valid, it will be taken in consideration by the code)
    - train_size: the size of the training data (percentage)
    - random_state: this is to controle how randomly the code will be to choose the train and valid files (this is a good value by default)
    - delete_input: you can activate it if you want that the code deletes the input images and labels after doing the split\n

    ### Example of usage:
    ```
    from pycad.preprocess.utils import DataSplitter

    input_dir_img = 'path to the input folder for the images'
    input_dir_labels = 'path to the input folder for the labels'

    splitter = DataSplitter(input_dir_img, input_dir_labels, .8)
    splitter.run()
    ```

    '''
    def __init__(self, images_dir, labels_dir, output_dir, train_size=0.8, random_state=42, delete_input=False):
        self.images_dir = images_dir
        self.labels_dir = labels_dir
        self.output_dir = output_dir
        self.train_size = train_size
        self.random_state = random_state
        self.delete_input = delete_input

        # Define the directory structure
        self.train_images_dir = os.path.join(self.output_dir, 'train', 'images')
        self.train_labels_dir = os.path.join(self.output_dir, 'train', 'labels')
        self.valid_images_dir = os.path.join(self.output_dir, 'valid', 'images')
        self.valid_labels_dir = os.path.join(self.output_dir, 'valid', 'labels')

    def split_data(self):
        # Get all file names
        all_images = os.listdir(self.images_dir)
        all_labels = os.listdir(self.labels_dir)

        # Split data into train and validation sets
        train_images, valid_images = train_test_split(all_images, test_size=1-self.train_size, random_state=self.random_state)
        train_labels, valid_labels = train_test_split(all_labels, test_size=1-self.train_size, random_state=self.random_state)

        return train_images, valid_images, train_labels, valid_labels

    def create_directories(self):
        # Create directories if they don't exist
        os.makedirs(self.train_images_dir, exist_ok=True)
        os.makedirs(self.train_labels_dir, exist_ok=True)
        os.makedirs(self.valid_images_dir, exist_ok=True)
        os.makedirs(self.valid_labels_dir, exist_ok=True)

    def copy_files(self, train_images, valid_images, train_labels, valid_labels):
        # Copy files into the corresponding directories
        print(f'[INFO]: Copying Train-Images to {self.train_images_dir}')
        for file in train_images:
            shutil.copy(os.path.join(self.images_dir, file), self.train_images_dir)
        
        print(f'[INFO]: Copying Train-Labels to {self.train_labels_dir}')
        for file in train_labels:
            shutil.copy(os.path.join(self.labels_dir, file), self.train_labels_dir)
        
        print(f'[INFO]: Copying Valid-Images to {self.valid_images_dir}')
        for file in valid_images:
            shutil.copy(os.path.join(self.images_dir, file), self.valid_images_dir)
        
        print(f'[INFO]: Copying Valid-Labels to {self.valid_labels_dir}')
        for file in valid_labels:
            shutil.copy(os.path.join(self.labels_dir, file), self.valid_labels_dir)
    
    def run(self):
        train_images, valid_images, train_labels, valid_labels = self.split_data()
        self.create_directories()
        self.copy_files(train_images, valid_images, train_labels, valid_labels)

        if self.delete_input:
            print(f'[INFO]: Deleting input directories')
            shutil.rmtree(self.images_dir)
            shutil.rmtree(self.labels_dir)