from pycad.converters import NiftiToPngConverter

path_to_nifti = './data/indata/one_file/case.nii.gz' # or .nii
path_to_nifti_dir = './data/indata/multiple_files/' 
path_to_save_png = './data/outdata'

converter = NiftiToPngConverter()
converter.convert_nifti_to_png(path_to_nifti, path_to_save_png, data_type='vol') # or data_type='seg' for segmentation.