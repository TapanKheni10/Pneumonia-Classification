import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

## These is a list of the files that will be created
list_of_files = [
    "app.py",
    "requirements.txt",
    "setup.py",
    "assests",
    "models",
    "research",
    "research/data_link.txt",
    "pages",
    "prediction_components",
    "prediction_components/__init__.py",
    "prediction_components/predict.py",
]

for file_path in list_of_files:
    if "." in file_path:
        Path(file_path).touch()
        logging.info(f"Created file at {file_path}")
    else:
        os.makedirs(file_path, exist_ok=True)
    logging.info(f"Created directory at {file_path}")