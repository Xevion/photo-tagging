import io
import sys
import os
import time
import rawpy
import imageio
import progressbar
import shutil
import logging

from google.cloud import vision

from .xmp import XMPParser
from .process import FileProcessor
from . import INPUT_PATH, TEMP_PATH, OUTPUT_PATH, PROCESSING_PATH
from . import RAW_EXTS, LOSSY_EXTS

log = logging.getLogger('app')

def run():
    client = vision.ImageAnnotatorClient()

    # Find files we want to process based on if they have a corresponding .XMP
    log.info('Locating processable files...')
    files = os.listdir(INPUT_PATH)
    select = [file for file in files if os.path.splitext(file)[1] != '.xmp']
    log.info(f'Found {len(files)} valid files')

    # Create the 'temp' directory
    log.info('Creating temporary processing directory')
    os.makedirs(TEMP_PATH)
    os.makedirs(OUTPUT_PATH)
    
    try:
        # Process files
        for index, file in progressbar.progressbar(list(enumerate(select)), redirect_stdout=True, term_width=110):
            _, ext = os.path.splitext(file)
            ext = ext[1:].lower()
            if ext in LOSSY_EXTS or ext in RAW_EXTS:
                process = FileProcessor(file)
                log.info(f"Processing file '{file}'...")
                process.run(client)
    except Exception as error:
        log.error(str(error))
        log.warning(
            'Removing temporary directory before raising exception.')
        os.rmdir(TEMP_PATH)
        raise

    # Remove the directory, we are done here
    log.info('Removing temporary directory.')
    os.rmdir(TEMP_PATH)
