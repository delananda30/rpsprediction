# RPS Prediction using VGG19 Model
Repositori ini berisi proyek menggunakan model VGG19 yang telah dilatih sebelumnya untuk memprediksi gestur tangan Batu-Gunting-Kertas (RPS). Proyek ini juga mencakup penerapan model menggunakan Flask, yang memungkinkan pengguna berinteraksi dengan sistem prediksi melalui antarmuka web.

## Dataset

![image](https://github.com/delananda30/rpsprediction/assets/71807981/d55bb033-48a4-42ff-b29d-08ddfab5eafc)
Dalam proyek ini, digunakan dataset berupa kumpulan citra gestur tangan yang mencakup tiga kategori utama: batu, gunting, dan kertas. Citra-citra ini merepresentasikan visual dari berbagai pose tangan, yang menjadi dasar pelatihan untuk model prediksi.

Dataset pelatihan terdiri dari 2520 sampel, yang dibagi menjadi subset training (75%), validation (15%), dan test (10%). Rincian jumlah data untuk masing-masing subset adalah sebagai berikut:
- Training Set: 1890 data
- Validation Set: 378 data
- Test Set: 252 data

![image](https://github.com/delananda30/rpsprediction/assets/71807981/67d18abe-44df-4c38-be0a-d5ba1584253a)

Untuk memperkaya dataset, dilakukan augmentasi dengan mengaplikasikan variasi gambar. Tujuan dari augmentasi adalah membantu model untuk lebih baik dalam mengenali pola yang berbeda dalam kelas-kelas tersebut. Proses augmentasi diimplementasikan untuk memastikan bahwa model tidak hanya belajar dari contoh yang sama tetapi juga mampu mengatasi variasi yang mungkin terjadi dalam situasi dunia nyata.

## Model
VGG19 (Visual Geometry Group 19) adalah salah satu arsitektur model Deep Convolutional Neural Network (CNN) yang dikembangkan oleh Karen Simonyan dan Andrew Zisserman pada tahun 2014. Model ini memiliki 19 layer (hence the name) dan sangat terkenal karena keefektifannya dalam mengatasi tugas pengenalan gambar.

Base model menggunakan arsitektur VGG19 yang telah dilatih sebelumnya dengan bobot dari dataset ImageNet. Lapisan fully connected pada bagian atas dihapus dan diganti dengan lapisan baru untuk tujuan proyek, yaitu prediksi gestur tangan RPS.

Berikut adalah struktur model beserta visualisasi plot model:
```plaintext
Model: "sequential"
_________________________________________________________________
Layer (type)                Output Shape              Param #   
=================================================================
vgg19 (Functional)          (None, 7, 7, 512)         20024384  
                                                                 
global_average_pooling2d (  (None, 512)               0         
GlobalAveragePooling2D)                                         
                                                                 
dense (Dense)               (None, 128)               65664     
                                                                 
dense_1 (Dense)             (None, 3)                 387       
                                                                 
=================================================================
Total params: 20,090,435 (76.64 MB)
Trainable params: 66,051 (258.01 KB)
Non-trainable params: 20,024,384 (76.39 MB)
_________________________________________________________________
```
Struktur model ini terdiri dari tiga lapisan utama, yaitu VGG19 sebagai base model, lapisan Global Average Pooling untuk meratakan output, dan dua lapisan Dense (fully connected) untuk klasifikasi tiga kategori gestur tangan: batu, gunting, dan kertas.

![image](https://github.com/delananda30/rpsprediction/assets/71807981/aa17a316-774b-4d4f-9792-0a567b90c5d3)

Visualisasi plot model memberikan gambaran intuitif mengenai arsitektur dan hubungan antar lapisan dalam model tersebut.

Model dilatih dengan optimizer Adam dan fungsi loss categorical_crossentropy. Proses pelatihan dilakukan selama 10 epoch. Berikut adalah beberapa hasil pelatihan:

```plaintext
Epoch 1/10
60/60 [==============================] - 63s 885ms/step - loss: 0.9585 - accuracy: 0.6021 - val_loss: 0.7845 - val_accuracy: 0.7963
...
Epoch 10/10
60/60 [==============================] - 46s 768ms/step - loss: 0.1384 - accuracy: 0.9614 - val_loss: 0.1320 - val_accuracy: 0.9683
```

Hasil evaluasi pada subset test menunjukkan tingkat akurasi yang tinggi:
```plaintext
Test Loss: 0.08905871212482452
Test Accuracy: 0.9920634627342224
```
Model dievaluasi lebih lanjut dengan melakukan prediksi pada subset test dan menghasilkan classification report:

```plaintext
Classification Report:
              precision    recall  f1-score   support

       paper       0.99      0.99      0.99        84
        rock       1.00      0.99      0.99        84
    scissors       0.99      1.00      0.99        84

    accuracy                           0.99       252
   macro avg       0.99      0.99      0.99       252
weighted avg       0.99      0.99      0.99       252
```
Classification report pada subset test menegaskan kinerja yang sangat baik, dengan presisi, recall, dan f1-score di atas 99% untuk setiap kelas (paper, rock, scissors).

Secara keseluruhan, model ini menggunakan konsep transfer learning dan arsitektur VGG19 untuk mencapai akurasi di atas 99% setelah pelatihan dan validasi. Keberhasilan ini menunjukkan kemampuan model dalam mengklasifikasikan gestur tangan pada permainan Batu-Gunting-Kertas.

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
