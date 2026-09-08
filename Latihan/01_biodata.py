# Konstanta tahun sekarang
TAHUN_SEKARANG = 2026

# Input data dari pengguna
nama = input("Masukkan Nama: ")
nim = input("Masukkan NIM: ")
kelas = input("Masukkan Kelas: ")
tahun_lahir = int(input("Masukkan Tahun Lahir: "))

# Hitung umur
umur = TAHUN_SEKARANG - tahun_lahir

# Tampilkan kartu biodata dengan f-string
print("\n=== KARTU BIODATA ===")
print(f"Nama        : {nama}")
print(f"NIM         : {nim}")
print(f"Kelas       : {kelas}")
print(f"Tahun Lahir : {tahun_lahir}")
print(f"Umur        : {umur} tahun")