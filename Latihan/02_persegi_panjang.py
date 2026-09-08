# latihan/02_persegi_panjang.py
# Algoritma dan Pemrograman - Pertemuan 02

# Program menghitung luas dan keliling persegi panjang

# Input panjang dan lebar
panjang = float(input("Masukkan panjang (cm): "))
lebar = float(input("Masukkan lebar (cm): "))

# Hitung luas dan keliling
luas = panjang * lebar
keliling = 2 * (panjang + lebar)

# Tampilkan hasil dengan 2 angka desimal
print(f"Luas      : {luas:.2f} cm^2")
print(f"Keliling  : {keliling:.2f} cm")