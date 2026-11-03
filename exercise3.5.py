daftar_tamu = ["Matin", "Hafizh", "Oca"]

print(f"{daftar_tamu[0]} tidak dapat hadir.")
daftar_tamu[0] = "Rakha"

for tamu in daftar_tamu:
    print(f"Halo {tamu}, kamu diundang makan malam.")