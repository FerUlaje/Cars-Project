import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('datasets/vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón

if hist_button:
    # escribir un mensaje
    st.write('Creacióon de un histograma para el conjunto de datos de anuncios de ventas de coches')

    # crear un histograma
    fig = px.histogram(car_data, x='odometer')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    