import streamlit as st
import cv2
import numpy as np
import pytesseract
from PIL import Image

# Si estás en Windows, especifica la ruta de Tesseract (ajusta según tu instalación)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

st.header('📷 Subir una imagen para leer el texto')
st.write('Por favor, sube una imagen (JPG, PNG, JPEG) para extraer el texto.')

# Cargar imagen
uploaded_file = st.file_uploader('Subir archivo', type=['jpg', 'png', 'jpeg'])

if uploaded_file is not None:
    st.image(uploaded_file, caption='🖼️ Imagen subida', use_column_width=True)
    st.write('🔍 Procesando imagen...')

    # Convertir a formato OpenCV
    img = Image.open(uploaded_file)
    img_cv = np.array(img)

    # Convertir a escala de grises (mejora la precisión del OCR)
    gray = cv2.cvtColor(img_cv, cv2.COLOR_RGB2GRAY)

    # Aplicar un poco de preprocesamiento para mejorar el reconocimiento
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

    # Extraer el texto con pytesseract
    text = pytesseract.image_to_string(binary, lang='eng+spa')

    # Mostrar el texto detectado
    st.write('📄 Texto detectado en la imagen:')
    st.text_area("Resultado OCR", text, height=300)
