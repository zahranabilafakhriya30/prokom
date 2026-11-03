pesan = "\nMasukkan sesuatu untuk ditampilkan."
pesan += "\nKetik 'keluar' untuk berhenti."

aktif = True

while aktif:
    jawaban = input(pesan)

    if jawaban.lower() == "keluar":
        aktif = False
    else:
        print(jawaban)