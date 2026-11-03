daftar_tamu = ["Fira", "Matin", "Hafizh", "Rakha", "Oca", "Nayfa"]

print("Meja makan hanya tersedia untuk dua orang.")

while len(daftar_tamu) > 2:
    tamu = daftar_tamu.pop()
    print(f"Maaf {tamu}, undangan dibatalkan.")

for tamu in daftar_tamu:
    print(f"{tamu}, undanganmu masih berlaku.")

del daftar_tamu[0]
del daftar_tamu[0]

print("Daftar tamu akhir:", daftar_tamu)