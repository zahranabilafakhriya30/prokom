usia = int(input("Masukkan usia Anda: "))

if usia < 2:
    print("Anda masih bayi.")
elif usia < 4:
    print("Anda sedang balita.")
elif usia < 13:
    print("Anda masih anak-anak.")
elif usia < 20:
    print("Anda sedang remaja.")
elif usia < 65:
    print("Anda sudah dewasa.")
else:
    print("Anda termasuk lanjut usia.")