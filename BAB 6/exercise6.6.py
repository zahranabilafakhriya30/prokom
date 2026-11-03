bahasa_favorit = {
    "Nadia": "Python",
    "Rara": "Java",
    "Fira": "C++",
    "Yota": "Python"
}

peserta = ["Nadia", "Rara", "Fira", "Yota", "Nayfa"]

for nama in peserta:
    if nama in bahasa_favorit:
        print(f"Terima kasih {nama} sudah mengikuti polling.")
    else:
        print(f"Halo {nama}, silakan ikuti polling.")