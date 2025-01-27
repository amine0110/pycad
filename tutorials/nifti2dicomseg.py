from pycad.converters import NiftiToDicomSeg

converter = NiftiToDicomSeg(
    dicom_dir=r"path/to/dicom/series/(scan)",
    nifti_file=r"path/to/nifti/mask"
)

# Print dimensions of both DICOM and NIfTI data for verification
converter.print_dimensions()

# Align the NIfTI mask with DICOM orientation
converter.align_mask()

# Create the DICOM-SEG file with custom parameters
converter.create_segmentation(
segment_label="liver",
algorithm_name="MySegmentationAlgorithm",
algorithm_version="v2.0",
manufacturer="MyCompany",
model_name="LiverSegmentationModel",
software_version="1.0.0",
device_serial="ABC123"
)

# Save the resulting DICOM-SEG file
converter.save_segmentation("liver_segmentation.dcm")