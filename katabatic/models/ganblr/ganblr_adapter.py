from katabatic_spi import KatabaticSPI
import pandas as pd #Install pandas into venv
from ganblr.models import GANBLR

class GanblrAdapter():

    def __init__(self):
        self.model = GANBLR() # Initialise and return an instance of the ganblr model. 
        return self.model

    def load(self, data_pathname):
        data = pd.DataFrame
        print("Loading Data...")
        return data
    
    def fit(self, X_train, y_train, k=0, epochs=10, batch_size=64):   #TODO: remove hard coded numbers
        self.model.fit(X_train, y_train, k, batch_size=batch_size, epochs=epochs) # TODO: train self.model on the input data
        return self.model   # Don't really need to return anything. 

    def generate():
        pass