#!/usr/bin/env python3
#
# Declaratively dynamically load the configured module and instantiate class
#
# - Activate Python virtual environment that has Aiko Services installed
# - Edit the CONFIGURATION_FILE and change parameters as needed
# - ./test.py  # Load module, instantiate class and invoke methods

import json   # json module 

from katabatic_spi import KatabaticSPI

from aiko_services.utilities import *

CONFIGURATION_FILE = "test.json"  # constant to retrieve the json config file. 

def main():
    print(f"[Katabatic test 0.0]")

    with open(CONFIGURATION_FILE, "r") as file:  # Open readonly
        configuration = json.load(file)  #configuration var is now a dict
    try:
        datagen_module_descriptor = configuration["datagen_module_descriptor"]  # unload the json dict 
        datagen_class_name = configuration["datagen_class_name"]
    except KeyError as key_error:
        raise SystemExit(       # SystemExit exception prints the below and immediately exits the interpreter
            f"Configuration '{CONFIGURATION_FILE}' doesn't have: {key_error}")

    diagnostic = None
    try:
        datagen_module = load_module(datagen_module_descriptor) # using aiko method
        datagen_class = getattr(datagen_module, datagen_class_name)
    except FileNotFoundError:
        diagnostic = "couldn't be found"
    except Exception:
        diagnostic = "couldn't be loaded"
    if diagnostic:
        raise SystemExit(f"Module {datagen_module_descriptor} {diagnostic}")

    data_gen_ml = datagen_class() #  create an instance of the datagen class
    if not isinstance(data_gen_ml, KatabaticSPI):       # Handles edge cases where the model isn't compatible with the SPI
        raise SystemExit(f"{datagen_class_name} doesn't implement KatabaticSPI")

    data_gen_ml.load_data(None)
    data_gen_ml.split_data(None, None)
    data_gen_ml.fit_model(None)

if __name__ == "__main__":
    main()
