import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('datasets/vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón

st.header('Autos en Venta 2018-2019 USA')

if hist_button:
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de ventas de coches')

    # crear un histograma
    fig = px.histogram(car_data, x='odometer')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Construir gráfico de dispersión')

if disp_button:
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de ventas de coches')

    # crear un gráfico de dispersión
    fig2 = px.scatter(car_data, x='odometer', y='price')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)

# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:
    st.write('Construir un histograma para la columna edómetro')
    # crear un histograma
    fig = px.histogram(car_data, x='odometer')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)