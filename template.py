import os
from pathlib import Path  ## this library takes care of path ie."/" or "\"
import logging   ## looging lib contains: Debug, Info, Warn, Error

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s: ') ## getting only INFO details from logger

package_name = "deepClassifier"

## creating the template folders 
list_of_files = [
   ".github/workflows/.gitkeep",   ## gitkeep doesn't allow the empty folders to add in github or production
   f"src/{package_name}/__init__.py", 
   f"src/{package_name}/components/__init__.py", 
   f"src/{package_name}/utils/__init__.py", 
   f"src/{package_name}/config/__init__.py", 
   f"src/{package_name}/pipeline/__init__.py", 
   f"src/{package_name}/entity/__init__.py", 
   f"src/{package_name}/constants/__init__.py",
   "tests/__init__.py",
   "tests/unit/__init__.py",          ## unit level testing means testing any classes that we creates
   "tests/integration/__init__.py",   ## integration tests for testing the pipelines
   "configs/config.yaml",
   "dvc.yaml",                          ## dvc --> data version pipeline
   "params.yaml",                       ## params --> keep all training parameter at one place
   "init_setup.sh",                     ## init_setup --> auto environment setup
   "requirements.txt",                  ## pip install -r requirements.txt
   "requirements_dev.txt",              ## required specially for development purposes
   "setup.py",
   "setup.cfg",
   "pyproject.toml",                   ## required if you are creating your own python packages
   "tox.ini",                          ## testing project locally
   "research/trials.ipynb",            ## for trial in jupyter notebook
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)  ## split the directory and the file seprately

    if filedir != "":                           ## if directory is not empty then create directory
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): ##0 letter filesize then create file
        with open(filepath, "w") as f:                           ## This avoid over-writing the files
            pass                                                           ## create an empty file
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")