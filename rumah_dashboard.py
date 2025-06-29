import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("D:/Data Projek/Projek(Data_Rumah)/Ris/rumah_model.pkl")


# Judul dashboard
st.title("Prediksi Harga Rumah (Model: XGBoost + Log)")

st.markdown("Masukkan data rumah yang ingin diprediksi:")

# Input dari pengguna
lt = st.number_input("Luas Tanah (m²)", min_value=10, max_value=1000, value=100)
lb = st.number_input("Luas Bangunan (m²)", min_value=10, max_value=1000, value=80)
kt = st.number_input("Jumlah Kamar Tidur", min_value=1, max_value=10, value=3)
km = st.number_input("Jumlah Kamar Mandi", min_value=1, max_value=10, value=2)
grs = st.number_input("Jumlah Garasi", min_value=0, max_value=5, value=1)
rasional = st.slider("Skor Rasionalitas (0.0 – 1.0)", 0.0, 1.0, 0.5)

# Prediksi
if st.button("Prediksi Harga Rumah"):
    fitur = np.array([[lb, lt, kt, km, grs, rasional]])
    pred_log = model.predict(fitur)[0]
    pred_juta = np.expm1(pred_log)  # balik dari log

    st.success(f"✅ Prediksi Harga Rumah: Rp {pred_juta:,.0f} juta")
