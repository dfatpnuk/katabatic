from katabatic_spi import KatabaticModelSPI
import pandas as pd #Install pandas into venv
from ganblr import GANBLR

class GanblrAdapter(KatabaticModelSPI):
    
    def load_model(self):
        self.model = GANBLR() # Initialise and return an instance of the ganblr model. 
        self.training_sample_size = 0
        return self.model

    #TODO: add exception handling to load()
    def load_data(self, data_pathname):
        data = pd.DataFrame
        print("Loading Data...")
        return data
    
    #TODO: add exception handling to fit()
    def fit(self, X_train, y_train, k=0, epochs=10, batch_size=64):   #TODO: remove hard coded numbers
        
        self.model.fit(X_train, y_train, k, batch_size=batch_size, epochs=epochs) # TODO: train self.model on the input data
        self.training_sample_size = X_train.len()
        return   # Don't need to return anything. 

    #TODO: add exception handling to generate()
    def generate(self, size=None):  #Modify so that if size is not specified, default is the training sample size.
        
        if size==None: 
            size = self.training_sample_size

        generated_data = self.model.sample(size)
        return generated_data