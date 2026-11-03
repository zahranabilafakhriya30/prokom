orang_1 = {
    "nama": "Nadia",
    "usia": 18,
    "kota": "Surakarta"
}

orang_2 = {
    "nama": "Oca",
    "usia": 20,
    "kota": "Kediri"
}

orang_3 = {
    "nama": "Fira",
    "usia": 19,
    "kota": "Yogyakarta"
}

orang = [orang_1, orang_2, orang_3]

for data in orang:
    print("\nNama:", data["nama"])
    print("Usia:", data["usia"])
    print("Kota:", data["kota"])