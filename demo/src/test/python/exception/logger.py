import logging
import os
import sys
import datetime

def configure_logger(log_dir):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file_path = os.path.join(log_dir, f"log_{timestamp}.log")
    file_handler = logging.FileHandler(log_file_path, mode='a')  

    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(message)s')

    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
