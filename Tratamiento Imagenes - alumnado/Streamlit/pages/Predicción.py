import streamlit as st
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from streamlit_drawable_canvas import st_canvas
import pickle





# Cargar el modelo desde el archivo
with open("svm_digits_model.pkl", "rb") as f:
    modelo = pickle.load(f)

scaler = modelo["scaler"]
clf = modelo["clf"]

# Create a canvas to draw the digit
canvas = st_canvas(
    fill_color="rgb(0, 0, 0)",  # Fixed fill color with some opacity
    stroke_width=10,
    stroke_color="rgb(255, 255, 255)",
    background_color="rgb(0, 0, 0)",
    update_streamlit=True,
    height=150,
    width=150,
    drawing_mode="freedraw",
    key="canvas",
)


def preprocess_image(image):
    # Convertir a escala de grises
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  
    #Redimensionar, ya que SVM fue entrenado con imagenes 8x8
    image = cv2.resize(image, (8, 8))
    
    #Necesitamos convertirla en una matriz de números, y que 
    # sean hexadecimales, no de 0 a 255, porque digits usa eso, por eso escalamos
    image = image / 255.0 * 16.0
    image = image.astype(int)
   

    # Aplanar la imagen para que sea un vector de 64 elementos
    image_array = image.flatten()
  

    # Aplicar el mismo scaler que usaste al entrenar
    image_array = scaler.transform(image_array.reshape(1, -1))
   

    
    return image_array




def preprocesar_canvas_para_svm(image_data, scaler):
    if image_data is None:
        return None

    imagen_scaled = preprocess_image(image_data)
    return imagen_scaled



#Predice mediante la imagen 
def predict(image):
    if image is None:
        return None
    
    prediccion = clf.predict(image)

    return prediccion[0]



# Predice con la imagen
if st.button("Predict"):
    if canvas.image_data is not None:
        img_processed = preprocesar_canvas_para_svm(canvas.image_data, scaler)
        prediction = clf.predict(img_processed)
        st.subheader("Predicción")
        st.write(f"El modelo predice que el número es: **{prediction}**")





archivo_subido = st.file_uploader("Sube una imagen manuscrita (JPG o PNG)", type=["jpg", "png"])

if archivo_subido is not None:
    # Mostrar imagen con PIL
    image = Image.open(archivo_subido)
    st.image(image, caption='Imagen subida',  width=150)  
    st.write("")

    # Make a prediction
    prediction = predict(preprocess_image(np.array(image)))
    #prediccion = predecir_digito(archivo_subido)
    st.subheader(f"✅ El modelo predice que el número es: **{prediction}**")

st.write("Esta app usa OpenCV para procesar imágenes y Scikit-learn para predecir dígitos manuscritos.")


