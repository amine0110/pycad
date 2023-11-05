from pycad.converters import Nifti2StlConverter

path_to_nifti = './data/indata/one_file/case.nii.gz'
path_to_save_stl = './data/outdata'

converter = Nifti2StlConverter(path_to_nifti, path_to_save_stl)
converter.nifti2stl_vtk()