from pathlib import Path

folder = Path(__file__).parent

files = ["cats.txt", "dogs.txt"]

for filename in files:
    path = folder / filename

    try:
        contents = path.read_text(encoding="utf-8")
        print(f"\nIsi file {filename}:")
        print(contents)

    except FileNotFoundError:
        pass