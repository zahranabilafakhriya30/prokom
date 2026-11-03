# import geometri as geo
from geometri import luasLingkaran, volTabung

jari2 = float(input("Masukkan jari-jari lingkaran: "))
tinggi = float(input("Masukkan tinggi tabung"))
# VolTab = geo.volTabung(geo.luasLingkaran(jari2), tinggi)
VolTab = volTabung(luasLingkaran(jari2), tinggi)

print("Volume Tabung", VolTab)