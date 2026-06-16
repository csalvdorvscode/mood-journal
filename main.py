

import random
import json
from datetime import datetime

quotes = [
    "Everything starts with you.",
    "Small steps are still progress.",
    "Your future is created today.",
    "Trust the process."
]


def write_entry():

    mood = input("How are you feeling today? ")
    entry = input("Write your journal entry: ")

    date = datetime.now().strftime("%Y-%m-%d %H:%M")

    new_entry = {
        "date": date,
        "mood": mood,
        "entry": entry
    }

    try:

        with open("journal.json", "r") as file:
            data = json.load(file)

    except:
        data = []

    data.append(new_entry)

    with open("journal.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Entry saved successfully.\n")


def view_entries():

    try:

        with open("journal.json", "r") as file:
            data = json.load(file)

            if not data:
                print("No entries found.\n")

            else:

                print("\n--- YOUR ENTRIES ---")

                for entry in data:

                    print(f"\nDate: {entry['date']}")
                    print(f"Mood: {entry['mood']}")
                    print(f"Entry: {entry['entry']}")

    except FileNotFoundError:
        print("Journal file not found.\n")

def mood_stats():

    try:

        with open("journal.json", "r") as file:
            data = json.load(file)

        if not data:
            print("No entries found.\n")
            return

        stats = {}

        for entry in data:

            mood = entry["mood"]

            if mood in stats:
                stats[mood] += 1

            else:
                stats[mood] = 1

        print("\n--- MOOD STATISTICS ---")

        for mood, count in stats.items():
            print(f"{mood}: {count}")

        print()

    except FileNotFoundError:
        print("Journal file not found.\n")

def search_by_mood():

    search_mood = input("Enter mood to search: ")

    try:

        with open("journal.json", "r") as file:
            data = json.load(file)

        found = False

        print("\n--- SEARCH RESULTS ---")

        for entry in data:

            if entry["mood"].lower() == search_mood.lower():

                print(f"\nDate: {entry['date']}")
                print(f"Mood: {entry['mood']}")
                print(f"Entry: {entry['entry']}")

                found = True

        if not found:
            print("No entries found for this mood.")

        print()

    except FileNotFoundError:
        print("Journal file not found.\n")

def random_quote():
    print("\n" + random.choice(quotes) + "\n")


def menu():

    while True:

        print("=== MOOD JOURNAL ===")
        print("1. Write entry")
        print("2. View entries")
        print("3. Random quote")
        print("4. Mood statistics")
        print("5. Search by mood")
        print("6. Exit")

        choice = input("Choose an option: ")

        match choice:

            case "1":
                write_entry()

            case "2":
                view_entries()

            case "3":
                random_quote()

            case "4":
                mood_stats()
            case "5":
                search_by_mood()

            case "6":
                print("Goodbye!")
                break

            case _:
                print("Invalid option.\n")


menu()
