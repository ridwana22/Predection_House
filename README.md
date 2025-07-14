## Predection_House

# Aplikasi Prediksi Harga Rumah dengan Streamlit
Proyek ini adalah aplikasi web interaktif untuk memprediksi harga rumah di area Tebet, Jakarta Selatan. Aplikasi ini dibangun menggunakan model machine learning XGBoost yang telah dilatih dan dioptimalkan untuk memberikan estimasi harga berdasarkan fitur-fitur properti yang dimasukkan oleh pengguna.

Proyek ini mencakup dua komponen utama:
  Notebook Analisis (data_rumah.ipynb): Berisi seluruh proses, mulai dari eksplorasi data, rekayasa fitur, hingga pelatihan dan evaluasi model.
  Dashboard Aplikasi (rumah_dashboard.py): Aplikasi web berbasis Streamlit yang menggunakan model yang telah dilatih untuk melakukan prediksi secara real-time.

🚀 Tampilan Aplikasi
Tampilan interaktif memungkinkan pengguna untuk memasukkan berbagai parameter properti dan secara instan mendapatkan prediksi harga.
  Fitur Input Pengguna:
  Luas Tanah (m²)
  Luas Bangunan (m²)
  Jumlah Kamar Tidur
  Jumlah Kamar Mandi
  Kapasitas Garasi
  Skor Rasionalitas: Sebuah slider yang merepresentasikan faktor harga per area yang kompleks, disederhanakan menjadi skor antara 0.0 hingga 1.0.
  Aplikasi ini memuat model rumah_model.pkl yang dihasilkan dari notebook untuk memberikan prediksi yang akurat.

📊 Alur Kerja Pembangunan Model
Proses di balik aplikasi ini didokumentasikan sepenuhnya dalam notebook data_rumah.ipynb.
  Eksplorasi Data (EDA)
  Menganalisis dataset dari data_rumah.xlsx yang berisi 1010 data properti.
  Melakukan visualisasi untuk memahami distribusi harga serta korelasinya dengan Luas Bangunan (LB) dan Luas Tanah (LT).
  Rekayasa Fitur (Feature Engineering)
  Transformasi Log: Variabel target HARGA ditransformasi ke skala logaritmik (LOG_HARGA) untuk menormalkan distribusinya dan meningkatkan akurasi model.
  Fitur Kustom Rational: Sebuah fitur bernama Rational dibuat untuk menangkap rasio harga terhadap luas. Dalam aplikasi dashboard, fitur ini diubah menjadi "Skor 
  Rasionalitas" yang dapat diatur oleh pengguna.

Pelatihan dan Evaluasi Model
  Tiga model regresi dibandingkan: Linear Regression, Random Forest, dan XGBoost.
  Dilakukan hyperparameter tuning menggunakan GridSearchCV untuk Random Forest dan XGBoost untuk mendapatkan performa optimal.
  XGBoost (Tuned) terbukti menjadi model terbaik dengan R2 Score sebesar 0.9828.

Ekspor ke Spreadsheet
🚀 Cara Menjalankan
Proyek ini terdiri dari dua bagian yang dapat dijalankan secara terpisah.
1. Menjalankan Notebook untuk Melatih Ulang Model
Bagian ini bersifat opsional jika Anda hanya ingin menjalankan aplikasi.
  Pastikan semua library yang tercantum di data_rumah.ipynb terpasang.
  Letakkan file data_rumah.xlsx di direktori yang sama.
  Jalankan semua sel di dalam notebook untuk menghasilkan file model rumah_model.pkl.

2. Menjalankan Dashboard Aplikasi Streamlit
Pastikan Anda memiliki streamlit, numpy, dan joblib terpasang.
  Ganti path ini di dalam rumah_dashboard.py
  model = joblib.load("path/ke/file/anda/rumah_model.pkl") 
  Jalankan aplikasi dari terminal:
    ( streamlit run rumah_dashboard.py )
  Buka browser dan akses alamat lokal yang ditampilkan untuk menggunakan aplikasi.
