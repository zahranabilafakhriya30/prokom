from pathlib import Path

folder = Path(__file__).parent
file = folder / "guest.txt"

name = input("Masukkan nama Anda: ")

with file.open("a", encoding="utf-8") as f:
    f.write(name + "\n")

print("Nama berhasil disimpan!")