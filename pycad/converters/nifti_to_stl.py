# Copyright (c) 2023 PYCAD
# This file is part of the PYCAD library and is released under the MIT License:
# https://github.com/amine0110/pycad/blob/main/LICENSE


import os
import numpy as np
import vtk
import vedo
import nibabel as nib
from skimage import measure, transform
from vtk.util.numpy_support import vtk_to_numpy



class Nifti2StlConverter:
    '''
    This converter is for nifti to stl file(s). There are multiple methods done here, some using vtk and another using vedo.\n
    - `nifti2stl_vtk`: convert one nifti file to one stl file (all the classes will be considered as one class and color)
    - `nifti2stl_vedo`: convert one nifti file to one or multiple stl files (depending on the number of classes), this approach helps create an stl file with small file size (but a small mesh also)
    - `nifti2stl_vtk_multi_class`: convert one nifti file to one or multiple stl files by keeping the exact mesh size, but this can lead to a large file size.\n

    ### Example of usage:
    ```
    from pycad.converters import Nifti2StlConverter

    path_to_nifti = 'path to the input nifti file'
    path_to_stl = 'path to save the stl file' # dont need to add the .stl neither the file name
    converter = Nifti2StlConverter(path_to_nift, path_to_stl)

    converter.nifti2stl_vtk()
    # you can do the same thing for the other types of converters from nifti to stl.
    ```
    '''

    def __init__(self, in_dir, out_dir):
        self.in_dir = in_dir
        self.out_dir = out_dir
        self.case_name = os.path.basename(in_dir).split('.')[0]
        os.makedirs(self.out_dir, exist_ok=True)

    def nifti2stl_vtk(self):
        reader = vtk.vtkNIFTIImageReader()
        reader.SetFileName(self.in_dir)
        reader.Update()

        contour = vtk.vtkContourFilter()
        contour.SetInputConnection(reader.GetOutputPort())
        contour.SetValue(0, 1)

        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(contour.GetOutputPort())

        actor = vtk.vtkActor()
        actor.SetMapper(mapper)

        smoother = vtk.vtkWindowedSincPolyDataFilter()
        smoother.SetInputConnection(contour.GetOutputPort())
        smoother.SetNumberOfIterations(150)
        smoother.BoundarySmoothingOn()
        smoother.FeatureEdgeSmoothingOff()
        smoother.SetFeatureAngle(120.0)
        smoother.SetPassBand(0.05)
        smoother.NonManifoldSmoothingOn()
        smoother.NormalizeCoordinatesOn()
        smoother.Update()

        writer = vtk.vtkSTLWriter()
        writer.SetInputConnection(smoother.GetOutputPort())
        writer.SetFileName(f'{self.out_dir}/{self.case_name}.stl')
        writer.Write()

    def nifti2stl_vedo(self):
        nifti_img = nib.load(self.in_dir)
        volume = nifti_img.get_fdata()

        classes = np.unique(volume)[1:]

        for class_value in classes:
            if int(class_value) != 0:
                segmented_volume = np.zeros(volume.shape)
                segmented_volume[volume == int(class_value)] = 1

                temp = transform.downscale_local_mean(segmented_volume, (2, 2, 2))

                verts, faces, normals, _ = measure.marching_cubes(temp, 0)

                mesh = vedo.Mesh([verts, faces])

                smoother = vtk.vtkWindowedSincPolyDataFilter()
                smoother.SetInputData(mesh.polydata())
                smoother.SetNumberOfIterations(150)
                smoother.BoundarySmoothingOn()
                smoother.FeatureEdgeSmoothingOff()
                smoother.SetFeatureAngle(120.0)
                smoother.SetPassBand(0.05)
                smoother.NonManifoldSmoothingOn()
                smoother.NormalizeCoordinatesOn()
                smoother.Update()

                mesh_smoothed = vedo.Mesh(smoother.GetOutput())

                filename = f"{self.out_dir}/{self.case_name}_{int(class_value)}.stl"
                mesh_smoothed.write(filename)

    def nifti2stl_vtk_multi_class(self, smoothing=True, reduce_meshes=True, number_of_iterations=50, percent_reductions=0.5):
        '''
        This function is to convert one nifti file to stl file(s) using vtk only. This function require additional arguments to control the smoothing...\n
        - `smoothing`: a boolean to indicate whether you want to apply smoothing or not
        - `reduce_meshes`: a boolean to indicate whether you want to reduce the mesh, this helps you get a small file size (if you have a large mesh)
        - `number_of_interations`: this coefficient belongs to the smoothing algorithm, more iterations applied means more smooth mesh
        - `percent_reductions`: this coefficient belongs to the reduction algorithm, which means how much you want to reduce the mesh
        '''
        reader = vtk.vtkNIFTIImageReader()
        reader.SetFileName(self.in_dir)
        reader.Update()

        image_data = reader.GetOutput()
        np_array = vtk_to_numpy(image_data.GetPointData().GetScalars())
        unique_values = np.unique(np_array)

        for value in unique_values:
            if value == 0:
                continue

            thresh = vtk.vtkImageThreshold ()
            thresh.SetInputConnection(reader.GetOutputPort())
            thresh.ThresholdBetween(value, value)
            thresh.ReplaceInOn()
            thresh.SetInValue(value)
            thresh.ReplaceOutOn()
            thresh.SetOutValue(0)
            thresh.Update()

            contour = vtk.vtkContourFilter()
            contour.SetInputConnection(thresh.GetOutputPort())
            contour.SetValue(0, value)
        
            if smoothing and reduce_meshes:
                smoother = vtk.vtkWindowedSincPolyDataFilter()
                smoother.SetInputConnection(contour.GetOutputPort())
                smoother.SetNumberOfIterations(number_of_iterations)
                smoother.BoundarySmoothingOn()
                smoother.FeatureEdgeSmoothingOff()
                smoother.SetFeatureAngle(120.0)
                smoother.SetPassBand(0.05)
                smoother.NonManifoldSmoothingOn()
                smoother.NormalizeCoordinatesOn()
                smoother.Update()

                decimate = vtk.vtkDecimatePro()
                decimate.SetInputConnection(smoother.GetOutputPort())
                decimate.SetTargetReduction(percent_reductions)
                decimate.Update()

                writer = vtk.vtkSTLWriter()
                writer.SetInputConnection(decimate.GetOutputPort())
                writer.SetFileName(f"{self.out_dir}/{self.case_name}_{int(value)}.stl")
                writer.Write()
        
            elif smoothing:
                smoother = vtk.vtkWindowedSincPolyDataFilter()
                smoother.SetInputConnection(contour.GetOutputPort())
                smoother.SetNumberOfIterations(number_of_iterations)
                smoother.BoundarySmoothingOn()
                smoother.FeatureEdgeSmoothingOff()
                smoother.SetFeatureAngle(120.0)
                smoother.SetPassBand(0.05)
                smoother.NonManifoldSmoothingOn()
                smoother.NormalizeCoordinatesOn()
                smoother.Update()

                writer = vtk.vtkSTLWriter()
                writer.SetInputConnection(smoother.GetOutputPort())
                writer.SetFileName(f"{self.out_dir}/{self.case_name}_{int(value)}.stl")
                writer.Write()
        
            elif reduce_meshes:
                decimate = vtk.vtkDecimatePro()
                decimate.SetInputConnection(contour.GetOutputPort())
                decimate.SetTargetReduction(percent_reductions)
                decimate.Update()

                writer = vtk.vtkSTLWriter()
                writer.SetInputConnection(decimate.GetOutputPort())
                writer.SetFileName(f"{self.out_dir}/{self.case_name}_{int(value)}.stl")
                writer.Write()
        
            else:
                writer = vtk.vtkSTLWriter()
                writer.SetInputConnection(contour.GetOutputPort())
                writer.SetFileName(f"{self.out_dir}/{self.case_name}_{int(value)}.stl")
                writer.Write()