import streamlit as st
import plotly.express as px
import fetcher
import analyzer

date = st.sidebar.date_input('Select the date')
coordinates = st.sidebar.text_input('Enter coordinates') 

@st.cache_data
def get_data_from_api(date, coordinates):

    fetch = fetcher.DataFetcher(coordinates)
    red, nir = fetch.fetch_satalite_data(date)
    return red, nir

if st.button('Analyze Crop'):
    red, nir = get_data_from_api(date,coordinates)

    analyzer_instance = analyzer.DataAnalayzer(red, nir)
    ndvi = analyzer_instance.calculate_ndvi()
    st.write("NVDI Calculation is complete")
    fig = px.imshow(ndvi, color_continuous_scale='RdYlGn') 
    st.plotly_chart(fig)
