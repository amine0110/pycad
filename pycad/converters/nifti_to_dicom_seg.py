# Copyright (c) 2023 PYCAD
# This file is part of the PYCAD library and is released under the MIT License:
# https://github.com/amine0110/pycad/blob/main/LICENSE
# More information can be found in the original documentation: https://highdicom.readthedocs.io/en/latest/quickstart.html#creating-segmentation-seg-images


from pathlib import Path
import highdicom as hd
import numpy as np
from pydicom.sr.codedict import codes
from pydicom.filereader import dcmread
import nibabel as nib


class NiftiToDicomSeg:
    def __init__(self, dicom_dir, nifti_file):
        self.series_dir = Path(dicom_dir)
        self.image_files = self.series_dir.glob('*.dcm')
        self.nifti_file = nib.load(nifti_file)
        self.mask_array = self.nifti_file.get_fdata()
        self.image_datasets = [dcmread(str(f)) for f in self.image_files]
        
    def print_dimensions(self):
        print("DICOM", len(self.image_datasets))
        print("DICOM", self.image_datasets[0].Rows)
        print("DICOM", self.image_datasets[0].Columns)
        print("NIFTI", self.mask_array.shape)
        print("NIfTI Affine Matrix:")
        print(self.nifti_file.affine)

    def align_mask(self):
        # Adjust the mask orientation to align with DICOM slices
        mask = np.transpose(self.mask_array, (2, 1, 0))  # Transpose to match DICOM dimensions
        mask = np.flip(mask, axis=0)  # Flip along the z-axis if needed
        mask = np.flip(mask, axis=1)  # Flip along the y-axis if needed
        
        # Debug info
        print("Updated mask shape:", mask.shape)
        print("Unique values in the mask after transpose/flip:", np.unique(mask))
        
        # Convert integer mask (0/1) to boolean mask (False/True)
        self.mask = mask.astype(bool)
        print("After conversion to bool:", np.unique(self.mask))
        print("Shape after bool", self.mask.shape)

    def create_empty_mask(self):
        return np.zeros(
            shape=(
                len(self.image_datasets),
                self.image_datasets[0].Rows,
                self.image_datasets[0].Columns
            ),
            dtype=np.bool
        )

    def create_segmentation(self, segment_label='liver', algorithm_name='test', 
                          algorithm_version='v1.0', manufacturer='Manufacturer',
                          model_name='Model', software_version='v1', 
                          device_serial='Device XYZ'):
        # Describe the algorithm that created the segmentation
        algorithm_identification = hd.AlgorithmIdentificationSequence(
            name=algorithm_name,
            version=algorithm_version,
            family=codes.cid7162.ArtificialIntelligence
        )

        # Describe the segment
        description_segment_1 = hd.seg.SegmentDescription(
            segment_number=1,
            segment_label=segment_label,
            segmented_property_category=codes.cid7150.Tissue,
            segmented_property_type=codes.cid7166.ConnectiveTissue,
            algorithm_type=hd.seg.SegmentAlgorithmTypeValues.AUTOMATIC,
            algorithm_identification=algorithm_identification,
            tracking_uid=hd.UID(),
            tracking_id='test segmentation of computed tomography image'
        )

        # Create the Segmentation instance
        self.seg_dataset = hd.seg.Segmentation(
            source_images=self.image_datasets,
            pixel_array=self.mask,
            segmentation_type=hd.seg.SegmentationTypeValues.BINARY,
            segment_descriptions=[description_segment_1],
            series_instance_uid=hd.UID(),
            series_number=2,
            sop_instance_uid=hd.UID(),
            instance_number=1,
            manufacturer=manufacturer,
            manufacturer_model_name=model_name,
            software_versions=software_version,
            device_serial_number=device_serial,
        )

    def save_segmentation(self, output_file="seg.dcm"):
        self.seg_dataset.save_as(output_file)
        print("Segmentation DICOM file saved successfully!")

