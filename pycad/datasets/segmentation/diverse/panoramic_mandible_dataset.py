# Copyright (c) 2023 PYCAD
# This file is part of the PYCAD library and is released under the MIT License:
# https://github.com/amine0110/pycad/blob/main/LICENSE


import os
import gdown
import zipfile
import requests

class PanMandibleDataset:
    '''
    This class is for the panoramic mandible segmentation dataset from the total segmentator dataset.
    You can get more information about it using `info()` function.

    ### Example usage

    ```Python
    from pycad.dataset.segmentation.diverse import PanMandibleDataset
    
    pan_mandible_dataset = PanMandibleDataset()
    pan_mandible_dataset.info()  # Print dataset information
    pan_mandible_dataset.download('all')  # Download and extract subgroup 100
    ```
    '''
    def __init__(self, dataset_size=116):
        self.dataset_size = dataset_size
        self.dataset_subgroups = {
            'all': 'https://drive.google.com/uc?id=12G07KVxcHic_TsSG2FAQHw9hMs29_Iyy'
        }
        self.base_path = 'datasets/'

    def info(self):
        print(f"This dataset consists of anonymized and deidentified panoramic dental X-rays of 116 patients, taken at Noor Medical Imaging Center, Qom, Iran. The subjects cover a wide range of dental conditions from healthy, to partial and complete edentulous cases. The mandibles of all cases are manually segmented by two dentists. This is a 2D dataset.")
        print(f"Total Cases: {self.dataset_size}")
        print(f"Subgroups: {self.dataset_size}")
        print("Source: https://data.mendeley.com/datasets/hxt48yk462/2")

    def download(self, subgroup, path=None):
        if subgroup not in self.dataset_subgroups:
            print(f"No subgroup {subgroup} available.")
            return

        if subgroup.isdigit() and int(subgroup) > self.dataset_size:
            print(f"Subgroup {subgroup} exceeds dataset size.")
            return

        download_url = self.dataset_subgroups[subgroup]
        save_path = path if path else self.base_path
        self._download_and_extract(download_url, save_path, subgroup)

    def _download_and_extract(self, url, path, subgroup):
        if not os.path.exists(path):
            os.makedirs(path)

        try:
            file_path = os.path.join(path, f'pan_mandible{subgroup}.zip')
            gdown.download(url, file_path, quiet=False)

            # Check file size after download
            if os.path.getsize(file_path) < 1024:  # Example size threshold (1KB)
                print("Downloaded file is too small, might be an error.")
                return

            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(path)
            print(f"Downloaded and extracted at {path}")

            # Delete the zip file after extraction
            os.remove(file_path)
            print(f"Deleted zip file: {file_path}")

        except requests.exceptions.RequestException as e:
            print("Error in downloading the file: ", e)
        except zipfile.BadZipFile:
            print("Error in extracting the file: File may be corrupted or not a zip file.")
        except Exception as e:
            print("An unexpected error occurred: ", e)
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"Deleted incomplete zip file: {file_path}")