import streamlit as st
import plotly.express as px
import fetcher
import analyzer

date = st.sidebar.date_input('Select the date')
coordinates = st.sidebar.text_input('Enter coords as: lat, lon, lat, lon') 

@st.cache_data
def get_data_from_api(date, geometry):
    fetch = fetcher.DataFetcher(geometry)
    red, nir = fetch.fetch_satalite_data(date)
    return red, nir

if st.button('Analyze Crop'):
    if coordinates:
        coords = [float(x.strip()) for x in coordinates.split(',')]
        
       
        points = [[coords[i], coords[i+1]] for i in range(0, len(coords), 2)]
        
        
        geometry = {
            "type": "Polygon",
            "coordinates": [points]
        }

        date_str = date.isoformat()
        
        
        red, nir = get_data_from_api(date_str, geometry)

    analyzer_instance = analyzer.DataAnalayzer(red, nir)
    ndvi = analyzer_instance.calculate_ndvi()
    st.write("NVDI Calculation is complete")
    fig = px.imshow(ndvi, color_continuous_scale='RdYlGn') 
    st.plotly_chart(fig)
