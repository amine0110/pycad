# Copyright (c) 2023 PYCAD
# This file is part of the PYCAD library and is released under the MIT License:
# https://github.com/amine0110/pycad/blob/main/LICENSE


import os
import pydicom
from pydicom.filereader import read_dicomdir
from glob import glob
from tqdm import tqdm

class DicomAnonymizer:
    '''
    This module is to help anonymize dicom files. 
    The tags to be anonymized are chosen by the user, when you run the code, you will be able to write the different tags (from the list) that you want to anonymize.

    Params:
    - input_dir: the directory to the input dicom files.
    - output_dir: the directory to the output (anonymized) dicom files.

    #### Example of usage:
    ```Python
    from pycad.datasets import DicomAnonymizer
    
    input_dir = 'path/to/input/dicom/dir'
    output_dir = 'path/to/output/anonymized/dir'
    anonymizer = DicomAnonymizer(input_dir, output_dir)
    anonymizer.run()
    ```
    '''
    def __init__(self, input_dir, output_dir):
        self.input_dir = input_dir
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def list_anonymization_fields(self):
        # List of common DICOM fields that are typically anonymized.
        # This list can be modified as needed.
        anonymization_fields = [
            'PatientName', 'PatientID', 'PatientBirthDate', 
            'PatientSex', 'StudyInstanceUID', 'SeriesInstanceUID', 
            'StudyID', 'InstitutionName', 'ReferringPhysicianName'
        ]
        print("The following fields can be anonymized:")
        for field in anonymization_fields:
            print(f"- {field}")
        return anonymization_fields
    
    def anonymize_dicoms(self, fields_to_anonymize):
        dicom_files = glob(os.path.join(self.input_dir, '*.dcm'))
        for file_path in tqdm(dicom_files, desc="Anonymizing"):
            try:
                # Read the DICOM file
                dicom = pydicom.read_file(file_path)
                
                # Anonymize the fields specified
                for field in fields_to_anonymize:
                    if field in dicom:
                        dicom.data_element(field).value = 'Anonymized'
                
                # Save the anonymized DICOM file
                dicom.save_as(os.path.join(self.output_dir, os.path.basename(file_path)))
            except Exception as e:
                print(f"Error anonymizing {file_path}: {e}")
    
    def run(self):
        # List fields that can be anonymized
        available_fields = self.list_anonymization_fields()
        
        # Ask the user which fields to anonymize
        fields_to_anonymize = input("Enter the fields you want to anonymize, separated by commas: ").split(',')
        fields_to_anonymize = [field.strip() for field in fields_to_anonymize if field.strip() in available_fields]
        
        # Confirm with the user before proceeding
        print("The following fields will be anonymized:")
        for field in fields_to_anonymize:
            print(f"- {field}")
        confirm = input("Do you want to proceed with anonymization? (yes/no): ")
        if confirm.lower() == 'yes':
            # Perform the anonymization
            self.anonymize_dicoms(fields_to_anonymize)
            print("Anonymization complete.")
        else:
            print("Anonymization canceled.")