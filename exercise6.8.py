hewan_1 = {
    "jenis": "Kucing",
    "pemilik": "Rara"
}

hewan_2 = {
    "jenis": "Anjing",
    "pemilik": "Matin"
}

hewan_3 = {
    "jenis": "Kelinci",
    "pemilik": "Nadia"
}

hewan = [hewan_1, hewan_2, hewan_3]

for data in hewan:
    print(f"{data['pemilik']} memiliki {data['jenis']}.")