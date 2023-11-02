# Copyright (c) 2023 PYCAD
# This file is part of the PYCAD library and is released under the MIT License:
# https://github.com/amine0110/pycad/blob/main/LICENSE


import argparse
from . import __version__

def main():
    parser = argparse.ArgumentParser(description="PYCAD library CLI.")
    parser.add_argument("--version", action="version", version=f"PYCAD version {__version__}")
    args = parser.parse_args()

if __name__ == "__main__":
    main()
