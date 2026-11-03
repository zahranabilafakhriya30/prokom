def tampilkan_pesan(daftar_pesan):
    for pesan in daftar_pesan:
        print(pesan)


def kirim_pesan(daftar_pesan, pesan_terkirim):
    while daftar_pesan:
        pesan = daftar_pesan.pop()

        print(f"Mengirim pesan: {pesan}")

        pesan_terkirim.append(pesan)


daftar_pesan = [
    "Selamat pagi!",
    "Semangat belajar!",
    "Jangan menyerah!"
]

pesan_terkirim = []

kirim_pesan(daftar_pesan[:], pesan_terkirim)

print("\nPesan yang berhasil dikirim:")
tampilkan_pesan(pesan_terkirim)