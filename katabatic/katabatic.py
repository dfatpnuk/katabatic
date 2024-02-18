# This file declaratively loads the configured module and instantiates the Tabular Data Generative Model (TDGM) class.
# To change the Tabular Data Generative Model (TDGM) used, update 'katabatic_config.json'

import json  #json module for config
from katabatic_spi import KatabaticModelSPI  #Katabatic SPI 
from importer import load_module   #Aiko Services

CONFIG_FILE = "katabatic_config.json" #Constant to retrieve config file

def main():
    print(f"[Katabatic test 0.1]")

    with open(CONFIG_FILE, "r") as file: #Open config file as read only
        config = json.load(file) #config is a dict of configuration variables
    try:
        module_name = config["tdgm_module_name"]
        class_name = config["tdgm_class_name"]
    except KeyError as key_error:
        raise SystemExit(   #SystemExit exception prints the below and immediately exits the interpreter
            f"Configuration file '{CONFIG_FILE}' does not contain: {key_error}")
    
    diagnostic = None #initialise an empty diagnostic variable
    try:
        # breakpoint()
        module = load_module(module_name)  # load_module method from Aiko services
        model_class = getattr(module, class_name)
    except FileNotFoundError:
        diagnostic = "could not be found."
    # except Exception as exception:
    #     diagnostic = f"could not be loaded: {exception}"
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
    main()