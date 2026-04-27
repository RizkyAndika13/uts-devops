# Implementasi DevOps pada Aplikasi Analisis Data Nilai Mahasiswa Menggunakan Docker, PostgreSQL, dan CI/CD

## Deskripsi Proyek
Proyek ini adalah aplikasi sederhana untuk melakukan analisis data nilai mahasiswa menggunakan Python. Data nilai diambil dari environment variable, kemudian diolah menggunakan library Pandas untuk menghitung rata-rata nilai. Hasil analisis tersebut disimpan ke dalam database PostgreSQL dan juga diekspor ke file CSV.

Aplikasi ini sudah dikembangkan menggunakan konsep DevOps dengan memanfaatkan Docker untuk containerization, Docker Compose untuk mengelola layanan, serta GitHub Actions untuk otomatisasi pengecekan kode (CI/CD).

---

## Arsitektur Sistem
Aplikasi ini menggunakan base image python:3.9-slim karena ukurannya lebih ringan dibanding image Python biasa, sehingga lebih efisien saat dijalankan di dalam container. Image ini sudah cukup untuk menjalankan aplikasi Python tanpa membawa banyak komponen yang tidak diperlukan.

Sistem terdiri dari dua container, yaitu app dan db. Container app menjalankan aplikasi Python, sedangkan container db menggunakan PostgreSQL sebagai database. Aplikasi akan mengambil konfigurasi database dari environment variable, lalu terhubung ke database melalui network internal Docker dengan menggunakan nama service db. Setelah terhubung, aplikasi akan menyimpan data hasil analisis ke dalam database.

Alur kerja:
Aplikasi mengambil data dari environment variable → memproses data → menyimpan ke database → menghasilkan file CSV.

---

## Cara Menjalankan (How to Run)

1. Clone repository:
   git clone <link-repo>
cd uts-devops

2. Jalankan aplikasi dengan Docker Compose:
   docker-compose up --build
   
3. Tunggu hingga proses selesai, lalu akan muncul output:
- Aplikasi berhasil terhubung ke database
- Data berhasil diproses
- Rata-rata nilai ditampilkan di terminal
