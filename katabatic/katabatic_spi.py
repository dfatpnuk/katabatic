# The Katabatic Service Provider Interface (SPI) provides an abstract base class (ABC) for all model adapters to implement.

from abc import ABC, abstractmethod

class KatabaticSPI(ABC):

    @abstractmethod
    def load_data(): #Load the model
        pass

    @abstractmethod
    def fit(self):  #Fit model to data
        pass

    @abstractmethod
    def generate(self): #Generate synthetic data
        pass


        
    