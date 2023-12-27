# RPS Prediction using VGG19 Model
Repositori ini berisi proyek menggunakan model VGG19 yang telah dilatih sebelumnya untuk memprediksi gestur tangan Batu-Gunting-Kertas (RPS). Proyek ini juga mencakup penerapan model menggunakan Flask, yang memungkinkan pengguna berinteraksi dengan sistem prediksi melalui antarmuka web.

## Dataset

![image](https://github.com/delananda30/rpsprediction/assets/71807981/d55bb033-48a4-42ff-b29d-08ddfab5eafc)
Dataset yang digunakan dalam proyek ini adalah kumpulan citra gestur tangan yang menunjukkan tiga kategori: batu, gunting, dan kertas. Citra-citra ini merupakan representasi visual dari berbagai pose tangan yang digunakan untuk melatih model prediksi.



![image](https://github.com/delananda30/rpsprediction/assets/71807981/67d18abe-44df-4c38-be0a-d5ba1584253a)

Dataset yang digunakan untuk pelatihan model memiliki 3 kelas dengan total 2520 sampel yang dibagi menjadi subset training (75%), validation (15%), dan test (10%). Augmentasi diterpakan 



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

## Model VGG19
VGG19 (Visual Geometry Group 19) adalah salah satu arsitektur model Deep Convolutional Neural Network (CNN) yang dikembangkan oleh Karen Simonyan dan Andrew Zisserman pada tahun 2014. Model ini memiliki 19 layer (hence the name) dan sangat terkenal karena keefektifannya dalam mengatasi tugas pengenalan gambar.

Dengan menggunakan konsep transfer learning dan model VGG19, model ini mampu mencapai akurasi sebesar 98% setelah dilatih dengan data pelatihan dan divalidasi dengan data validasi. Akurasi yang tinggi ini menunjukkan kemampuan model untuk dengan baik mengenali dan mengklasifikasikan gestur tangan batu, gunting, dan kertas pada permainan Batu-Gunting-Kertas.

## Aplikasi Web
<img width="960" alt="image" src="https://github.com/delananda30/rpsprediction/assets/71807981/f128877e-bbab-4e7f-926c-dd7d7cdf6b38">
<img width="960" alt="image" src="https://github.com/delananda30/rpsprediction/assets/71807981/744c8b92-9560-4528-9d62-f35ec814fc1f">

### Getting Started
Install dependencies:
```bash
  pip install -r requirements.txt
```

Run the Flask application:
```bash
  flask run
```
Buka peramban web Anda dan buka http://localhost:5000 untuk berinteraksi dengan sistem prediksi RPS.

## Authors
- [Dela Ananda Setyarini](https://github.com/delananda30)
