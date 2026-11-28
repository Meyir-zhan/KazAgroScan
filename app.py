import streamlit as st
import plotly.express as px
import fetcher
import analyzer
import folium 
import datetime
from folium.plugins import Draw
from streamlit_folium import st_folium 

m = folium.Map(location=[48.0, 68.0], zoom_start=4)
Draw(export=False).add_to(m)
map_data = st_folium(m, width=700, height=450)


start_date = st.sidebar.date_input(
    'Select the starting date',
    value = datetime.date.today() - datetime.timedelta(days=7),
    min_value = datetime.date(2020, 1, 1),
    max_value = datetime.date.today(),
)
end_date = st.sidebar.date_input(
    'Select the end date',
    value = datetime.date.today(),
    min_value = datetime.date(2020, 1, 1),
    max_value = datetime.date.today(),    
)

if start_date > end_date or start_date == end_date:
    st.warning("Select the range")
    st.stop()

@st.cache_data
def get_data_from_api(date, geometry):
    fetch = fetcher.DataFetcher(geometry)
    red, nir = fetch.fetch_satellite_data(date)
    return red, nir

if st.button('Analyze Crop'):
    if map_data and map_data["all_drawings"] and len(map_data["all_drawings"]) > 0:
        geometry = map_data["all_drawings"][-1]["geometry"]
        date_str = f"{start_date.isoformat()}/{end_date.isoformat()}"
        red, nir = get_data_from_api(date_str, geometry)

        if red is None and nir is None:
            st.warning("No satellite data found for this location and date.  "
                        " Try another date or draw a larger area on the map.")
            st.stop()
        
        analyzer_instance = analyzer.DataAnalyzer(red, nir)
        ndvi = analyzer_instance.calculate_ndvi()
        st.write("NVDI Calculation is complete")
        st.write(f"NDVI Shape: {ndvi.shape}")
        if ndvi.shape[0] > 0 and ndvi.shape[1] > 0 :
            fig = px.imshow(ndvi, color_continuous_scale='RdYlGn') 
            st.plotly_chart(fig)
        else:
            st.write("There is no data")
    
    else:
        st.warning("Draw a shape on the map first.")
    
    
