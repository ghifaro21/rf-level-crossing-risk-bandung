# 🚂 Klasifikasi Risiko Perlintasan Sebidang Kereta Api (Kota Bandung)

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.36+-red?logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.5-orange?logo=scikit-learn)

## 📌 Deskripsi Proyek
Aplikasi web interaktif ini merupakan luaran dari **Proyek Terintegrasi 1 - S1 Sains Data ULBI (2026)**. Sistem ini mengimplementasikan model *Machine Learning* **Random Forest** untuk mengklasifikasikan tingkat risiko (Rendah, Sedang, Tinggi) pada titik perlintasan sebidang kereta api di Kota Bandung. 

Pelabelan data dasar (*ground truth*) disusun menggunakan pendekatan *Rule-Based Scoring* yang mengacu pada **Peraturan Menteri Perhubungan PM 94 Tahun 2018**, **SK.770/KA.401/DRJD/2005**, dan prinsip eksposur **ALCAM**.

## 🌟 Fitur Utama
- **Prediksi Real-Time:** Inferensi risiko instan berdasarkan 16 fitur teknis dan lingkungan.
- **Mode Auto-Fill:** Estimasi otomatis volume kendaraan, jarak pandang, dan sudut perpotongan berdasarkan kelas jalan dan jenis perlintasan.
- **Visualisasi Spasial:** Integrasi peta *OpenStreetMap* (OSM) untuk anotasi lokasi perlintasan.
- **Rekomendasi Mitigasi:** Saran tindakan keselamatan dinamis sesuai hasil klasifikasi risiko.
- **Transparansi Model:** Halaman metodologi yang memaparkan *pipeline*, *hyperparameter*, dan bobot fitur.

## 🛠️ Tech Stack
- **Framework:** Streamlit
- **Machine Learning:** Scikit-learn (Random Forest Classifier)
- **Data Processing:** Pandas, NumPy, Joblib
- **Visualization:** Plotly (Gauge & Bar Charts)

## 🚀 Cara Menjalankan Secara Lokal

1. **Clone repository:**
   ```bash
   git clone https://github.com/username-anda/rf-level-crossing-risk-bandung.git
   cd rf-level-crossing-risk-bandung

# Struktur Direktori
rf-level-crossing-risk-bandung/
│
├── .streamlit/
│   └── config.toml             # Konfigurasi tema Dark Mode kustom
├── artifacts/                  # Folder berisi model .pkl (WAJIB ADA)
│   ├── rf_model.pkl
│   ├── scaler_rf.pkl
│   ├── encoders_rf.pkl
│   └── feature_cols_rf.pkl
├── components/
│   ├── sidebar.py              # Navigasi sidebar & panel status model
│   └── charts.py               # Visualisasi Plotly (Gauge & Bar chart)
├── core/
│   ├── config.py               # Manajemen path direktori artefak
│   └── model.py                # Load model (@st.cache_resource) & predict_risk()
├── views/
│   ├── home.py                 # Halaman Beranda (Dashboard Ringkasan)
│   ├── predict.py              # Halaman Prediksi (Form Input 16 Fitur & OSM)
│   └── methodology.py          # Halaman Metodologi (Transparansi Pipeline)
├── styles/
│   └── theme.py                # Definisi warna & CSS custom
├── app.py                      # Entry point & routing antar halaman
├── requirements.txt            # Daftar dependensi Python
├── .gitignore                  # File yang diabaikan Git
└── README.md                   # Dokumentasi utama repository

# rf-level-crossing-risk-bandung
🚂 Sistem Klasifikasi Risiko Perlintasan Sebidang Kereta Api di Kota Bandung menggunakan Random Forest &amp; Streamlit. (Proyek Terintegrasi 1 - S1 Sains Data ULBI, 2026)
