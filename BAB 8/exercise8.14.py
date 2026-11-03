def buat_mobil(merek, tipe, **informasi):
    mobil = {
        "merek": merek,
        "tipe": tipe
    }

    for kunci, nilai in informasi.items():
        mobil[kunci] = nilai

    return mobil


mobil = buat_mobil(
    "Toyota",
    "Avanza",
    warna="Hitam",
    tahun=2025,
    transmisi="Otomatis"
)

print(mobil)