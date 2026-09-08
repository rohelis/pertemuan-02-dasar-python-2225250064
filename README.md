# Praktikum Algoritma dan Pemrograman - Pertemuan 02

**Identitas**
* **Nama:** Rohelis
* **NIM:** 2225250064
* **Kelas:** 3B

**Tujuan Repositori**
Repositori ini berfungsi sebagai tempat penyimpanan dan pengumpulan berkas tugas serta latihan praktik untuk mata kuliah Algoritma dan Pemrograman Pertemuan 02, khususnya mengenai tipe data, operasi dasar, dan *f-string* dalam Python.

**Daftar dan Fungsi Berkas**
* `tugas/kalkulator_koordinat.py`: Program utama (Tugas 1) untuk menghitung perubahan koordinat (dx, dy), jarak Euclidean, dan letak titik tengah dari dua titik koordinat.
* `latihan/01_biodata.py`: Program latihan untuk meminta input data diri dan menghitung umur berdasarkan tahun lahir.
* `latihan/02_persegi_panjang.py`: Program latihan untuk menghitung luas dan keliling persegi panjang dengan output dua angka desimal.
* `latihan/03_konversi_suhu.py`: Program latihan untuk mengonversi suhu dari satuan Celsius ke Fahrenheit dan Kelvin.
* `latihan/04_nilai_akhir.py`: Program latihan untuk menghitung nilai akhir mahasiswa berdasarkan persentase bobot Tugas, UTS, dan UAS.
* `.gitignore`: Berkas konfigurasi untuk mengabaikan file/folder tertentu agar tidak diunggah ke Git.
* `README.md`: Berkas dokumentasi utama untuk menjelaskan isi repositori ini.

**Cara Menjalankan Program dari Terminal**
Buka terminal/command prompt, pastikan direktori aktif berada di folder utama (*root*) repositori, lalu jalankan perintah berikut:
* Tugas Utama: `python tugas/kalkulator_koordinat.py`
* Latihan 1: `python latihan/01_biodata.py`
* Latihan 2: `python latihan/02_persegi_panjang.py`
* Latihan 3: `python latihan/03_konversi_suhu.py`
* Latihan 4: `python latihan/04_nilai_akhir.py`
*(Catatan: Gunakan `python3` sebagai ganti `python` jika menggunakan macOS atau Linux).*

**Tabel Hasil Tiga Test Case Tugas Utama (Kalkulator Koordinat)**

| Test Case | Koordinat Titik A | Koordinat Titik B | Output Perubahan (dx, dy) | Output Jarak | Output Titik Tengah |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Kasus 1** | x=0, y=0 | x=3, y=4 | dx = 3.00, dy = 4.00 | 5.00 | (1.50, 2.00) |
| **Kasus 2** | x=-2, y=-1 | x=4, y=7 | dx = 6.00, dy = 8.00 | 10.00 | (1.00, 3.00) |
| **Kasus 3** | x=2, y=2 | x=2, y=2 | dx = 0.00, dy = 0.00 | 0.00 | (2.00, 2.00) |

**Refleksi Singkat dan Sumber**
* **Refleksi:** Melalui tugas ini, saya belajar cara menerima masukan dari pengguna menggunakan `input()`, melakukan konversi tipe data ke `float` dan `int`, serta menerapkan rumus matematika (seperti jarak Euclidean) tanpa menggunakan pustaka eksternal. Saya juga memahami cara merapikan format tampilan teks terminal menggunakan *f-string*.
* **Sumber:** Modul RPS Praktikum Algoritma dan Pemrograman Dosen Dr. Aan Hendrayana, S.Si., M.Pd.git add .