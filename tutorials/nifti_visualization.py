from pycad.visualization import NIFTIVisualizer

path_to_nifti = './data/indata/one_file/liver_4.nii.gz'

visualizer = NIFTIVisualizer(path_to_nifti)
visualizer.visualize()