import streamlit as st
from PIL import Image

st.title("🧫 MicroDetect AI")
st.write("Upload gambar mikroskop kamu, dan kami bantu deteksi penyakitnya (dummy AI).")

uploaded_file = st.file_uploader("Upload gambar mikroskop:", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Citra Mikroskop yang Diupload", width=300)
    st.write("🔍 Menganalisis...")
    st.success("✅ Hasil Deteksi: Malaria Terdeteksi (Dummy)")
else:
    st.info("Silakan upload gambar dulu untuk mulai analisis.")