# The Katabatic Service Provider Interface (SPI) provides an abstract base class (ABC) for all model adapters to implement.

from abc import ABC

class KatabaticSPI(ABC):

    def init():   #Initialise the model
        pass

    def load(): #Load the model
        pass

    def fit():  #Fit model to data
        pass

    def generate(): #Generate synthetic data
        pass


        
    