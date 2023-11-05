from pycad.converters import DicomToNrrdConverter

path_to_dicom = './data/indata/one_file/'
path_to_dicom_dir = './data/indata/multiple_files/'
path_to_save_nrrd = './data/outdata/'

converter = DicomToNrrdConverter(10)
converter.convert(path_to_dicom_dir, path_to_save_nrrd)