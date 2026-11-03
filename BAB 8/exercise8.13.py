def buat_profil(nama_depan, nama_belakang, **informasi):
    profil = {
        "nama_depan": nama_depan,
        "nama_belakang": nama_belakang
    }

    for kunci, nilai in informasi.items():
        profil[kunci] = nilai

    return profil


profil_pengguna = buat_profil(
    "Zahra",
    "Nabila",
    jurusan="Teknik Industri",
    universitas="UNS",
    kota="Kediri"
)

print(profil_pengguna)