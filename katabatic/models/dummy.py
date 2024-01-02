# A dummy datagen model written by Jaime Blackwell

import model   # Import the abstract base class

# This dummy model simply duplicates the data and returns it. 
class DummyModel(model):
    def __init__(self, x, Y, batch_size = 64):
        
        self.batch_size = batch_size
        self.x = x   # data to train on
        self.Y = Y   # Y is the target variable
        self.k = 0

    def build(self):  # Build the model
        return 42

    def fit(self, x, y ):  
        return 42

    def generate():
        return 42
