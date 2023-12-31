# Copyright (c) 2023 PYCAD
# This file is part of the PYCAD library and is released under the MIT License:
# https://github.com/amine0110/pycad/blob/main/LICENSE


import os
import gdown
import zipfile
import requests

class HippocampusDataset:
    '''
    This class is for the hippocampus segmentation dataset from the decathlon dataset.
    You can get more information about it using `info()` function.

    ### Example usage

    ```Python
    from pycad.dataset.segmentation.decathlon import HippocampusDataset
    
    hippocampus_dataset = HippocampusDataset()
    hippocampus_dataset.info()  # Print dataset information
    hippocampus_dataset.download('100')  # Download and extract subgroup 100
    ```
    '''
    def __init__(self, dataset_size=260):
        self.dataset_size = dataset_size
        self.dataset_subgroups = {
            '100': 'https://drive.google.com/uc?id=1ptHJt0N4D01Jc7k3mrlzL_YIlY-GQijA',
            'all': 'https://drive.google.com/uc?id=1MGUJuXOHKWJoOXv22FNunTVX0HfsVxQN'
        }
        self.base_path = 'datasets/'

    def info(self):
        print(f"Hippocampus Dataset from Decathlon dataset. This is a collection of CT scans with means these are 3D volumes.")
        print(f"Total Cases: {self.dataset_size}")
        print(f"Subgroups: 100, {self.dataset_size}")
        print("Source: http://medicaldecathlon.com/")

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
            file_path = os.path.join(path, f'hippocampus{subgroup}.zip')
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