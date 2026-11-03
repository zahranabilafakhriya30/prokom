angka_favorit = {
    "Rara": [7, 10],
    "Nadia": [5, 15],
    "Oca": [3, 8],
    "Fira": [9, 12],
    "Yota": [4, 20]
}

for nama, angka in angka_favorit.items():
    print(f"\nAngka favorit {nama}:")
    for nilai in angka:
        print(nilai)