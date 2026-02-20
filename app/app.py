import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import matplotlib.pyplot as plt
import streamlit as st
from src.data import load_cmapss_train, filter_motor_data
from src.features import get_sensor_list

# Configuración de página
st.set_page_config(page_title="C-MAPSS Explorador", layout="wide")  # Configuración del título y ancho de la página
st.title("Explorador de datos C-MAPSS")  # Título principal de la app

# Cargar datos
train = load_cmapss_train(
    "/Users/jesusescano/Desktop/Codigos/Proyectos/predictive-maintenance-cmapss/data/CMAPSSData/train_FD001.txt"
)  # Carga los datos de entrenamiento desde la ruta indicada

# Selección de motor y sensor
motor_id = st.selectbox("Selecciona motor", sorted(train['unit'].unique()))  # Desplegable para seleccionar el motor
sensor_id = st.selectbox("Selecciona sensor", get_sensor_list())  # Desplegable para seleccionar el sensor

# Filtrar datos
motor_data = filter_motor_data(train, motor_id)  # Filtra los datos solo del motor seleccionado

# Graficar
fig, ax = plt.subplots(figsize=(10, 4))  # Crear la figura del gráfico con tamaño 10x4 pulgadas
ax.plot(motor_data['time'], motor_data[sensor_id])  # Dibujar gráfico: eje X = ciclos, eje Y = valores del sensor
ax.set_xlabel("Ciclos")  # Etiqueta del eje X
ax.set_ylabel("Valor")  # Etiqueta del eje Y
ax.set_title(f"Evolución de {sensor_id} (motor {motor_id})")  # Título de la gráfica indicando sensor y motor

st.pyplot(fig)  # Mostrar el gráfico en Streamlit