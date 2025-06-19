import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# Load model .h5
model = tf.keras.models.load_model("microdetect_model.h5")

st.title("MicroDetect AI")
st.write("Upload gambar mikroskop darah untuk deteksi malaria")

# Upload gambar
uploaded_file = st.file_uploader("Pilih gambar", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).resize((64, 64))
    st.image(img, caption="Gambar yang diupload", width=300)

    # Preprocessing
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)  # jadi (1, 64, 64, 3)

    # Prediksi
    pred = model.predict(img_array)[0][0]

    if pred > 0.5:
        st.success(f"🧬 Hasil Deteksi: *Tidak Terinfeksi* (Confidence: {pred:.2f})")
    else:
        st.error(f"🧪 Hasil Deteksi: *Malaria Terdeteksi!* (Confidence: {1-pred:.2f})")
