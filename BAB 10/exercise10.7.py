while True:
    try:
        angka1 = input("Masukkan angka pertama (q untuk keluar): ")

        if angka1.lower() == "q":
            break

        angka2 = input("Masukkan angka kedua: ")

        if angka2.lower() == "q":
            break

        hasil = int(angka1) + int(angka2)

        print(f"Hasil: {hasil}")

    except ValueError:
        print("Masukkan angka yang valid!")

print("Program selesai.")