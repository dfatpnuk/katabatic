#!/usr/bin/env python3
#
# Declaratively dynamically load the configured module and instantiate class
#
# - Activate Python virtual environment that has Aiko Services installed
# - Edit the CONFIGURATION_FILE and change parameters as needed
# - ./test.py  # Load module, instantiate class and invoke methods

import json

from katabatic_spi import KatabaticSPI

from aiko_services.utilities import *

CONFIGURATION_FILE = "test.json"

def main():
    print(f"[Katabatic test 0.0]")

    with open(CONFIGURATION_FILE, "r") as file:
        configuration = json.load(file)
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
        raise SystemExit(f"Module {DATAGEN_MODULE_DESCRIPTOR} {diagnostic}")

    data_gen_ml = datagen_class()
    if not isinstance(data_gen_ml, KatabaticSPI):
        raise SystemExit(f"{DATAGEN_CLASS_NAME} doesn't implement KatabaticSPI")

    data_gen_ml.load_data(None)
    data_gen_ml.split_data(None, None)
    data_gen_ml.fit_model(None)

if __name__ == "__main__":
    main()
