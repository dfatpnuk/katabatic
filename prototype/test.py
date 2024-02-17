#!/usr/bin/env python3
#
# Declaratively dynamically load the configured module and instantiate class
#
# - Activate Python virtual environment that has Aiko Services installed
# - Edit the CONFIGURATION_FILE and change parameters as needed
# - ./test.py  # Load module, instantiate class and invoke methods
#
# To Do
# ~~~~~
# - Improve command line handling with the "click" module

import json
from multiprocessing import Process
import os
import sys

from katabatic_spi import KatabaticSPI

from aiko_services.utilities import *

CONFIGURATION_FILE = "test.json"

def run_datagen_model(datagen_model_name):
    print(f"--------------------------")
    print(f"module name:    {__name__}")
    print(f"parent process: {os.getppid()}")
    print(f"process id:     {os.getpid()}")

    with open(CONFIGURATION_FILE, "r") as file:
        configuration = json.load(file)

        if not datagen_model_name in configuration:
            raise SystemExit(
                f"Configuration '{CONFIGURATION_FILE}' doesn't have DataGen model: {datagen_model_name}")
        configuration = configuration[datagen_model_name]

    try:
        datagen_module_descriptor = configuration["datagen_module_descriptor"]
        datagen_class_name = configuration["datagen_class_name"]
    except KeyError as key_error:
        raise SystemExit(
            f"Configuration '{CONFIGURATION_FILE}' doesn't have: {key_error}")

    diagnostic = None
    try:
        datagen_module = load_module(datagen_module_descriptor)
        datagen_class = getattr(datagen_module, datagen_class_name)
    except FileNotFoundError:
        diagnostic = "couldn't be found"
    except Exception:
        diagnostic = "couldn't be loaded"
    if diagnostic:
        raise SystemExit(f"Module {datagen_module_descriptor} {diagnostic}")

    data_gen_ml = datagen_class()
    if not isinstance(data_gen_ml, KatabaticSPI):
        raise SystemExit(f"{datagen_class_name} doesn't implement KatabaticSPI")

    data_gen_ml.load_data(None)
    data_gen_ml.split_data(None, None)
    data_gen_ml.fit_model(None)

if __name__ == "__main__":
    print(f"[Katabatic test 0.1]")
    print(f"module name:    {__name__}")
    print(f"parent process: {os.getppid()}")
    print(f"process id:     {os.getpid()}")

    if len(sys.argv) < 2:
        raise SystemExit("Usage: test.py DATAGEN_MODEL_NAME ...")
    arguments = sys.argv[1:]

    for index in range(len(arguments)):
    #   p = Process(target=f, args=("./test.sh {arguments[index]},))
    #   p.start()
    #   p.join()
    #   READ DATA FROM CHILD PROCESS

        datagen_model_name = arguments[index]  # Move to child proess
        run_datagen_model(datagen_model_name)  # Move to child proess

    # COMPARE AND GRAPH ALL THE CHILD PROCESS RESULTS !
