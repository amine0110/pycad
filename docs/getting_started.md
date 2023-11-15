# Getting Started with PYCAD

Welcome to the PYCAD library! This guide will walk you through the basics of setting up and using our library for medical imaging.

## Prerequisites

Ensure you have Python 3.x installed. You can check your Python version using the command: python --version.

## Installation

### Option 1: Install using pip (Recommended)
You can directly install PYCAD from GitHub using pip:

```bash
pip install pycad-medic
```

### Option 2: Install using pip from source
You can directly install PYCAD from GitHub using pip:

```bash
pip install git+https://github.com/amine0110/pycad.git
```

### Option 3: Install by Cloning the Repository
#### 1. Clone the Repository:

Navigate to your desired directory and run:

```bash
git clone https://github.com/amine0110/pycad.git
```

#### 2. Navigate to the Cloned Directory:

```bash
cd pycad
```

#### 3. Install using setup.py:

```bash
python setup.py install
```
or 
```bash
pip install requirements.txt
```

### (Optional) Setting up a Virtual Environment

Before installing the library, it's often recommended to create a virtual environment for your projects to avoid potential conflicts between dependencies:

```bash
python -m venv pycad_env
source pycad_env/bin/activate  # On Windows, use `pycad_env\Scripts\activate`
```
Or
```bash
conda create -n my_env python=3.10
conda activate my_env
```

Then, proceed with either of the above installation options.

## Basic Usage

Multiple STL visualization using the visualization module of PYCAD:

```Python
from pycad.visualization import STLVisualizer
from glob import glob

stl_paths = glob("path/to/*.stl")


visualizer = STLVisualizer(stl_paths)
visualizer.visualize()
```

## Getting Help
- **Documentation**: Visit [PYCAD Documentation](https://github.com/amine0110/pycad/tree/main/docs) for comprehensive guides and API references.
- **Issues**: If you encounter any problems or have suggestions, please [file an issue](https://github.com/amine0110/pycad/issues) on our GitHub repository.

## Business Inquiries
For business-related questions, collaborations, or feedback, please reach out at [contact@pycad.co](mailto:contact@pycad.co).
