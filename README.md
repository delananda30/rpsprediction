# Rock-Paper-Scissors (RPS) Prediction using VGG19 Model

Repositori ini berisi proyek yang memanfaatkan model VGG19 yang telah dilatih sebelumnya untuk memprediksi hasil gestur tangan Batu-Gunting-Kertas (RPS). Proyek ini juga mencakup penerapan model menggunakan Flask, yang memungkinkan pengguna berinteraksi dengan sistem prediksi melalui antarmuka web.

## Project Overview
Proyek ini terbagi menjadi dua bagian utama:
1. **Pelatihan Model:** Model deep learning (VGG19) dilatih menggunakan dataset yang berisi gambar tangan menunjukkan gestur batu, gunting, atau kertas.
2. **Deploy dengan Flask:** Model yang sudah dilatih kemudian di-deploy menggunakan Flask, menciptakan aplikasi web di mana pengguna dapat mengunggah gambar gestur tangan, dan model akan memprediksi apakah itu batu, gunting, atau kertas.

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

## Model VGG19
VGG19 (Visual Geometry Group 19) adalah salah satu arsitektur model Deep Convolutional Neural Network (CNN) yang dikembangkan oleh Karen Simonyan dan Andrew Zisserman pada tahun 2014. Model ini memiliki 19 layer (hence the name) dan sangat terkenal karena keefektifannya dalam mengatasi tugas pengenalan gambar.

Dengan menggunakan konsep transfer learning dan model VGG19, model ini mampu mencapai akurasi sebesar 98% setelah dilatih dengan data pelatihan dan divalidasi dengan data validasi. Akurasi yang tinggi ini menunjukkan kemampuan model untuk dengan baik mengenali dan mengklasifikasikan gestur tangan batu, gunting, dan kertas pada permainan Batu-Gunting-Kertas.

## Web
<img width="960" alt="image" src="https://github.com/delananda30/rpsprediction/assets/71807981/f128877e-bbab-4e7f-926c-dd7d7cdf6b38">
<img width="960" alt="image" src="https://github.com/delananda30/rpsprediction/assets/71807981/a4ebb029-dc5f-4e96-a677-7e201024ef28">

## Authors
- [Dela Ananda Setyarini](https://github.com/delananda30)
