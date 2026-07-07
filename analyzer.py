import numpy 

class DataAnalayzer:
    def __init__(self, red_grid, nir_grid):
        self.red_grid = red_grid
        self.nir_grid = nir_grid

    def calculate_ndvi(self):
        denominator =  self.nir_grid + self.red_grid
        ndvi = numpy.where(denominator == 0, 0.0,(self.nir_grid - self.red_grid) / denominator)
        return ndvi
        