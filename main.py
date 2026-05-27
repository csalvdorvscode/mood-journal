

import random

quotes = [
    "Everything starts with you.",
    "Small steps are still progress.",
    "Your future is created today.",
    "Trust the process."
]


def write_entry():
    entry = input("Write your journal entry: ")

    with open("journal.txt", "a") as file:
        file.write(entry + "\n")

    print("Entry saved successfully.\n")


def view_entries():
    try:
        with open("journal.txt", "r") as file:
            content = file.read()

            if content == "":
                print("No entries found.\n")
            else:
                print("\n--- YOUR ENTRIES ---")
                print(content)

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
        print("4. Exit")

        choice = input("Choose an option: ")

        match choice:

            case "1":
                write_entry()

            case "2":
                view_entries()

            case "3":
                random_quote()

            case "4":
                print("Goodbye!")
                break

            case _:
                print("Invalid option.\n")


menu()
