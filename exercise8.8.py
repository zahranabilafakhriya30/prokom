def buat_album(nama_penyanyi, judul_album):
    return {
        "penyanyi": nama_penyanyi,
        "album": judul_album
    }


while True:
    print("\nMasukkan informasi album.")
    print("Ketik 'q' untuk keluar.")

    penyanyi = input("Nama penyanyi: ")

    if penyanyi.lower() == "q":
        break

    album = input("Judul album: ")

    if album.lower() == "q":
        break

    hasil = buat_album(penyanyi, album)

    print(hasil)