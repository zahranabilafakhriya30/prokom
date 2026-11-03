while True:
    usia = input("Masukkan usia Anda (ketik 'selesai' untuk keluar): ")

    if usia.lower() == "selesai":
        break

    usia = int(usia)

    if usia < 3:
        harga = 0
    elif usia <= 12:
        harga = 10
    else:
        harga = 15

    if harga == 0:
        print("Tiket gratis.")
    else:
        print(f"Harga tiket adalah Rp{harga}.")