from pathlib import Path
import json

folder = Path(__file__).parent
file = folder / "favorite_number.json"

if file.exists():
    favorite_number = json.loads(
        file.read_text(encoding="utf-8")
    )
    print(f"Your favorite number is {favorite_number}!")

else:
    favorite_number = input("What is your favorite number? ")

    file.write_text(
        json.dumps(favorite_number),
        encoding="utf-8"
    )

    print("Your favorite number has been saved!")