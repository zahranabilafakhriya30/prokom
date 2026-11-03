ide_program = [
    "Program menghitung nilai mahasiswa.",
    "Program menghitung biaya produksi.",
    "Program menghitung persediaan barang.",
    "Program mengatur jadwal kegiatan.",
    "Program menghitung keuntungan penjualan."
]

print("Daftar ide program:")

for nomor, ide in enumerate(ide_program, start=1):
    print(f"{nomor}. {ide}")