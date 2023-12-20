import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import cv2
import numpy as np
from pyngrok import ngrok
from keras.preprocessing.image import img_to_array

# Fungsi untuk memuat model
@st.cache(allow_output_mutation=True)
def load_model():
    model = tf.keras.models.load_model('model.h5')
    return model

# Memuat model saat aplikasi dimulai
with st.spinner('Model is being loaded..'):
    model = load_model()

# Judul aplikasi
st.write("""
         # Paper Rock Scissors Classification
         """
         )

# Pemuatan gambar
file = st.file_uploader("Please upload an image file", type=["jpg", "png"])

# Fungsi untuk melakukan prediksi
def import_and_predict(image_data, model):
        size = (150, 100)    
        image = ImageOps.fit(image_data, size, Image.Resampling.LANCZOS)
        image = np.asarray(image)
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        img_reshape = img[np.newaxis,...]
        prediction = model.predict(img_reshape)[0]  # Perubahan di sini
        return prediction

# Menampilkan tampilan jika tidak ada file yang diunggah
if file is None:
    st.text("Please upload an image file")
else:
    # Menampilkan gambar yang diunggah
    image = Image.open(file)
    st.image(image, use_column_width=True)

    # Melakukan prediksi
    class_names = ['paper', 'rock', 'scissors']  # Ganti dengan kelas yang sesuai
    predictions = import_and_predict(image, model)
    predict_class = np.argmax(predictions)
    predicted_label = class_names[predict_class]

    # Menampilkan hasil prediksi
    st.write("Prediction:", predicted_label)
    st.write("Prediction:", predictions)

# Mengonfigurasi pyngrok untuk membuat tunnel
public_url = ngrok.connect(port='8501')

# Menampilkan URL ngrok
st.write('**Ngrok Tunnel URL:**', public_url)
