def buat_sandwich(*isi):
    print("\nSandwich dengan isi:")

    for bahan in isi:
        print(f"- {bahan}")


buat_sandwich("Keju", "Tomat")
buat_sandwich("Daging", "Selada", "Saus")
buat_sandwich("Telur", "Mayones", "Timun")