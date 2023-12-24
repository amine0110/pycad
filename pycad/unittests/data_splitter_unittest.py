import unittest
import os

class TestDataConsistency(unittest.TestCase):
    '''
    This is the unit test for the DataSplitter module. It will test whether the same filenames are in the images and labels folder.
    '''
    @classmethod
    def setUpClass(cls):
        cls.output_dir = cls.output_dir if hasattr(cls, 'output_dir') else 'default/path'
        cls.sets = ['train', 'valid', 'test']

    @classmethod
    def set_output_dir(cls, new_output_dir):
        cls.output_dir = new_output_dir

    def test_filename_consistency(self):
        for set_name in self.sets:
            with self.subTest(set=set_name):
                images_dir = os.path.join(self.output_dir, set_name, 'images')
                labels_dir = os.path.join(self.output_dir, set_name, 'labels')

                # Ensure both directories exist
                self.assertTrue(os.path.isdir(images_dir))
                self.assertTrue(os.path.isdir(labels_dir))

                # Extract filenames without extension
                image_files = {os.path.splitext(file)[0] for file in os.listdir(images_dir)}
                label_files = {os.path.splitext(file)[0] for file in os.listdir(labels_dir)}

                # Assert that the sets are equal
                self.assertEqual(image_files, label_files, f"Mismatch in {set_name} set")

def run_tests(output_dir):
    TestDataConsistency.set_output_dir(output_dir)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDataConsistency)
    unittest.TextTestRunner().run(suite)

# Example of usage
if __name__ == "__main__":
    output_dir = 'path to the output path from the data splitter module'
    run_tests(output_dir)

