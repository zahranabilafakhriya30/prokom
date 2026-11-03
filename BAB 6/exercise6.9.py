tempat_favorit = {
    "Rara": ["Bali", "Bandung"],
    "Fira": ["Jakarta", "Surabaya"],
    "Nadia": ["Yogyakarta", "Malang"]
}

for nama, tempat in tempat_favorit.items():
    print(f"\nTempat favorit {nama}:")
    for lokasi in tempat:
        print(f"- {lokasi}")