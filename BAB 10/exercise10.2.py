from pathlib import Path

# Mengambil lokasi folder tempat program disimpan
folder_program = Path(__file__).parent

# Mengakses file learning_python.txt di folder BAB 10
path = folder_program / "learning_python.txt"

# Membaca isi file
contents = path.read_text(encoding="utf-8")

# Mengganti kata Python menjadi C
for line in contents.splitlines():
    kalimat = line.replace("Python", "C")
    print(kalimat)
