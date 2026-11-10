from random import choice

daftar_lottery = [
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10,
    "A", "B", "C", "D", "E"
]

my_ticket = [1, "A", 5, "C"]

percobaan = 0

while True:
    hasil = []

    for i in range(4):
        angka = choice(daftar_lottery)
        hasil.append(angka)
        daftar_lottery.remove(angka)

    percobaan += 1

    if set(hasil) == set(my_ticket):
        break

print("Tiket berhasil menang!")
print("Jumlah percobaan:", percobaan)