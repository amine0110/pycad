from pycad.converters import NiftiToNrrdConverter

path_to_nifti = './data/indata/one_file/case.nii.gz'
path_to_nifti_dir = './data/indata/multiple_files/' # or .nii
path_to_save_nrrd = './data/outdata'

converter = NiftiToNrrdConverter()
converter.convert(path_to_nifti_dir, path_to_save_nrrd)