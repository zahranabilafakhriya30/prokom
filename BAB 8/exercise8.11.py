def tampilkan_pesan(daftar_pesan):
    for pesan in daftar_pesan:
        print(pesan)


def kirim_pesan(daftar_pesan, pesan_terkirim):
    while daftar_pesan:
        pesan = daftar_pesan.pop()
        pesan_terkirim.append(pesan)


daftar_pesan = [
    "Halo semuanya!",
    "Selamat belajar!",
    "Semoga sukses!"
]

pesan_terkirim = []

kirim_pesan(daftar_pesan[:], pesan_terkirim)

print("Daftar pesan asli:")
tampilkan_pesan(daftar_pesan)

print("\nDaftar pesan terkirim:")
tampilkan_pesan(pesan_terkirim)