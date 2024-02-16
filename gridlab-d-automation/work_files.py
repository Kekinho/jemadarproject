# -*- coding: utf-8 -*-

import os
import glob


def delete_files_in_folder_output_files_gridlab():
    py_files = glob.glob('output_files_gridlab/*.csv')
    print(py_files)
    for py_file in py_files:
        try:
            os.remove(py_file)
        except OSError as e:
            print(f"Error:{e.strerror}")


def delete_files_in_folder_data_gridlab():
    py_files = glob.glob('data_gridlab/*.csv')
    print(py_files)
    for py_file in py_files:
        try:
            os.remove(py_file)
        except OSError as e:
            print(f"Error:{e.strerror}")

