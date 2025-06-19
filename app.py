import streamlit as st
import PIL
from PIL import Image
import numpy as np

st.title ("MicroDetect AI")
st.Write ("Upload gambar mikroskop kamu dan kami bantu deteksi penyakitnya (dummy AI)")

uploaded_file = st.file_uploader ("Upload gambar citra mikroskop", type=["jpg", "png", "jpeg"])

if uploaded_file is not none:
    image = image.open(uploaded_file)
    st.image(image, caption="Citra Mikroskop yang Diunggah", width = 300)

    # Simulasi prediksi AI dimmy
    st.Write("🔍 Menganalisis...")
    st.success("✅ Hasil Deteksi : *Malaria Terdeteksi*")
  else:
    st.info("silahkan upload gambar untuk mulai.")