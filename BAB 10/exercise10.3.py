from pathlib import Path

folder = Path(__file__).parent
file = folder / "learning_python.txt"

if not file.exists():
    file.write_text(
        "I love learning Python.\n"
        "Python is interesting.\n"
        "Python is easy to learn.\n",
        encoding="utf-8"
    )

lines = file.read_text(encoding="utf-8").splitlines()

for line in lines:
    print(line)