import os
import json
from module import length, Maximum, find_max_Journal, number_task

class Journaltracker:

    def __init__(self, filename="journals.json"):
        self.filename = filename
        self.journals = self.load_journals()

    def load_journals(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    return json.load(file)
            except (json.JSONDecodeError, FileNotFoundError):
                return []
        return []

    def save_journals(self):
        with open(self.filename, 'w') as file:
            json.dump(self.journals, file, indent=4)

    def add_journal(self, title, entry):
        self.journals.append({
            "title": title,
            "entry": entry
        })

    def read_journal(self, index):
        journal = self.journals[index]

        title_width = length(journal["title"])

        print(journal["title"])
        print("─" * title_width)

        input(f"\n{journal["entry"]}")

    def delete_journal(self, index):
        journal = self.journals

        confirmation = input(f"Are you sure you want to delete journal with the title \"{journal[index]["title"]}\" (Y/N)? ")

        if  confirmation  == "Y" or confirmation == "y":
            journal.pop(index)
            self.save_journals()

    def display_journals(self):
        if not self.journals:
            return ""
        
        title_width = find_max_Journal(self.journals)
        number_width = number_task(self.journals)
        

        number_width = int(Maximum(number_width, len("No."))) + 2
        title_width = int(Maximum(title_width, len("Title"))) + 2

        top_border = "┌" + "─" * number_width + "┬" + "─" * title_width + "┐"
        print(top_border)

        header = f"│{'No.':^{number_width}}│{'Journal':^{title_width}}│"
        print(header)

        separator = "├" + "─" * number_width + "┼" + "─" * title_width + "┤"
        print(separator)

        for index, journal in enumerate(self.journals):
            row = f"│{str(index + 1):^{number_width}}│{journal['title']:<{title_width}}│"
            print(row)

        bottom_border = "└" + "─" * number_width + "┴" + "─" * title_width + "┘"
        print(bottom_border)

    def count(self):
        journal = self.journals
        return length(journal)