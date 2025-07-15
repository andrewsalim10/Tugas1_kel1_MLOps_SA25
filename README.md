---
title: MLOpsDrugText
emoji: 📚
colorFrom: red
colorTo: pink
sdk: gradio
sdk_version: 5.34.2
app_file: app.py
pinned: false
license: apache-2.0
short_description: Deployment Test from Github Actions
---

# 📌 Tugas MLOps

Praktik penerapan pipeline **Machine Learning Operations (MLOps)** dengan **GitHub Actions** sebagai **Continuous Integration** dan **Hugging Face Spaces** sebagai **Continuous Deployment**.

**Hugging Face Spaces** : [Tugas1_kel1_MLOps_SA25](https://huggingface.co/spaces/Bagus21/Tugas1_kel1_MLOps_SA25)

---

## 📊 Dataset

- **Nama**: `credit_risk_dataset.csv`  
- **Tipe**: CSV (Comma Separated Values)  
- **Deskripsi**: Dataset ini berisi tentang informasi yang berhubungan dengan risiko kredit dan ciri-ciri seorang debitur (peminjam) seperti data peminjam dan keuangannya. Dataset ini digunakan untuk membangkan sebuah model yang bisa memprediksi apakah peminjam bisa mengambil kredit atau tidak.  
- **Tautan**: [credit_risk_dataset](https://www.kaggle.com/datasets/laotse/credit-risk-dataset/data)

---

## 💡 Fitur

- Klasifikasi status pinjaman dari seorang debitur dengan model Exra Trees Classifier.
- User Interface dengan Gradio
- Aplikasi berada pada platform Hugging Face Spaces
- Managemen repository secrets pada Github
- Melakukan CI/CD dengan Github Actions dan Hugging Face Spaces

---

## 🧠 Algoritma Model

- **Model**: Extra Trees Classifier  
- **Alasan Pemilihan**:
  - Cepat dalam pelatihan dan prediksi.
  - Efektif dalam melakukan prediksi.

---

## ⚙️ Tech Stack

| Tools              | Deskripsi                                      |
|-------------------|-----------------------------------------------|
| **Python**         | Bahasa pemrograman utama                      |
| **Scikit-learn**   | Library untuk model ExtraTreesClassifier                |
| **Gradio**         | UI interaktif berbasis Python                 |
| **Hugging Face Spaces** | Platform hosting dan deployment          |
| **GitHub**         | Control version kode dan pengaturan CI/CD          |
| **Google Colab**   | Tempat eksplorasi dan pelatihan model awal    |
| **Docker**   | Tempat eksplorasi dan pembungkusan aplikasi    |

---

## 🧠 Model Overview

- **Tipe Model**: Decision trees
- **Tugas**: Prediksi Penerimaan Pinjaman
- **Data**: 
    - person_age : Usia Pengaju
    - person_income : Penghasilan tahunan pengaju
    - person_home_ownership : Jenis kepemilikan rumah pengaju
    - person_emp_length : Lama durasi kerja pengaju (tahun)
    - loan_intent : Tujuan pinjaman
    - loan_amnt : Jumlah pinjaman yang diajukan
    - loan_int_rate : Suku bunga untuk pinjaman (tahun)
    - loan_percent_income : Persentase penghasilan yang disisihkan untuk melunasi pinjaman
    - cb_person_default_on_file : Riwayat gagal bayar pengaju
    - cb_person_cred_hist_length : Lama durasi pelunasan pengaju
- **Target**: 
    - loan_status : Menerima atau menolak pinjaman

---

## 👥 Tim & Kontribusi

| Nama Lengkap                             | NIM              |
|------------------------------------------|------------------|
| Andrew Salim                             | 205150207111048  |
| Bagus Jati Pramono                       | 215150200111012  |
| Daffa Daniswara Kodrihan                 | 195150200111052  |
| Sonia Anindhiya                          | 225150200111045  |

---

## 🏫 Institusi

- **Program Studi**: Teknik Informatika  
- **Departemen**: Teknik Informatika  
- **Fakultas**: Ilmu Komputer  
- **Universitas**: Universitas Brawijaya – Malang  
- **Tahun**: 2025

---