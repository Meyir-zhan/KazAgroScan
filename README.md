# KazAgroScan

KazAgroScan is a Python-based dashboard that analyzes crop health using satellite imagery. It leverages cloud-native geospatial tools to fetch and process satellite data dynamically.

## Key Features
* **Cloud-Native Pipeline:** Streams satellite imagery directly from the Microsoft Planetary Computer using STAC (SpatioTemporal Asset Catalog).
* **Automated NDVI Analysis:** Calculates Normalized Difference Vegetation Index (NDVI) to assess crop health.
* **Interactive Dashboard:** Built with Streamlit for real-time visualization of field health.

## Technology Stack
* **Data Retrieval:** `pystac-client`, `planetary-computer`, `rasterio`
* **Data Processing:** `numpy`
* **Frontend:** `streamlit`, `plotly`

## Architecture
This project uses a modular design:
1. `app.py`: The user interface and application entry point.
2. `fetcher.py`: Handles catalog searching, authentication, and data streaming.
3. `analyzer.py`: Contains the logic for NDVI computation.

## Installation
1. Clone this repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
