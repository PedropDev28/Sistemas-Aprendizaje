#Formulario de registro de usuarios

import streamlit as st
import pandas as pd

    # Formulario de registro de usuarios
st.title('Registro de Usuarios')
st.write('Por favor, ingrese la siguiente información para registrarse')
nombre = st.text_input('Nombre')
apellido = st.text_input('Apellido')
edad = st.number_input('Edad', min_value=0, max_value=100)
email = st.text_input('Email')
telefono = st.text_input('Teléfono')
ciudad = st.text_input('Ciudad')
pais = st.text_input('País')

if st.button('Registrar'):
    st.write('Registrando usuario...')
    st.write('Nombre:', nombre)
    st.write('Apellido:', apellido)
    st.write('Edad:', edad)
    st.write('Email:', email)
    st.write('Teléfono:', telefono)
    st.write('Ciudad:', ciudad)
    st.write('País:', pais)
    st.write('Usuario registrado exitosamente')
    st.audio('audio.mp3')
