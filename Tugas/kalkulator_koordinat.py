"""
Nama        : Rohelis
NIM         : 2225250064
Deskripsi   : Program Kalkulator Koordinat Dua Titik untuk menghitung
              perubahan (dx, dy), jarak Euclidean, dan titik tengah.
              Disimpan pada tugas/kalkulator_koordinat.py.
"""

print("KALKULATOR KOORDINAT DUA TITIK")

# 1. Menerima input koordinat x dan y untuk titik A dan B sebagai float
x1 = float(input("x titik A: "))
y1 = float(input("y titik A: "))
x2 = float(input("x titik B: "))
y2 = float(input("y titik B: "))

# 2. Menghitung perubahan koordinat dx dan dy
dx = x2 - x1
dy = y2 - y1

# 3. Menghitung jarak Euclidean tanpa menggunakan pustaka math
jarak = ((dx ** 2) + (dy ** 2)) ** 0.5

# 4. Menghitung titik tengah
tengah_x = (x1 + x2) / 2
tengah_y = (y1 + y2) / 2

# 5. Menampilkan hasil dengan format dua angka desimal (:.2f)
print() # Mencetak baris kosong agar sesuai contoh keluaran
print(f"Titik A      : ({x1:.2f}, {y1:.2f})")
print(f"Titik B      : ({x2:.2f}, {y2:.2f})")
print(f"Perubahan    : dx = {dx:.2f}, dy = {dy:.2f}")
print(f"Jarak A ke B : {jarak:.2f}")
print(f"Titik tengah : ({tengah_x:.2f}, {tengah_y:.2f})")