# Rock-Paper-Scissors (RPS) Prediction using VGG19 Model

Repositori ini berisi proyek yang memanfaatkan model VGG19 yang telah dilatih sebelumnya untuk memprediksi hasil gestur tangan Batu-Gunting-Kertas (RPS). Proyek ini juga mencakup penerapan model menggunakan Flask, yang memungkinkan pengguna berinteraksi dengan sistem prediksi melalui antarmuka web.

## Dataset
Dataset yang digunakan dalam proyek ini adalah kumpulan citra gestur tangan yang menunjukkan tiga kategori: batu, gunting, dan kertas. Citra-citra ini merupakan representasi visual dari berbagai pose tangan yang digunakan untuk melatih model prediksi.

### Struktur Dataset
Dataset ini telah dibagi menjadi tiga bagian: train, validation, dan test, dengan masing-masing kategori (batu, gunting, kertas). Pembagian dataset mengikuti rasio 75% untuk pelatihan, 15% untuk validasi, dan 10% untuk pengujian. Total gambar dalam dataset ini adalah 2520.

1. **Direktori Train:**
   - `batu/`: Citra tangan dengan gestur batu untuk pelatihan.
   - `gunting/`: Citra tangan dengan gestur gunting untuk pelatihan.
   - `kertas/`: Citra tangan dengan gestur kertas untuk pelatihan.

2. **Direktori Validation:**
   - `batu/`: Citra tangan dengan gestur batu untuk validasi.
   - `gunting/`: Citra tangan dengan gestur gunting untuk validasi.
   - `kertas/`: Citra tangan dengan gestur kertas untuk validasi.

3. **Direktori Test:**
   - `batu/`: Citra tangan dengan gestur batu untuk pengujian.
   - `gunting/`: Citra tangan dengan gestur gunting untuk pengujian.
   - `kertas/`: Citra tangan dengan gestur kertas untuk pengujian.

### Rasio Pembagian

- **Train:**
  - Batu: 567 citra (75% dari 756 citra)
  - Gunting: 567 citra (75% dari 756 citra)
  - Kertas: 567 citra (75% dari 756 citra)

- **Validation:**
  - Batu: 113 citra (15% dari 756 citra)
  - Gunting: 113 citra (15% dari 756 citra)
  - Kertas: 113 citra (15% dari 756 citra)

- **Test:**
  - Batu: 84 citra (10% dari 840 citra)
  - Gunting: 84 citra (10% dari 840 citra)
  - Kertas: 84 citra (10% dari 840 citra)
