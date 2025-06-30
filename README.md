# Predection_House
## Dataset

Dataset yang digunakan adalah `Data_Rumah.xlsx - Sheet1.csv`. Dataset ini berisi informasi properti rumah dengan kolom-kolom sebagai berikut:

- `Luas Bangunan`: Luas bangunan dalam meter persegi (m²).
- `Luas Tanah`: Luas tanah dalam meter persegi (m²).
- `Jumlah Kamar Tidur`: Jumlah kamar tidur.
- `Jumlah Kamar Mandi`: Jumlah kamar mandi.
- `Jumlah Garasi`: Jumlah garasi.
- `Rasionalitas`: Skor rasionalitas (kemungkinan skala 0.0 - 1.0, perlu diklarifikasi jika ada).
- `Harga`: Harga rumah (variabel target).

## Analisis dan Pemodelan

Proses analisis data, pra-pemrosesan, pemilihan fitur, pelatihan model, dan evaluasi dilakukan dalam `data_rumah.ipynb`. Model-model berikut dieksplorasi:

- **Regresi Linier**
- **Random Forest**
- **XGBoost**

Transformasi logaritmik diterapkan pada variabel target (`Harga`) untuk menangani skewness dan meningkatkan kinerja model. XGBoost terbukti menjadi model dengan kinerja terbaik untuk tugas prediksi ini setelah penyetelan hyperparameter. Model terbaik disimpan sebagai `rumah_model.pkl`.

## Aplikasi Streamlit

`rumah_dashboard.py` adalah aplikasi web berbasis Streamlit yang memungkinkan pengguna untuk memprediksi harga rumah secara interaktif. Pengguna dapat memasukkan nilai untuk fitur-fitur seperti luas tanah, luas bangunan, jumlah kamar tidur, kamar mandi, garasi, dan skor rasionalitas, kemudian mendapatkan prediksi harga rumah.

## Cara Menjalankan

Ikuti langkah-langkah di bawah ini untuk menjalankan aplikasi Streamlit secara lokal.

### Prasyarat

Pastikan Anda telah menginstal Python 3.12.6 Kemudian instal dependensi yang diperlukan:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn xgboost streamlit joblib
