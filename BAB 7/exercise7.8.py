pesanan = ["Sandwich", "Roti", "Burger"]

sandwich_selesai = []

while pesanan:
    makanan = pesanan.pop()

    print(f"Pesanan {makanan} sedang dibuat.")

    sandwich_selesai.append(makanan)

print("\nDaftar pesanan selesai:")

for makanan in sandwich_selesai:
    print(makanan)