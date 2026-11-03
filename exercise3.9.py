lokasi = ["Bali", "Jakarta", "Bandung", "Yogyakarta", "Surabaya"]

print("Daftar awal:", lokasi)

print("Urutan alfabetis:", sorted(lokasi))

print("Daftar awal:", lokasi)

print("Urutan terbalik:", sorted(lokasi, reverse=True))

lokasi.reverse()
print("Setelah reverse:", lokasi)

lokasi.reverse()
print("Kembali seperti semula:", lokasi)

lokasi.sort()
print("Urutan permanen:", lokasi)

lokasi.sort(reverse=True)
print("Urutan alfabetis terbalik:", lokasi)