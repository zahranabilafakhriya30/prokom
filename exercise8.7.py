def buat_album(nama_penyanyi, judul_album, jumlah_lagu=None):
    album = {
        "penyanyi": nama_penyanyi,
        "album": judul_album
    }

    if jumlah_lagu is not None:
        album["jumlah_lagu"] = jumlah_lagu

    return album


print(buat_album("Taylor Swift", "Midnights"))
print(buat_album("Ariana Grande", "Positions"))
print(buat_album("LANY", "mamasboy", 10))