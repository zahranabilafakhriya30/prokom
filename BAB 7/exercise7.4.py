print("Masukkan topping pizza.")
print("Ketik 'selesai' untuk mengakhiri.")

while True:
    topping = input("Topping: ")

    if topping.lower() == "selesai":
        break

    print(f"Menambahkan {topping} ke pizza.")