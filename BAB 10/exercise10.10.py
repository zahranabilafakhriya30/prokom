from pathlib import Path

folder = Path(__file__).parent
file = folder / "book.txt"

if not file.exists():
    file.write_text(
        "Python is a programming language. "
        "Python is easy to learn. "
        "Learning Python is interesting.",
        encoding="utf-8"
    )

text = file.read_text(encoding="utf-8")

word = "Python"
jumlah = text.lower().count(word.lower())

print(f"Kata '{word}' muncul sebanyak {jumlah} kali.")