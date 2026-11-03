pesanan = [
    "Sandwich",
    "Pastrami",
    "Burger",
    "Pastrami",
    "Roti",
    "Pastrami"
]

print("Pastrami sedang habis.")

while "Pastrami" in pesanan:
    pesanan.remove("Pastrami")

print("\nDaftar pesanan:")
for makanan in pesanan:
    print(makanan)