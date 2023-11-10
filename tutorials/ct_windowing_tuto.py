# This is a tutorial about how to use pycad to perform the windowing on CT scans. 
# This helps change the contrast of the scan to something more clear in visualization.

from pycad.preprocessing import CTWindowing
import os

dicom_dir = "path/to/dicom/series"  # Directory with DICOM files.
output_dir = "path/to/output"
window_center = 40
window_width = 400
converter = CTWindowing(window_center, window_width, visualize=True)
converter.convert(dicom_dir, output_dir)

# And if you have a directory that contains directories of dicom series, then use this:
path_dirs = [os.path.join(path_dirs, dir) for dir in os.listdir(dicom_dir) if os.path.isdir(os.path.join(path_dirs, dir))]
converter.convert(path_dirs, output_dir)