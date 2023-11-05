from pycad.converters import NrrdToDicomConverter

path_to_nrrd = './data/indata/one_file/case.nrrd'
path_to_nrrd_dir = './data/indata/multiple_files/'
path_to_save_dicom = './data/outdata'

converter = NrrdToDicomConverter()
converter.nrrd2dicom_1file(path_to_nrrd, path_to_save_dicom) # convert one nrrd file to dicom series
converter.nrrd2dicom_mfiles(path_to_nrrd_dir, path_to_save_dicom) # convert multiple nrrd files to dicom series