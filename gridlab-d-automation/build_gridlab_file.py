# -*- coding: utf-8 -*-

import gridlab_lib as glm_lib
import os
from pathlib import Path

# paramethers
from gridlab_lib import Schedule

tmyfile = "WA-Seattle.tmy2"
name_file_gridlab = 'gridlab-d_input_file.glm'

def write_file_microgrid(microgrid):
    gridlab_input_file = open(name_file_gridlab, 'w')
    gridlab_input_file.write(glm_lib.Clock(1).__str__())
    gridlab_input_file.write(glm_lib.create_modules())
    gridlab_input_file.write(glm_lib.create_object_climate(tmyfile))
    gridlab_input_file.write(glm_lib.create_object_triplex_meter())
    gridlab_input_file.write(str(microgrid))
    gridlab_input_file.close()


def get_path_gridlab_temp_files():
    return os.path.join(os.getcwd(), "output_files_gridlab")


def run_gridlab_d_file():
    Path("./output_files_gridlab").mkdir(exist_ok=True)
    current_path = os.getcwd()
    os.chdir(os.path.join(current_path, "output_files_gridlab"))
    command = os.path.join(current_path, name_file_gridlab)
    os.system("gridlabd " + command)
    os.chdir(current_path)



