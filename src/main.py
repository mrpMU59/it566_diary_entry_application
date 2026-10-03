""" Interactive Diary Application. """

from datetime import datetime

import diary

""" Print a list of entries, or a message if the list is empty. """
def print_entries(entries):
    if not entries:
        print("No entries found.")
        return
    for entry in entries:
        print(entry)


""" Ask the user for a date until a valid one is entered. """
def ask_for_date():
    while True:
        entered_date = input("Enter a date (YYYY-MM-DD): ")
        if diary.is_valid_date(entered_date):
            return entered_date

        print("Invalid date. Please use the format YYYY-MM-DD.")


""" Wait for the user before showing the menu again. """
def return_to_menu():
    input("\nPress Enter to return to the menu.")


""" Show numbered entries and delete the one the user picks. """
def delete_entry(filename):
    entries = diary.read_entries(filename)
    
    if not entries:
        print("No entries to delete.")
        return

    for entry_number, entry in enumerate(entries, start=1):
        print(f"{entry_number}. {entry}")

    choice = input("Enter the number of the entry to delete: ")
    if choice.isdigit() and 1 <= int(choice) <= len(entries):
        diary.delete_entry(filename, int(choice))
        print("Entry deleted.")

    else:
        print("Invalid number.")


def main():
    filename = "diary.txt"

    while True:
        print("==================================")
        print(f"Current diary file: {filename}")
        print("1. Add entry")
        print("2. Print all entries")
        print("3. Print entries by date")
        print("4. Load a different diary file")
        print("5. Delete an entry")
        print("6. Quit")
        print("==================================")

        choice = input("Choose an option: ")

        if choice == "1":
            entered_date = input("\n" + "Date (YYYY-MM-DD, press ENTER for today): ")
            
            if entered_date == "":
                entered_date = datetime.now().strftime(diary.date_format)

            elif not diary.is_valid_date(entered_date):
                print("\n" + "Invalid date. Please use the format YYYY-MM-DD.")
                continue

            entry_text = input("Write your entry: ")
            diary.add_entry(filename, entered_date, entry_text)
            print("Entry saved.")
        
        elif choice == "2":
            print("\n")
            print_entries(diary.read_entries(filename))

        elif choice == "3":
            entered_date = ask_for_date()
            print("\n")
            print_entries(diary.filter_entries(filename, entered_date))

        elif choice == "4":
            print("\n")
            filename = input("Enter the diary file name: ")
            print(f"Now using {filename}")

        elif choice == "5":
            print("\n")
            delete_entry(filename)

        elif choice == "6":
            print("\n" + "Goodbye!")
            break

        else:
            print("\n" + "Invalid option. Please choose 1-5.")

        return_to_menu()


if __name__ == "__main__":
    main()

        

