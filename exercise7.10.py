hasil_polling = {}

aktif = True

while aktif:
    nama = input("\nMasukkan nama Anda: ")
    tujuan = input("Ke mana Anda ingin berlibur? ")

    hasil_polling[nama] = tujuan

    ulang = input("Apakah ingin membiarkan orang lain menjawab? (ya/tidak): ")

    if ulang.lower() == "tidak":
        aktif = False

print("\nHasil polling:")

for nama, tujuan in hasil_polling.items():
    print(f"{nama} ingin berlibur ke {tujuan}.")