from pycad.converters import NrrdToNiftiConverter

path_to_nrrd = './data/indata/one_file/case.nrrd'
path_to_nrrd_dir = './data/indata/multiple_files/'
path_to_save_nifti = './data/outdata'

converter = NrrdToNiftiConverter()
converter.convert(path_to_nrrd_dir, path_to_save_nifti)