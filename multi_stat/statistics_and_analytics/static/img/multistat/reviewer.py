import os

FILES = [file for file in os.listdir() if file != "__pycache__"]


def check_files(filename):
    for file in FILES:
        if file == filename:
            return True
    return False
