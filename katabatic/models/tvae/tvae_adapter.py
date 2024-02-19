from katabatic_spi import KatabaticModelSPI
import sdv
from sdv.tabular import TVAE

class TvaeAdapter(KatabaticModelSPI):

    def load_model(self):
        self.model = TVAE()
        return

    def load_data(self):
        pass

    def fit(self, data):
        self.model.fit(data)
        return

    def generate(self):
        pass