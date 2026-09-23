import pystac_client
import planetary_computer
import rasterio
from rasterio.windows import from_bounds

class DataFetcher:
    def __init__(self,coordinates):
        self.coordinates = coordinates
    
    def fetch_satalite_data(self, date):
        catalog = pystac_client.Client.open("https://planetarycomputer.microsoft.com/api/stac/v1")
        search = catalog.search(collections=["sentinel-2-l2a"], datetime=date, intersects=self.coordinates)

        items = search.item_collection()
        
        print(f"DEBUG: Found {len(items)} items.")
        if len(items) == 0:
       
            raise ValueError("No satellite data found for this location and date.")

        item = items[0]
        signed_red = planetary_computer.sign(item.assets["B04"].href)
        signed_nir = planetary_computer.sign(item.assets["B08"].href)

        cords = self.coordinates["coordinates"][0]
        min_x = min(pt[0] for pt in cords)
        min_y = min(pt[1] for pt in cords)
        max_x = max(pt[0] for pt in cords)
        max_y = max(pt[1] for pt in cords)

        with rasterio.open(signed_red) as red_ds:
            window_red = from_bounds(min_x,min_y,max_x,max_y, transform=red_ds.transform)
            red = red_ds.read(1, window = window_red)

        with rasterio.open(signed_nir) as nir_ds:
            window_nir = from_bounds(min_x,min_y,max_x,max_y, transform=nir_ds.transform)
            nir = nir_ds.read(1, window = window_nir)

        return red, nir