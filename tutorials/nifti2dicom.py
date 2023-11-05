from pycad.converters import NiftiToDicomConverter

path_to_nifti = './data/indata/one_file/case.nii.gz' # or .nii
path_to_nifti_dir = './data/indata/multiple_files/'
path_to_save_dicom = './data/outdata'

converter = NiftiToDicomConverter()
converter.nifti2dicom_1file(path_to_nifti, path_to_save_dicom) # convert one nifti file to dicom series
converter.nifti2dicom_mfiles(path_to_nifti_dir, path_to_save_dicom) # convert multiple nifti files to dicom series