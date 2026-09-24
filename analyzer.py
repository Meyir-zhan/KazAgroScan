import numpy 

class DataAnalyzer:
    def __init__(self, red_grid, nir_grid):
        self.red_grid = red_grid.astype(float)
        self.nir_grid = nir_grid.astype(float)

    def calculate_ndvi(self):
        denominator =  self.nir_grid + self.red_grid
        ndvi = numpy.zeros_like(denominator)
        mask = denominator != 0
        numpy.divide(self.nir_grid - self.red_grid, denominator, out = ndvi, where = mask)
        return ndvi
        