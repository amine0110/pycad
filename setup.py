from setuptools import setup, find_packages

setup(
    name='pycad-medic',
    version='0.0.3',
    author='Mohammed El Amine Mokhtari',
    author_email='mohammed@pycad.co',
    packages=find_packages(),
    description='A medical imaging library for Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://pycad.co',
    project_urls={
        "Documentation": "https://pycad.co",
        "Source Code": "https://github.com/amine0110/pycad",
    },
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
