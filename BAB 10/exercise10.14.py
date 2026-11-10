from pathlib import Path
import json

folder = Path(__file__).parent
file = folder / "user_dictionary.json"

if file.exists():
    username = json.loads(file.read_text(encoding="utf-8"))

    answer = input(
        f"Are you {username}? (yes/no): "
    )

    if answer.lower() == "yes":
        print(f"Welcome back, {username}!")

    else:
        username = input("What is your name? ")

        file.write_text(
            json.dumps(username),
            encoding="utf-8"
        )

        print(f"We'll remember you, {username}!")

else:
    username = input("What is your name? ")

    file.write_text(
        json.dumps(username),
        encoding="utf-8"
    )

    print(f"We'll remember you, {username}!")