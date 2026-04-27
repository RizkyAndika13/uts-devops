import pandas as pd
import os
import psycopg2
import time

print("Memulai proses analisis data")

# Ambil data dari environment variable
nilai_str = os.getenv('DATA_NILAI', '85,90,78,92,88')
nilai = list(map(int, nilai_str.split(',')))

# Koneksi ke database
while True:
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST", "db"),
            user=os.getenv("DB_USER", "user"),
            password=os.getenv("DB_PASSWORD", "password"),
            dbname=os.getenv("DB_NAME", "uts_db")
        )
        print("Connected to database")
        break
    except Exception:
        print("Menunggu database siap")
        time.sleep(3)

cur = conn.cursor()

# Membuat tabel jika belum ada
cur.execute("""
CREATE TABLE IF NOT EXISTS nilai_mahasiswa (
    id SERIAL PRIMARY KEY,
    nilai INT
)
""")

# Membuat DataFrame
df = pd.DataFrame({'Nilai': nilai})

# Simpan ke database
for n in df["Nilai"]:
    cur.execute("INSERT INTO nilai_mahasiswa (nilai) VALUES (%s)", (n,))

conn.commit()

# Analisis data
rata_rata = df["Nilai"].mean()
print(f"Rata-rata nilai: {rata_rata}")

# Simpan ke CSV
df.to_csv('hasil_analisis.csv', index=False)
print("Hasil disimpan ke CSV")

cur.close()
conn.close()

print("Proses selesai")
