import csv
import time
import os
from validate_date import validate_Date
from clear_Screen import Clear_Screen
from module import Maximum, find_max_lengths, length

class taskViewer:

    def __init__(self, filename="tasks.csv"):
        self.filename = filename
        self.tasks = self.load_tasks()
        print(f"success with {filename}")

    def load_tasks(self):
        tasks = []
        
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', newline='') as file:
                    reader = csv.DictReader(file)
                    tasks = [row for row in reader]
            except (csv.Error, FileNotFoundError):
                print("Error on load_tasks")
                return []
        return tasks

    def save_tasks(self):
        
        with open(self.filename, 'w', newline='') as file:
            fieldnames = ['task', 'deadline', 'status']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.tasks)
            print(f"Data successfully saved at {file}")

    def add_task(self, task, deadline, status="Pending"):
        self.tasks += ({
            "task": task,
            "deadline": deadline,
            "status": status
        })
        
        print(f"self.tasks = {self.tasks}")
        print(f"Type = {type(self.tasks)}")
        if self.tasks:
            print(f"First 3 items: {self.tasks[:3] if len(self.tasks) >= 3 else self.tasks}")

    def delete_task(self):
        pass
    
    def edit_task(self):
        pass
        
    def create_table(self):
        if not self.tasks:
            return "No tasks available!"

        task_width, deadline_width, status_width = find_max_lengths(self.tasks)

        task_width = int(Maximum(task_width, length("Task")) + 2)
        deadline_width = int(Maximum(deadline_width, length("Deadline")) + 2)
        status_width = int(Maximum(status_width, length("Status")) + 2)

        top_border = "┌" + "─" * task_width + "┬" + "─" * deadline_width + "┬" + "─" * status_width + "┐"
        print(top_border)
        header = f"│{'Task':^{task_width}}│{'Deadline':^{deadline_width}}│{'Status':^{status_width}}│"
        print(header)
        separator = "├" + "─" * task_width + "┼" + "─" * deadline_width + "┼" + "─" * status_width + "┤"
        print(separator)
        for task in self.tasks:
            row = f"│{task:<{task_width}}│{task['deadline']:^{deadline_width}}│{task['status']:^{status_width}}│"
            print(row)
        bottom_border = "└" + "─" * task_width + "┴" + "─" * deadline_width + "┴" + "─" * status_width + "┘"
        print(bottom_border)
        

    def display_tasks(self):
        print(self.create_table())