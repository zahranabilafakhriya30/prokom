buah_favorit = ["Mangga", "Apel", "Jeruk"]

buah = input("Masukkan nama buah: ")

if buah.lower() in [item.lower() for item in buah_favorit]:
    print(f"Anda benar-benar menyukai {buah}!")
else:
    print(f"{buah} bukan buah favorit Anda.")