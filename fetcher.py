import pystac_client
import planetary_computer
import rasterio

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


        with rasterio.open(signed_red) as red_ds:
            red = red_ds.read(1)

        with rasterio.open(signed_nir) as nir_ds:
            nir = nir_ds.read(1)

        return red, nir