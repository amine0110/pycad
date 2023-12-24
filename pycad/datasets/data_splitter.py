# Copyright (c) 2023 PYCAD
# This file is part of the PYCAD library and is released under the MIT License:
# https://github.com/amine0110/pycad/blob/main/LICENSE


import os
import shutil
import random
import logging

class DataSplitter:
    '''
    This class is for splitting the images and labels into train/valid/test folders. The format by default is the yolo format, it is as follows:\n
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
    \n
    test\n
    |__ images\n
        |__ image_0\n
        |__ image_1\n
        |__ ...\n
    |__ labels\n
        |__ label_0\n
        |__ label_1\n
        |__ ...\n
    
    ### Params
    - images_dir: the path to the images
    - labels_dir: the path to the labels 
    - output_dir: the path to save the split folders 
    - train_ratio: the train ratio, default=0.7
    - valid_ratio: the validation ratio, default=0.2
    - test_ratio: the test ratio, default=0.1
    - delete_input: whether you want to delete the input files after split, default=False

    ### Example of usage:
    ```
    from pycad.datasets import DataSplitter

    img = 'datasets/dental/xray_panoramic_mandible/images'
    msk = 'datasets/dental/xray_panoramic_mandible/masks'
    output = 'datasets/dental/test'

    splitter = DataSplitter(img, msk, output, 0.7, 0.2, 0.1, delete_input=False)
    splitter.run()
    '''
    def __init__(self, images_dir, labels_dir, output_dir, train_ratio=0.7, valid_ratio=0.2, test_ratio=0.1, delete_input=False):
        self.images_dir = images_dir
        self.labels_dir = labels_dir
        self.output_dir = output_dir
        self.train_ratio = train_ratio
        self.valid_ratio = valid_ratio
        self.test_ratio = test_ratio
        self.delete_input = delete_input
        self.setup_directories()

    def setup_directories(self):
        self.dirs = {
            'train': {'images': os.path.join(self.output_dir, 'train', 'images'),
                      'labels': os.path.join(self.output_dir, 'train', 'labels')},
            'valid': {'images': os.path.join(self.output_dir, 'valid', 'images'),
                      'labels': os.path.join(self.output_dir, 'valid', 'labels')},
            'test': {'images': os.path.join(self.output_dir, 'test', 'images'),
                     'labels': os.path.join(self.output_dir, 'test', 'labels')}
        }
        for d in self.dirs.values():
            for path in d.values():
                os.makedirs(path, exist_ok=True)

    def get_filenames(self):
        images = sorted(os.listdir(self.images_dir))
        labels = sorted(os.listdir(self.labels_dir))
        return images, labels

    def split_data(self, images, labels):
        data = list(zip(images, labels))
        random.shuffle(data)
        total = len(data)
        train_end = int(total * self.train_ratio)
        valid_end = train_end + int(total * self.valid_ratio)

        train_data = data[:train_end]
        valid_data = data[train_end:valid_end]
        test_data = data[valid_end:] if self.test_ratio > 0 else []

        return {'train': train_data, 'valid': valid_data, 'test': test_data}

    def copy_files(self, split_data):
        for split, data in split_data.items():
            for img, lbl in data:
                shutil.copy(os.path.join(self.images_dir, img), self.dirs[split]['images'])
                shutil.copy(os.path.join(self.labels_dir, lbl), self.dirs[split]['labels'])
                logging.info(f'Copied {img} and {lbl} to {split} set')

    def run(self):
        images, labels = self.get_filenames()
        split_data = self.split_data(images, labels)
        self.copy_files(split_data)

        if self.delete_input:
            shutil.rmtree(self.images_dir)
            shutil.rmtree(self.labels_dir)
            logging.info('Deleted original input directories')