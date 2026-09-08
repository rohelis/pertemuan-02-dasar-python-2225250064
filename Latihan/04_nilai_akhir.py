# Menerima input dari pengguna
nama = input("Masukkan nama: ")
nilai_tugas = float(input("Masukkan nilai Tugas: "))
nilai_uts = float(input("Masukkan nilai UTS: "))
nilai_uas = float(input("Masukkan nilai UAS: "))

# Menghitung nilai akhir berdasarkan bobot 
# (Tugas 20%, UTS 30%, UAS 50%)
nilai_akhir = (nilai_tugas * 0.20) + (nilai_uts * 0.30) + (nilai_uas * 0.50)

# Menampilkan hasil dengan dua angka desimal
print(f"\nNama: {nama}")
print(f"Nilai Akhir: {nilai_akhir:.2f}")