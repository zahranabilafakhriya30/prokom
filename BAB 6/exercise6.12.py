kota = {
    "Kediri": {
        "provinsi": "Jawa Timur",
        "ciri_khas": "Tahu Takwa"
    },
    "Surakarta": {
        "provinsi": "Jawa Tengah",
        "ciri_khas": "Batik"
    },
    "Yogyakarta": {
        "provinsi": "Daerah Istimewa Yogyakarta",
        "ciri_khas": "Gudeg"
    }
}

for nama, informasi in kota.items():
    print(f"\nNama kota: {nama}")
    print("Provinsi:", informasi["provinsi"])
    print("Ciri khas:", informasi["ciri_khas"])