# This file declaratively loads the configured module and instantiates the Tabular Data Generative Model (TDGM) class.
# To change the Tabular Data Generative Model (TDGM) used, update 'katabatic_config.json'

import os
import sys
import json
from multiprocessing import Process
from katabatic_spi import KatabaticModelSPI  # Katabatic Model SPI 

from importer import load_module   # Aiko Services module loader

CONFIG_FILE = "katabatic_config.json" #Constant to retrieve config file

def run_model(model_name):
    print(f"--------------------------")
    print(f"module name:    {__name__}")
    print(f"parent process: {os.getppid()}")
    print(f"process id:     {os.getpid()}")

    with open(CONFIG_FILE, "r") as file: # Open config file as read only
        config = json.load(file) # config is a dict of dicts, each containing config variables for a model.

        if not model_name in config:
            raise SystemExit(
                f"Configuration '{CONFIG_FILE}' doesn't have model: {model_name}")
        config = config[model_name] # now config is just one dict, containing config variables of a single model.

    try:
        module_name = config["tdgm_module_name"]
        class_name = config["tdgm_class_name"]
    except KeyError as key_error:
        raise SystemExit(   # SystemExit exception prints the below and immediately exits the interpreter
            f"Configuration file '{CONFIG_FILE}' does not contain: {key_error}")
    
    diagnostic = None # initialise an empty diagnostic variable
    try:
        #breakpoint()
        module = load_module(module_name)  # load_module method from Aiko services
        model_class = getattr(module, class_name)
        
    except FileNotFoundError:
        diagnostic = "could not be found."
    except Exception as exception:
        diagnostic = f"could not be loaded: {exception}"
    if diagnostic:
        raise SystemExit(f"Module {module_name} {diagnostic}")

    model = model_class() # Create an instance of the model class
    if not isinstance(model, KatabaticModelSPI):
        raise SystemExit(f"{class_name} doesn't implement KatabaticModelSPI.")
    
    # TODO: Add some demo data here
    X_train = 0
    y_train = 0

    model.load_model()
    model.fit(X_train, y_train)
    model.generate()

if __name__ == "__main__":
    print(f"[Katabatic test 0.1]")
    print(f"module name:    {__name__}")
    print(f"parent process: {os.getppid()}")
    print(f"process id:     {os.getpid()}")

    if len(sys.argv) < 2:
        raise SystemExit("Usage: katabatic.py MODEL_NAME ...")
    arguments = sys.argv[1:]

    for index in range(len(arguments)):
        model_name = arguments[index]  # Move to child proess
        run_model(model_name)  # Move to child proess