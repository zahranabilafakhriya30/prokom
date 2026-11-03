pengguna_sekarang = [
    "Nadia",
    "Rara",
    "Hafizh",
    "Matin",
    "Nayfa"
]

pengguna_baru = [
    "Rofiq",
    "Rakha",
    "Fadlan",
    "Yota",
    "Fira"
]

pengguna_sekarang_kecil = [
    nama.lower() for nama in pengguna_sekarang
]

for nama in pengguna_baru:
    if nama.lower() in pengguna_sekarang_kecil:
        print(f"Nama {nama} sudah digunakan.")
    else:
        print(f"Nama {nama} tersedia.")