# DicomCTWindowing Documentation
## Preprocessing DICOM CT Images with Windowing

The `DicomCTWindowing` class is designed to facilitate the preprocessing of DICOM CT (Computed Tomography) images by applying a technique known as windowing or level adjustment. This technique is critical in medical imaging, as it allows radiologists and medical AI systems to visualize different structures in the CT images more effectively.

![CT windowing](../../assets/ct_windowing.png?raw=true)

## What is Windowing (Level Adjustment)?
Windowing, also known as contrast stretching or level adjustment, is a technique used to enhance the visibility of structures in CT images by adjusting the range of Hounsfield Units (HU) displayed on the image. The HU is a quantitative scale for describing radiodensity, where water is defined to have a value of 0 HU, air is approximately -1000 HU, and dense bone structures can reach upwards of +1000 HU.

The windowing process is defined by two main parameters:

- **Window Width (WW)**: This determines the range of HU that will be displayed. A larger window width includes a broader range of HU, making the image look less contrasted, whereas a smaller window width results in higher contrast, showing fewer variations in density.

- **Window Center (WC)**: This indicates the midpoint of the HU range. It's the HU value that will be mapped to the middle of the grayscale.

The transformation of HU to grayscale pixel intensity $I$ can be defined by the following equation:


$I(x, y) = \frac{HU(x, y) - (WC - \frac{WW}{2})}{WW} \times 255$


Where $I(x, y)$ is the intensity of the pixel at position $(x, y)$ in the output image, $HU(x, y)$ is the original HU value of that pixel, $WC$ is the window center, and $WW$ is the window width.

The result of this equation is then clamped to the range [0, 255] to fit the grayscale range of pixel values.

## Features of DicomCTWindowing
- **Versatility**: Can process a single series or multiple series of DICOM files located in different folders.
- **Customizable Windowing**: Allows the user to set the window width and center according to the anatomical structure of interest (e.g., lung, bone, brain).
- **Visualization**: Optionally display an example slice before and after processing for quick quality assurance.
- **Robust**: Handles exceptions and errors with proper logging.

## Usage
### Initialization

```Python
from pycad.preprocessing import DicomCTWindowing

converter = DicomCTWindowing(window_center, window_width, visualize=True)
```
- `window_center`: The center of the window used for windowing.
- `window_width`: The width of the window used for windowing.
- `visualize`: Whether to show an example slice before and after windowing at the end of processing.

## Processing a Directory
```Python
converter.convert(dicom_dir, output_dir)
```

- `dicom_dir`: Directory containing DICOM files for a single CT series.
- `output_dir`: Directory where the processed images will be saved.

## Processing Multiple Directories
If you have multiple directories to process, simply pass a list of directory paths to the `convert` method:

```Python
converter.convert([dicom_dir1, dicom_dir2], output_dir)
```

## Integration
The `DicomCTWindowing` is designed to be a plug-and-play component in medical image preprocessing pipelines. It is especially suited for preparing datasets for machine learning models, where specific tissue visualization is crucial.
