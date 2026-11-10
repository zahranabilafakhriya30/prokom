from random import choice

daftar_lottery = [
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10,
    "A", "B", "C", "D", "E"
]

hasil = []

for i in range(4):
    angka = choice(daftar_lottery)
    hasil.append(angka)
    daftar_lottery.remove(angka)

print("Tiket yang memenangkan hadiah:", hasil)