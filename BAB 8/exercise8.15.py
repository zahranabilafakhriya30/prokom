def cetak_model(desain_awal, desain_selesai):
    while desain_awal:
        model = desain_awal.pop()

        print(f"Mencetak model: {model}")

        desain_selesai.append(model)


desain_awal = ["Model A", "Model B", "Model C"]
desain_selesai = []

cetak_model(desain_awal[:], desain_selesai)

print("\nModel yang telah selesai:")
print(desain_selesai)