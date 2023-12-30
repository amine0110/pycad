import unittest
import numpy as np
import nibabel as nib
import os
from pycad.datasets import MultiClassNiftiMerger  

class TestMultiClassNiftiMerger(unittest.TestCase):
    @staticmethod
    def create_sample_nifti_file(filename, data):
        """
        Create a sample NIfTI file with given data.
        """
        nifti_img = nib.Nifti1Image(data, affine=np.eye(4))
        nib.save(nifti_img, filename)

    def test_merge_classes(self):
        # Create sample class files
        class1_data = np.zeros((5, 5, 5))
        class1_data[2:4, 2:4, 2:4] = 1  # Some sample segmentation
        self.create_sample_nifti_file('class1.nii', class1_data)

        class2_data = np.zeros((5, 5, 5))
        class2_data[1:3, 1:3, 1:3] = 1  # Some sample segmentation
        self.create_sample_nifti_file('class2.nii', class2_data)

        # Create a dummy volume file
        volume_data = np.random.rand(5, 5, 5)
        self.create_sample_nifti_file('volume.nii', volume_data)

        # Process merging
        merger = MultiClassNiftiMerger('volume.nii', ['class1.nii', 'class2.nii'], '.', move_volumes=False)
        merger.combine_classes()

        # Load the merged file and check if classes are merged correctly
        merged_nifti = nib.load('segmentations/combined.nii')
        merged_data = merged_nifti.get_fdata()

        # Check if the merged data has the expected class labels
        self.assertEqual(merged_data[3, 3, 3], 1)  # Belongs to class 1
        self.assertEqual(merged_data[2, 2, 2], 2)  # Belongs to class 2

        # Clean up the created files
        os.remove('class1.nii')
        os.remove('class2.nii')
        os.remove('volume.nii')
        os.remove('segmentations/combined.nii')

if __name__ == '__main__':
    unittest.main()
