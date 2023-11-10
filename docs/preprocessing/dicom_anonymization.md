# DicomAnonymizer Documentation

## Overview
The `DicomAnonymizer` module within the PYCAD library provides users with the capability to anonymize DICOM files. Anonymization of medical images is a critical process in ensuring the privacy of patients' personal information, especially when sharing medical data for research or educational purposes. The `DicomAnonymizer` focuses on customizable anonymization, allowing users to select specific DICOM tags for anonymization according to their requirements or institutional policies.
## Features
-   Anonymize any specified DICOM tags.
-   Simple CLI interface for selecting tags to anonymize.
-   Support for batch processing of multiple DICOM files.
-   Verification step before the anonymization process is executed.
## Prerequisites
-   PYCAD library installed.
-   Input directory with DICOM files ready for anonymization.
-   Output directory where anonymized DICOM files will be saved.
## Parameters
-   `input_dir`: Directory containing original DICOM files.
-   `output_dir`: Directory where anonymized DICOM files will be saved.
## Usage
### Step 1: Importing and Initializing
```python
from pycad.datasets import DicomAnonymizer

input_dir = 'path/to/input/dicom/dir'
output_dir = 'path/to/output/anonymized/dir'
anonymizer = DicomAnonymizer(input_dir, output_dir)
```
### Step 2: Listing Fields
Upon initialization, `DicomAnonymizer` can provide a list of commonly anonymized DICOM tags.
```python
anonymizer.list_anonymization_fields()
```
### Step 3: Running Anonymization
```python
anonymizer.run()
```
When `run()` is called, the user is prompted to enter the tags they wish to anonymize. After confirmation, the anonymization process begins.
## Anonymization Fields
By default, the anonymization process can include the following fields, but it can be customized as needed:
-   PatientName
-   PatientID
-   PatientBirthDate
-   PatientSex
-   StudyInstanceUID
-   SeriesInstanceUID
-   StudyID
-   InstitutionName
-   ReferringPhysicianName
## Example
```python

# Create an instance of the DicomAnonymizer
anonymizer = DicomAnonymizer('path/to/dicom_files', 'path/to/save_anonymized_files')

# Print out the fields available for anonymization
anonymizer.list_anonymization_fields()

# Run the anonymization process
anonymizer.run()

```
## Note
Anonymization is irreversible; it is recommended to keep a backup of the original data before proceeding. The responsibility for ensuring that all necessary DICOM tags are anonymized according to relevant regulations and ethical guidelines lies with the user.
## License
This `DicomAnonymizer` module is part of the PYCAD library and is released under the MIT License. For more details, see the [LICENSE](https://github.com/amine0110/pycad/blob/main/LICENSE) file.