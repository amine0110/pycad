from setuptools import setup, find_packages

setup(
    name='pycad',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'numpy==1.26.0',
        'tqdm==4.66.1',
        'glob2',
        'SimpleITK==2.3.0',
        'pillow==10.0.1',
        'pydicom==2.4.3',
        'vtk==9.2.6',
        'vedo==2023.4.6',
        'scikit-image==0.22.0',
        'opencv-python==4.8.1.78',
        'pytest-shutil',
        'nibabel==3.2.2',
        'scikit-learn==1.1.2'
        # other libraries with their versions
    ],
    entry_points={
        'console_scripts': [
            'pycad=pycad.cli:main',
        ],
    },
)
