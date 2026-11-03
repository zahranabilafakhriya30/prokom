negara = ["Indonesia", "Jepang", "Korea", "Malaysia"]

print("Daftar awal:", negara)

print("Elemen pertama:", negara[0])
print("Elemen terakhir:", negara[-1])

negara.append("Thailand")
print("Setelah append:", negara)

negara.insert(1, "Singapura")
print("Setelah insert:", negara)

del negara[2]
print("Setelah del:", negara)

negara.remove("Malaysia")
print("Setelah remove:", negara)

negara.sort()
print("Setelah sort:", negara)

negara.reverse()
print("Setelah reverse:", negara)

print("Jumlah negara:", len(negara))