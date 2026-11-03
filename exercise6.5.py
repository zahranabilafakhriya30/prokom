sungai = {
    "Nil": "Mesir",
    "Amazon": "Brasil",
    "Kapuas": "Indonesia"
}

for nama_sungai, negara in sungai.items():
    print(f"Sungai {nama_sungai} mengalir melalui {negara}.")

print("\nDaftar sungai:")
for nama_sungai in sungai.keys():
    print(nama_sungai)

print("\nDaftar negara:")
for negara in sungai.values():
    print(negara)