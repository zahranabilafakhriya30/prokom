def hitung_luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    return luas


def tampilkan_hasil(panjang, lebar):
    luas = hitung_luas_persegi_panjang(panjang, lebar)

    print(f"Panjang: {panjang} cm")
    print(f"Lebar: {lebar} cm")
    print(f"Luas: {luas} cm persegi")


tampilkan_hasil(10, 5)