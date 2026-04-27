# Implementasi DevOps pada Aplikasi Analisis Data Nilai Mahasiswa Menggunakan Docker, PostgreSQL, dan CI/CD

## Deskripsi Proyek
Proyek ini merupakan aplikasi sederhana untuk melakukan analisis data nilai mahasiswa. Data diambil dari environment variable, diproses menggunakan Python, kemudian disimpan ke dalam database PostgreSQL dan file CSV.

---

## Arsitektur Sistem
Aplikasi ini menggunakan Docker untuk memastikan portabilitas dan konsistensi lingkungan. Base image yang digunakan adalah `python:3.9-slim` karena ringan dan efisien.

Sistem terdiri dari dua layanan:
- **app**: menjalankan aplikasi Python
- **db**: database PostgreSQL

Alur kerja:
Aplikasi mengambil data dari environment variable → memproses data → menyimpan ke database → menghasilkan file CSV.

---

## Cara Menjalankan

1. Clone repository:
