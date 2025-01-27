from pycad.converters import NiftiToDicomRT

selected_classes = {
        1: "liver",
        2: "heart"
    }
    
# Initialize and run the converter
converter = NiftiToDicomRT(
    nifti_path="path/to/nifti/mask",
    dicom_series_path="path/to/dicom/series/folder",
    output_path="path/to/output/rtstruct.dcm",
    selected_classes=selected_classes
)

# Perform the conversion
converter.convert()