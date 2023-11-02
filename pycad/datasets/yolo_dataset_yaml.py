# Copyright (c) 2023 PYCAD
# This file is part of the PYCAD library and is released under the MIT License:
# https://github.com/amine0110/pycad/blob/main/LICENSE


class YOLODatasetYaml:
    '''
    This class creates the `dataset.yaml` file to train the YOLOv8 model.\n
    `Params`:
    - train_path: the path to training images and labels (you give just the directory that contains the two folders)
    - valid_path: the path to valid images and labels (you give just the directory that contains the two folders)
    - nc: the number of classes to train
    - class_names: here you can enter as much as class names as you want to train, the number of class names should be equal to the number of classes given before\n

    To create the dataset.yaml file, you need to call the method `create_yaml` and also give the path to the location to save the yaml file.\n
    \n\n
    #### Example usage:
    from pycad.preprocess.utils import YOLODatasetYaml

    config = YOLODatasetYaml("path/to/train", "path/to/valid", 3, "t1", "t2", "t3")\n
    config.create_yaml("dataset.yaml")
    '''
    def __init__(self, train_path, valid_path, nc, *class_names):
        self.train_path = train_path
        self.valid_path = valid_path
        self.nc = nc
        self.names = []
        self.set_class_names(*class_names)
        
    def set_class_names(self, *class_names):
        if self.nc != len(class_names):
            raise ValueError(f"The number of classes (nc={self.nc}) must be equal to the number of class names provided ({len(class_names)}).")
        self.names = list(class_names)
    
    def save(self, save_path):
        with open(save_path, 'w') as outfile:
            outfile.write(f"train: {self.train_path}\n")
            outfile.write(f"val: {self.valid_path}\n")
            outfile.write("\n")  # Adding a blank line
            outfile.write(f"nc: {self.nc}\n")
            outfile.write("names: " + str(self.names).replace("'", '"') + "\n")
            
    def create_yaml(self, save_path):
        self.save(save_path)