from pathlib import Path

folder_program = Path(__file__).parent
nama_file = folder_program / "learning_python.txt"

isi = [
    "I love learning Python.\n",
    "Python is easy to learn.\n",
    "Python is very interesting.\n"
]

# Membuat file jika belum tersedia
if not nama_file.exists():
    nama_file.write_text("".join(isi), encoding="utf-8")

# Membaca file
teks = nama_file.read_text(encoding="utf-8")

print(teks)