# Copyright (c) 2023 PYCAD
# This file is part of the PYCAD library and is released under the MIT License:
# https://github.com/amine0110/pycad/blob/main/LICENSE


import SimpleITK as sitk
import os
import time
from glob import glob
from tqdm import tqdm


class NrrdToDicomConverter:
    '''
    The nrrd to dicom converter can be used to convert one or multiple nrrd files into dicom series. It can be called `from pycad.converters import NrrdToDicomConverter`\n

    ```
    from pycad.converters import NrrdToDicomConverter

    in_dir = 'path to one nrrd file'
    out_dir = 'path to the folder to save the dicom series'
    converter = NrrdToDicomConverter()

    converter.nrrd2dicom_1file(in_dir, out_dir) # to convert one nrrd file, and you can do the same thing with multiple nrrd files using nrrd2dicom_mfile

    ```
    '''
    def __init__(self):
        pass

    @staticmethod
    def writeSlices(series_tag_values, new_img, i, out_dir):
        '''
        This function is used to extract the extract the meta data and store it in each slice of the dicom series.
        '''
        
        image_slice = new_img[:,:,i]
        img_np = sitk.GetArrayFromImage(image_slice)

        # Rescale the image slice intensities and cast to integer type
        rescaler = sitk.RescaleIntensityImageFilter()
        rescaler.SetOutputMinimum(int(img_np.min()))
        rescaler.SetOutputMaximum(int(img_np.max())) # Adjust according to your needs
        image_slice = rescaler.Execute(image_slice)

        image_slice = sitk.Cast(image_slice, sitk.sitkInt16) # or another integer type as needed

        writer = sitk.ImageFileWriter()
        writer.KeepOriginalImageUIDOn()

        # Tags shared by the series.
        list(map(lambda tag_value: image_slice.SetMetaData(tag_value[0], tag_value[1]), series_tag_values))

        # Slice specific tags.
        image_slice.SetMetaData("0008|0012", time.strftime("%Y%m%d")) # Instance Creation Date
        image_slice.SetMetaData("0008|0013", time.strftime("%H%M%S")) # Instance Creation Time

        # Setting the type to CT preserves the slice location.
        image_slice.SetMetaData("0008|0060", "CT")  # set the type to CT so the thickness is carried over

        # (0020, 0032) image position patient determines the 3D spacing between slices.
        image_slice.SetMetaData("0020|0032", '\\'.join(map(str,new_img.TransformIndexToPhysicalPoint((0,0,i))))) # Image Position (Patient)
        image_slice.SetMetaData("0020,0013", str(i)) # Instance Number

        # Write to the output directory and add the extension dcm, to force writing in DICOM format.
        writer.SetFileName(os.path.join(out_dir,'slice' + str(i).zfill(4) + '.dcm'))
        writer.Execute(image_slice)


    def nrrd2dicom_1file(self, in_dir, out_dir):
        """
        This function is to convert only one nrrd file into dicom series

        `nrrd_dir`: the path to the one nrrd file
        `out_dir`: the path to output
        """

        os.makedirs(out_dir, exist_ok=True)

        new_img = sitk.ReadImage(in_dir) 
        modification_time = time.strftime("%H%M%S")
        modification_date = time.strftime("%Y%m%d")

        direction = new_img.GetDirection()
        series_tag_values = [("0008|0031",modification_time), # Series Time
                        ("0008|0021",modification_date), # Series Date
                        ("0008|0008","DERIVED\\SECONDARY"), # Image Type
                        ("0020|000e", "1.2.826.0.1.3680043.2.1125."+modification_date+".1"+modification_time), # Series Instance UID
                        ("0020|0037", '\\'.join(map(str, (direction[0], direction[3], direction[6],# Image Orientation (Patient)
                                                            direction[1],direction[4],direction[7])))),
                        ("0008|103e", "Created-Pycad")] # Series Description


        # Write slices to output directory
        list(map(lambda i: self.writeSlices(series_tag_values, new_img, i, out_dir), range(new_img.GetDepth())))

    def nrrd2dicom_mfiles(self, nrrd_dir, out_dir=''):
        """
        This function is to convert multiple nrrd files into dicom files

        `nrrd_dir`: You enter the global path to all of the nrrd files here.
        `out_dir`: Put the path to where you want to save all the dicoms here.

        PS: Each nrrd file's folders will be created automatically, so you do not need to create an empty folder for each patient.
        """

        images = glob(nrrd_dir + '/*.nrrd')

        for image in tqdm(images):
            o_path = out_dir + '/' + os.path.basename(image)[:-7]
            os.makedirs(o_path, exist_ok=True)

            self.nrrd2dicom_1file(image, o_path)