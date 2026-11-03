kota = {
    "Jakarta": {
        "negara": "Indonesia",
        "populasi": "Lebih dari 10 juta",
        "fakta": "Merupakan ibu kota Indonesia sebelumnya."
    },
    "Tokyo": {
        "negara": "Jepang",
        "populasi": "Sekitar 14 juta",
        "fakta": "Merupakan pusat pemerintahan Jepang."
    },
    "Paris": {
        "negara": "Prancis",
        "populasi": "Sekitar 2 juta",
        "fakta": "Terkenal dengan Menara Eiffel."
    }
}

for nama_kota, informasi in kota.items():
    print(f"\nKota: {nama_kota}")
    print("Negara:", informasi["negara"])
    print("Populasi:", informasi["populasi"])
    print("Fakta:", informasi["fakta"])