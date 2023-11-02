# Copyright (c) 2023 PYCAD
# This file is part of the PYCAD library and is released under the MIT License:
# https://github.com/amine0110/pycad/blob/main/LICENSE


import SimpleITK as sitk
import os
from glob import glob
import numpy as np
from tqdm import tqdm
from PIL import Image


class NiftiToPngConverter:
    '''
    The nifti to png converter can be used to convert one or multiple nifti files into png images. It can be called `from pycad.converters import NiftiToPngConverter`.\n
    `max_v` and `min_v` needs to be checked before doing the conversion. Please see the plan [here](https://www.notion.so/What-to-do-before-training-a-model-with-Yolov8-443dd35fd3974770a3d17759ec1d3de4?pvs=4).\n

    ### Example of usage:
    ```
    from pycad.converters import NiftiToPngConverter

    image_paths = 'path ot images'
    seg_paths = 'path to segmentations'
    output_path = 'path to save the outputs'
    converter = NiftiToPngConverter(max_v=200, min_v=-200)

    converter.run(image_paths, seg_paths, output_path)
    
    ```
    '''

    def __init__(self, max_v=200, min_v=-200):
        self.max_v = max_v
        self.min_v = min_v

    def prepare_image(self, image_data, data_type='vol'):
        '''
        This function prepares the image data for conversion.
        '''
        if data_type == 'vol':
            HOUNSFIELD_MIN = int(float(self.min_v))
            HOUNSFIELD_MAX = int(float(self.max_v))
            HOUNSFIELD_RANGE = HOUNSFIELD_MAX - HOUNSFIELD_MIN

            image_data[image_data < HOUNSFIELD_MIN] = HOUNSFIELD_MIN
            image_data[image_data > HOUNSFIELD_MAX] = HOUNSFIELD_MAX
            normalized_image = (image_data - HOUNSFIELD_MIN) / HOUNSFIELD_RANGE

            return np.uint8(normalized_image * 255)
        elif data_type == 'seg':
            return np.uint8(image_data)

    def convert_nifti_to_png(self, in_dir:str, out_dir:str, data_type:str):
        '''
        This function is to take one nifti file and then convert it into png series, it keeps the same casename and then adds _indexID.\n
        - `in_dir`: the path to one nifti file: nii | nii.gz\n
        - `out_dir`: the path to save the png series\n
        - `data_type`: the type of the input nifti file, is it a volume or segmentation?
        '''
        try:
            new_img = sitk.ReadImage(in_dir)
            img_array = sitk.GetArrayFromImage(new_img)
            case_name = os.path.basename(in_dir)[:-7]

            if not os.path.exists(out_dir):
                os.makedirs(out_dir)

            for i, img_slice in enumerate(img_array):
                prepared_image = self.prepare_image(img_slice, data_type=data_type)
                prepared_image = np.rot90(prepared_image, 2)
                img = Image.fromarray(prepared_image)
                img = img.convert('RGB')
                img.save(f"{out_dir}/{case_name}_{str(i).zfill(4)}.png")
        except:
            print('Error with the file:', in_dir)

    def convert_nifti_to_png_dir(self, in_dir:str, out_dir:str, data_type:str):
        '''
        This function is the directory version of `convert_nifti_to_png`, and it can be used to convert a whole directory of nifti files either for volumes or segmentations.\n
        - `in_dir`: the directory to the nifti files (.nii or .nii.gz)\n
        - `out_dir`: the directory to save the png outputs\n
        - `data_type`: the type of the input, either vol for volumes or seg for segmentations, any mistake on this will cause wrong png files
        '''
        cases_list = glob(os.path.join(in_dir, '*'))
        cases_list = [case for case in cases_list if case.endswith('.nii') or case.endswith('.nii.gz')]

        for case in tqdm(cases_list):
            self.convert_nifti_to_png(case, out_dir, data_type)

    def run(self, in_dir_vol:str = None, in_dir_seg:str = None, out_dir:str = None):
        '''
        This function is the main function to call the conversion function for the volumes and segmentations.\n
        - `in_dir_vol`: path to the input dir containing the volume files (nifti)\n
        - `in_dir_seg`: path to the input dir containing the segmentation files (nifti)\n
        - `out_dir`: path to save the converted png files for the volumes and the segmentations\n
        '''

        if in_dir_vol:
            print("Converting volume files")
            self.convert_nifti_to_png_dir(in_dir_vol, out_dir + '/images', 'vol') # convert the volumes
        
        if in_dir_seg:
            print("Converting segmentation files")
            self.convert_nifti_to_png_dir(in_dir_seg, out_dir + '/labels', 'seg') # convert the segmentation files
