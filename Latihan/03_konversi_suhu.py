# latihan/03_konversi_suhu.py
# Program konversi suhu dari Celsius ke Fahrenheit dan Kelvin

# Konstanta
KELVIN_OFFSET = 273.15

# Input suhu dalam Celsius
celsius = float(input("Masukkan suhu dalam Celsius: "))

# Konversi ke Fahrenheit dan Kelvin
fahrenheit = (9 / 5) * celsius + 32
kelvin = celsius + KELVIN_OFFSET

# Tampilkan hasil
print(f"Suhu Celsius    : {celsius:.2f} °C")
print(f"Suhu Fahrenheit : {fahrenheit:.2f} °F")
print(f"Suhu Kelvin     : {kelvin:.2f} K")