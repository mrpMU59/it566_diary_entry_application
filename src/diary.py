""" Functions for reading, writing, and managing dated diary entries from user input. 
    Each entry is stored as one line in a text file in the format: YYYY-MM-DD | entry text """

from datetime import datetime

date_format = "%Y-%m-%d"


""" Returns True of the text is a valid date in YYYY-MM-DD format."""
def is_valid_date(entry_date):
    try:
        datetime.strptime(entry_date, date_format)
        return True
    except ValueError:
        return False



""" Add one entry as a new line in the file. """
def add_entry(filename, entry_text, entry_date):
    with open(filename, "a") as file:
        file.write(f"{entry_date} | {entry_text}\n")


""" Return all entries from the diary file as a list of lines. """
def read_entries(filename):
    entries = []
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if line != "":
                    entries.append(line)

    except FileNotFoundError:
        pass
    
    return entries


""" Return specifc entries by the given date. """
def filter_entries(filename, entry_date):
    entries = read_entries(filename)
    matching_entries = []
    for entry in entries:
        if entry.startswith(entry_date + ":"):
            matching_entries.append(entry)
    return matching_entries


""" Return today's date as YYYY-MM-DD. """
def get_today():
    return str(datetime.today())


""" Delete a specific entry. """
def delete_entry(filename, entry_number):
    entries = read_entries(filename)
    entries.pop(entry_number - 1)
    with open(filename, "w") as file:
        for entry in entries:
            file.write(entry + "\n")