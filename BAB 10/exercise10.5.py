from pathlib import Path

folder = Path(__file__).parent
file = folder / "guest_book.txt"

while True:
    name = input("Rara (ketik 'quit' untuk berhenti): ")

    if name.lower() == "quit":
        break

    print(f"Hello, {name}! Selamat datang.")

    with file.open("a", encoding="utf-8") as f:
        f.write(name + " mengunjungi program.\n")

print("Program selesai.")