from setuptools import setup, find_packages

setup(
    name='pycad',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'tqdm',
        'glob2',
        'SimpleITK',
        'pillow',
        'pydicom',
        'vtk',
        'vedo',
        'scikit-image',
        'opencv-python',
        'pytest-shutil',
        'ultralytics'
        # other libraries
    ],
)
